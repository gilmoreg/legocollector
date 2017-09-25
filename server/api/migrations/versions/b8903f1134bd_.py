"""empty message

Revision ID: b8903f1134bd
Revises: 
Create Date: 2017-09-24 23:59:05.186280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8903f1134bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('legoset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('stocklevel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lego_set', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('stock_level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lego_set'], ['legoset.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('watch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('lego_set', sa.Integer(), nullable=True),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['lego_set'], ['legoset.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watch')
    op.drop_table('stocklevel')
    op.drop_table('user')
    op.drop_table('legoset')
    # ### end Alembic commands ###
