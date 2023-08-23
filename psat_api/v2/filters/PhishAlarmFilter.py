"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from datetime import datetime
from psat_api.v1.filters.PhishAlarmFilter import PhishAlarmFilter as PhishAlarmFilterV1
from psat_api.web.FilterOptions import TFilterOptions

class PhishAlarmFilter(PhishAlarmFilterV1):
    __RECORD_START = 'filter[_dw_record_update_start_dt]'
    __RECORD_END = 'filter[_dw_record_update_end_dt]'
    __INCLUDE_DELETED_CAMPAIGNS = 'filter[_includedeletedcampaigns]'
    def __init__(self):
        super().__init__()

    def set_record_start_date(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__RECORD_START] = start_date
        return self

    def get_record_start_date(self) -> datetime:
        return self._options[self.__RECORD_START]

    def set_record_end_date(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__RECORD_END] = start_date
        return self

    def get_record_end_date(self) -> datetime:
        return self._options[self.__RECORD_END]

    def set_include_deleted_campaigns(self, enabled: bool) -> TFilterOptions:
        self._options[self.__INCLUDE_DELETED_CAMPAIGNS] = enabled
        return self

    def get_include_deleted_campaigns(self):
        return self._options[self.__INCLUDE_DELETED_CAMPAIGNS]
