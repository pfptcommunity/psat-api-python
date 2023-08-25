"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from psat_api.common.Region import Region
from psat_api.common.Version import Version
from psat_api.v3.reports.Reports import Reports
from psat_api.web import ClientBase

class Client(ClientBase):
    __reports: Reports

    def __init__(self, region: Region, api_token: str, raise_for_status: bool = False):
        super().__init__(region, Version.V3, api_token, raise_for_status)
        self.__reports = Reports(self, "api/reporting/{}/".format(Version.V3.value))

    @property
    def reports(self):
        return self.__reports