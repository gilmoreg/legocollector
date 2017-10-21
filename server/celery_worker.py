# /server/celery_worker.py
from os import environ
from celery import Celery
from celery.signals import task_postrun
from celery.schedules import crontab
from celery.utils.log import get_task_logger


from api.app import create_app
from api.database import db
from api.controllers.legoset_controller import LegoSetController


def create_celery(app):
    celery = Celery(app.import_name,
                    broker=environ['RABBITMQ_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


flask_app = create_app()
celery = create_celery(flask_app)
logger = get_task_logger(__name__)


@celery.task
def update_stock_levels():
    logger.info('worker updating stock levels')
    legoset_controller = LegoSetController()
    legoset_controller.update_stock_levels()


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes daily at midnight
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        update_stock_levels.s(), name='update stock levels every minute'
    )


@task_postrun.connect
def close_session(*args, **kwargs):
    # Flask SQLAlchemy will automatically create new sessions for you from
    # a scoped session factory, given that we are maintaining the same app
    # context, this ensures tasks have a fresh session (e.g. session errors
    # won't propagate across tasks)
    db.session.remove()