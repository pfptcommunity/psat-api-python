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
    __RECORD_START = 'filter[_dw_record_update_start_dt]'
    __RECORD_END = 'filter[_dw_record_update_end_dt]'
    __INCLUDE_DELETED_CAMPAIGNS = 'filter[_includedeletedcampaigns]'

    def __init__(self):
        super().__init__()

    @property
    def report_date_start(self) -> datetime:
        return self._options[self.__REPORT_START]

    @report_date_start.setter
    def report_date_start(self, start_date: datetime):
        self._options[self.__REPORT_START] = start_date

    def set_report_date_start(self, start_date: datetime) -> TFilterOptions:
        self.report_date_start = start_date
        return self

    @property
    def report_date_end(self) -> datetime:
        return self._options[self.__REPORT_END]

    @report_date_end.setter
    def report_date_end(self, end_date: datetime):
        self._options[self.__REPORT_END] = end_date

    def set_report_date_end(self, end_date: datetime) -> TFilterOptions:
        self.report_date_end = end_date
        return self

    @property
    def received_date_start(self) -> datetime:
        return self._options[self.__RECEIVED_START]

    @received_date_start.setter
    def received_date_start(self, start_date: datetime):
        self._options[self.__RECEIVED_START] = start_date

    def set_received_date_start(self, start_date: datetime) -> TFilterOptions:
        self.received_date_start = start_date
        return self

    @property
    def received_date_end(self) -> datetime:
        return self._options[self.__RECEIVED_END]

    @received_date_end.setter
    def received_date_end(self, end_date: datetime):
        self._options[self.__RECEIVED_END] = end_date

    def set_received_date_end(self, end_date: datetime) -> TFilterOptions:
        self.received_date_end = end_date
        return self

    @property
    def user_email_addresses(self) -> List[str]:
        return self._options[self.__USER_EMAILS]

    @user_email_addresses.setter
    def user_email_addresses(self, emails: List[str]):
        self._options[self.__USER_EMAILS] = emails

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.user_email_addresses = emails
        return self

    @property
    def include_deleted_users(self) -> bool:
        return self._options[self.__DELETED_USERS]

    @include_deleted_users.setter
    def include_deleted_users(self, enable: bool):
        self._options[self.__DELETED_USERS] = enable

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.include_deleted_users = enable
        return self

    @property
    def actions(self) -> List[str]:
        return self._options[self.__ACTIONS]

    @actions.setter
    def actions(self, actions: List[str]):
        self._options[self.__ACTIONS] = actions

    def set_actions(self, actions: List[str]) -> TFilterOptions:
        self.actions = actions
        return self

    def set_user_tags(self, tag: str, value: str) -> TFilterOptions:
        self._options[self.__FILTER_USER_TAG.format(tag)] = "'{}'".format(value)
        return self

    def get_user_tags(self, tag: str) -> str:
        return self._options[self.__FILTER_USER_TAG.format(tag)].lstrip().rstrip()

    @property
    def user_tag(self):
        return self._options[self.__USER_TAG]

    @user_tag.setter
    def user_tag(self, enabled: bool):
        self._options[self.__USER_TAG] = enabled

    def set_user_tag(self, enabled: bool) -> TFilterOptions:
        self.user_tag = enabled
        return self

    @property
    def include_platform_notifications(self) -> bool:
        return self._options[self.__PLATFORM_NOTIFICATIONS]

    @include_platform_notifications.setter
    def include_platform_notifications(self, enable: bool):
        self._options[self.__PLATFORM_NOTIFICATIONS] = enable

    def set_include_platform_notifications(self, enable: bool) -> TFilterOptions:
        self.include_platform_notifications = enable
        return self

    @property
    def record_start_date(self) -> datetime:
        return self._options[self.__RECORD_START]

    @record_start_date.setter
    def record_start_date(self, start_date: datetime):
        self._options[self.__RECORD_START] = start_date

    def set_record_start_date(self, start_date: datetime) -> TFilterOptions:
        self.record_start_date = start_date
        return self

    @property
    def record_end_date(self) -> datetime:
        return self._options[self.__RECORD_END]

    @record_end_date.setter
    def record_end_date(self, end_date: datetime):
        self._options[self.__RECORD_END] = end_date

    def set_record_end_date(self, end_date: datetime) -> TFilterOptions:
        self.record_start_date = end_date
        return self

    @property
    def include_deleted_campaigns(self):
        return self._options[self.__INCLUDE_DELETED_CAMPAIGNS]

    @include_deleted_campaigns.setter
    def include_deleted_campaigns(self, enabled: bool):
        self._options[self.__INCLUDE_DELETED_CAMPAIGNS] = enabled

    def set_include_deleted_campaigns(self, enabled: bool) -> TFilterOptions:
        self.include_deleted_campaigns = enabled
        return self
