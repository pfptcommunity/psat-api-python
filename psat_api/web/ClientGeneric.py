"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from typing import Generic, TypeVar, Type

from psat_api.Region import Region
from psat_api.Version import Version
from psat_api.web.ClientBase import ClientBase

TReport = TypeVar("TReport")


class ClientGeneric(Generic[TReport], ClientBase):
    __reports: TReport

    def __init__(self, cls: Type[TReport], version: Version, region: Region, api_token: str, raise_for_status: bool = False):
        super().__init__(region, version, api_token, raise_for_status)
        self.__reports = cls(self, "api/reporting/{}/".format(version.value))

    @property
    def reports(self) -> TReport:
        return self.__reports


