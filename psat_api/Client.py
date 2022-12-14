"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.0
License: MIT
"""
from psat_api import Version
from psat_api import Region
from psat_api.reports.Reports import Reports
from psat_api.web.Resource import Resource


class Client(Resource):
    __api_token: str
    __version: Version
    __service: Region
    __reports: Reports

    def __init__(self, region: Region, version: Version, api_token: str):
        super().__init__(None, "https://" + region.value)
        self.__version = version
        self.__service = region
        self.__api_token = api_token
        self.__reports = Reports(self, "api/reporting/v{}/".format(version.value))
        self.session.headers.update({'x-apikey-token': api_token})

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
