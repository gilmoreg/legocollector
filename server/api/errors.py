''' Custom error handler '''
from flask import jsonify, current_app

class FlaskError(Exception):
    ''' Generic Exception for returning error information '''
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

    
    def __str__(self):
        return '<FlaskError message: {} status_code: {} payload: {}>'.format(self.message, self.status_code, self.payload)


    def json_response(self):
        print('FlaskError', self) # TODO log properly
        return jsonify({'error': self.message}), self.status_code


def exception_json_response(exception):
    ''' Static helper method to return JSON response with error message '''
    print('Exception', exception) # TODO log properly
    if current_app.config['ENV'] == 'prod':
        return jsonify({'error': 'Something went wrong'}), 500
    if isinstance(exception, FlaskError):
        return exception.json_response()
    return jsonify({'error': str(exception)}), 500
