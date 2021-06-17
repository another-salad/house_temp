

class InvalidParameterError(BaseException):
    """Raised when a supplied parameter is invalid"""


class JWTError(BaseException):
    """Raised when no JWT is returned"""


class SensorError(BaseException):
    """Raised when the temp sensor doesn't resond as expected"""


class SetTempError(BaseException):
    """Raised when an error occurs when attempting to save the sensor temp to the DB"""