"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from psat_api.common import Region
from psat_api.common import Version
from psat_api.web import ClientBase
from .reports.Reports import Reports


class Client(ClientBase):
    __reports: Reports

    def __init__(self, region: Region, api_token: str):
        super().__init__(region, Version.V1, api_token)
        self.__reports = Reports(self, "api/reporting/{}/".format(Version.V1.value))

    @property
    def reports(self):
        return self.__reports
