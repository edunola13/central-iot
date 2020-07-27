from rest_framework.exceptions import APIException
from rest_framework import status


class ConflictError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Conflict'


class ServiceUnavailableError(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


class BussinesLogicError(Exception):
    def __init__(self, key, message):
        super().__init__(message)
        self.key = key
        self.message = message
