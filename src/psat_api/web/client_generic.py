"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from typing import Generic, TypeVar, Type

from psat_api.common import Region
from psat_api.common import Version
from .ClientBase import ClientBase

TReport = TypeVar("TReport")


class ClientGeneric(Generic[TReport], ClientBase):
    __reports: TReport

    def __init__(self, cls: Type[TReport], version: Version, region: Region, api_token: str):
        super().__init__(region, version, api_token)
        self.__reports = cls(self, "api/reporting/{}/".format(version.value))

    @property
    def reports(self) -> TReport:
        return self.__reports
