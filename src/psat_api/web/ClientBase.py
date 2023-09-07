"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from requests.adapters import HTTPAdapter

from psat_api.common import Region
from psat_api.common import Version
from .ErrorHandler import ErrorHandler
from .Resource import Resource


class TimeoutHTTPAdapter(HTTPAdapter):
    timeout = None

    def __init__(self, *args, **kwargs):
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None and hasattr(self, 'timeout'):
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


class ClientBase(Resource):
    __api_token: str
    __error_handler: ErrorHandler
    __version: Version
    __service: Region

    def __init__(self, region: Region, version: Version, api_token: str):
        super().__init__(None, "https://" + region.value)
        self.__service = region
        self.__version = version
        self.__api_token = api_token
        self.session.headers.update({'x-apikey-token': api_token})
        self.__error_handler = ErrorHandler()
        self.session.hooks = {"response": self.__error_handler.handler}

    @property
    def token(self):
        return self.__api_token

    @property
    def service(self):
        return self.__service.value

    @property
    def version(self):
        return self.__version.value

    @property
    def timeout(self):
        return self.session.adapters.get('https://').timeout

    @timeout.setter
    def timeout(self, timeout):
        self.session.adapters.get('https://').timeout = timeout

    @property
    def error_handler(self) -> ErrorHandler:
        return self.__error_handler

    @error_handler.setter
    def error_handler(self, error_handler: ErrorHandler):
        self.__error_handler = error_handler
