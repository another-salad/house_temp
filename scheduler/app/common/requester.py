import requests
from json import loads

from common.conf_read import get_conf
from common.enums import HTTPErrorCodes, RequestTypes
from common.exceptions import InvalidParameterError


class Requester:
    """The base class for handling GET/POST commands"""

    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    http_methods = {RequestTypes.GET: "get", RequestTypes.POST: "post"}
    hosts = None

    @property
    def hosts(self):
        """All the host addresses from the config file"""
        return get_conf()

    def request(self, method: int, uri: str, ssl: bool = False, args: dict = None) -> tuple:
        """Sends a GET/POST request to a URI, args optional

        Args:
            method (int): 0 GET, 1 POST
            uri (str): The host to send a request to
            ssl (bool): True for SSL else False
            args (dict, optional): The args to send with the request (json serializable). Defaults to None.

        Returns:
            tuple: error (bool), return_vals (dict, string, exception)
        """
        error = False
        return_vals = None
        if method not in self.http_methods.keys():
            raise InvalidParameterError(f"HTTP method key {method} not found. Supported methods: {self.http_methods}")

        req = getattr(requests, self.http_methods[method])
        uri_prefix = "https" if ssl else "http"
        uri = f"{uri_prefix}://{uri}"
        req_kwargs = {"url": uri, "headers": self.headers}
        if args:
            req_kwargs.update({"json": args})

        try:

            response = req(**req_kwargs)
            if response.status_code != HTTPErrorCodes.OK:
                error = True
                return_vals = response.text
            else:
                return_vals = loads(response.content)

        except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL) as exc:
            error = True
            return_vals = exc

        return error, return_vals
