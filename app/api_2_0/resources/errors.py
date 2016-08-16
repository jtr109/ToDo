from flask import jsonify
from api_app.exceptions import ValidationError
from api_app.api_2_0 import api2


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api2.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
