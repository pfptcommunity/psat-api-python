"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.1
License: MIT
"""
from psat_api.Region import Region
from psat_api.Version import Version
from psat_api.v2.reports.Reports import Reports
from psat_api.web.ClientBase import ClientBase

class Client(ClientBase):
    __reports: Reports

    def __init__(self, region: Region, api_token: str, raise_for_status: bool = False):
        super().__init__(region, Version.V2, api_token, raise_for_status)
        self.__reports = Reports(self, "api/reporting/{}/".format(Version.V2.value))

    @property
    def reports(self):
        return self.__reports
