"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from datetime import datetime
from typing import List
from psat_api.web import FilterOptions, TFilterOptions

class PhishAlarmFilter(FilterOptions):
    __REPORT_START = 'filter[_reporteddate_start]'
    __REPORT_END = 'filter[_reporteddate_end]'
    __RECEIVED_START = 'filter[_receiveddate_start]'
    __RECEIVED_END = 'filter[_receiveddate_end]'
    __USER_EMAILS = 'filter[_useremailaddress]'
    __DELETED_USERS = 'filter[_includedeletedusers]'
    __ACTIONS = 'filter[_action]'
    __FILTER_USER_TAG = 'filter[user_tag][{}]'
    __USER_TAG = 'user_tag_enable'
    __PLATFORM_NOTIFICATIONS = 'filter[_includeplatformnotifications]'

    def __init__(self):
        super().__init__()

    def set_report_date_start(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__REPORT_START] = start_date
        return self

    def get_report_date_start(self) -> datetime:
        return self._options[self.__REPORT_START]

    def set_report_date_end(self, end_date: datetime) -> TFilterOptions:
        self._options[self.__REPORT_END] = end_date
        return self

    def get_report_date_end(self) -> datetime:
        return self._options[self.__REPORT_END]

    def set_received_date_start(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__RECEIVED_START] = start_date
        return self

    def get_received_date_start(self) -> datetime:
        return self._options[self.__RECEIVED_START]

    def set_received_date_end(self, end_date: datetime) -> TFilterOptions:
        self._options[self.__RECEIVED_END] = end_date
        return self

    def get_received_date_end(self) -> datetime:
        return self._options[self.__RECEIVED_END]

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self._options[self.__USER_EMAILS] = emails
        return self

    def get_user_email_addresses(self) -> List[str]:
        return self._options[self.__USER_EMAILS]

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self._options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self._options[self.__DELETED_USERS]

    def set_actions(self, actions: List[str]) -> TFilterOptions:
        self._options[self.__ACTIONS] = actions
        return self

    def get_actions(self) -> List[str]:
        return self._options[self.__ACTIONS]

    def set_user_tags(self, tag: str, value: str) -> TFilterOptions:
        self._options[self.__FILTER_USER_TAG.format(tag)] = "'{}'".format(value)
        return self

    def get_user_tags(self, tag: str) -> str:
        return self._options[self.__FILTER_USER_TAG.format(tag)].lstrip().rstrip()

    def set_user_tag(self, enabled: bool) -> TFilterOptions:
        self._options[self.__USER_TAG] = enabled
        return self

    def get_user_tag(self):
        return self._options[self.__USER_TAG]

    def set_include_platform_notifications(self, enable: bool) -> TFilterOptions:
        self._options[self.__PLATFORM_NOTIFICATIONS] = enable
        return self

    def get_include_platform_notifications(self) -> bool:
        return self._options[self.__PLATFORM_NOTIFICATIONS]
