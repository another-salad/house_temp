"""All Enums"""

from enum import IntEnum


class RequestTypes(IntEnum):
    """HTTP Request Types"""
    GET = 0
    POST = 1


class HTTPErrorCodes(IntEnum):
    """HTTP standard error codes"""
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
