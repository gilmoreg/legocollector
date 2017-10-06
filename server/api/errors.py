''' Custom error handler '''
class FlaskError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        ''' Constructor '''
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        ''' Repr as dict '''
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv