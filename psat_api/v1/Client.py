"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.1
License: MIT
"""
from psat_api.Region import Region
from psat_api.Version import Version
from psat_api.v1.reports.Reports import Reports
from psat_api.web.ErrorHandler import ErrorHandler
from psat_api.web.Resource import Resource


class Client(Resource):
    __api_token: str
    __error_handler: ErrorHandler
    __version: Version
    __service: Region
    __reports: Reports

    def __init__(self, region: Region, api_token: str, raise_for_status: bool = False):
        super().__init__(None, "https://" + region.value)
        self.__version = Version.V1
        self.__service = region
        self.__api_token = api_token
        self.__error_handler = ErrorHandler(raise_for_status)
        self.__reports = Reports(self, "api/reports/{}/".format(self.__version.value))
        self._session.headers.update({'x-apikey-token': api_token})
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

    @property
    def reports(self):
        return self.__reports
