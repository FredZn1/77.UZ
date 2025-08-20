from rest_framework.exceptions import APIException


class ObjectNotFound(APIException):

    status_code = 404
    default_detail = "Requested object was not found."
    default_code = "not_found"
