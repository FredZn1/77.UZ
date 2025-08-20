from rest_framework.exceptions import APIException


class ObjectNotFound(APIException):
    status_code = 404
    default_detail = "The requested object was not found."
    default_code = "not_found"
