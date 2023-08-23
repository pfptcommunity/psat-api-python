"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from psat_api.Region import Region
from psat_api.Version import Version
from psat_api.web.ErrorHandler import ErrorHandler
from psat_api.web.Resource import Resource


class ClientBase(Resource):
    __api_token: str
    __error_handler: ErrorHandler
    __version: Version
    __service: Region

    def __init__(self, region: Region, version: Version, api_token: str, raise_for_status: bool = False):
        super().__init__(None, "https://" + region.value)
        self.__service = region
        self.__version = version
        self.__api_token = api_token
        self._session.headers.update({'x-apikey-token': api_token})
        self.__error_handler = ErrorHandler(raise_for_status)
        self._session.hooks = {"response": self.__error_handler.handler}

    @property
    def token(self):
        return self.__api_token

    @property
    def service(self):
        return self.__service.value

    @property
    def version(self):
        return self.__version.value
