"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.1
License: MIT
"""
from requests import Response
from psat_api import Version
from psat_api import Region
from psat_api.reports.Reports import Reports
from psat_api.web.Resource import Resource


class Client(Resource):
    __api_token: str
    __version: Version
    __service: Region
    __reports: Reports
    __raise_for_status: bool
    def __session_hook(self, response: Response, **kwargs) -> Response:
        if response.status_code == 401:
            response.reason = "Authorization Error, Missing Authorization Header, or Expired Token"
        elif response.status_code == 402:
            response.reason = "API Budget Empty"
        elif response.status_code == 403:
            response.reason = "User is not authorized to access this resource with an explicit deny"
        elif response.status_code == 422:
            response.reason = "Invalid Token, Token Decode Error, Invalid Header"
        elif response.status_code == 500:
            response.reason = "Database Error, Internal Server Error"

        if self.__raise_for_status:
            response.raise_for_status()

        return response

    def __init__(self, region: Region, version: Version, api_token: str,  raise_for_status: bool = False):
        super().__init__(None, "https://" + region.value)
        self.__version = version
        self.__service = region
        self.__api_token = api_token
        self.__raise_for_status = raise_for_status
        self.__reports = Reports(self, "api/reporting/v{}/".format(version.value))
        self.session.headers.update({'x-apikey-token': api_token})
        self.session.hooks = {"response": self.__session_hook}
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
