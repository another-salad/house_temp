"""The DB object, inherits from Requester"""


from common import ACCESS_TOKEN_KEY, UN, PW
from common.exceptions import JWTError
from common.enums import RequestTypes
from common.requester import Requester
from common.secret_read import get_secret


class DB(Requester):
    """The DB object, inherits from Requester"""

    call = "call"
    auth = "auth"

    def __init__(self) -> None:
        super().__init__()
        self.db_host = self.hosts.db
        self.headers = self.headers | {"Authorization": f"Bearer {self.token}"}

    @property
    def username(self):
        """The DB username"""
        return get_secret(file_name=UN)

    @property
    def password(self):
        """The DB password"""
        return get_secret(file_name=PW)

    @property
    def token(self):
        """The JWT token for the DB connection"""
        error, resp = self.request(method=RequestTypes.POST, uri=f"{self.hosts.db}/{self.auth}", args={"username": self.username, "password": self.password})
        if error:
            raise JWTError(f"Token not returned. Response: {resp}")

        return resp[ACCESS_TOKEN_KEY]
