"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from datetime import datetime
from typing import List
from psat_api.web import FilterOptions, TFilterOptions

class PhishingFilter(FilterOptions):
    __EVENT_START = 'filter[_eventtimestamp_start]'
    __EVENT_END = 'filter[_eventtimestamp_end]'
    __CAMPAIGN_NAMES = 'filter[_campaignname]'
    __CAMPAIGN_START = 'filter[_campaignstartdate_start]'
    __CAMPAIGN_END = 'filter[_campaignstartdate_end]'
    __NO_ACTION = 'filter[_includenoaction]'
    __USER_EMAILS = 'filter[_useremailaddress]'
    __DELETED_USERS = 'filter[_includedeletedusers]'
    __INCLUDE_ARCHIVED = 'filter[_includearchivedcampaigns]'
    __FILTER_USER_TAG = 'filter[user_tag][{}]'
    __USER_TAG = 'user_tag_enable'

    def __init__(self):
        super().__init__()

    def set_event_start_date(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__EVENT_START] = start_date
        return self

    def get_event_start_date(self) -> datetime:
        return self._options[self.__EVENT_START]

    def set_event_end_date(self, end_date: datetime) -> TFilterOptions:
        self._options[self.__EVENT_END] = end_date
        return self

    def get_event_end_date(self) -> datetime:
        return self._options[self.__EVENT_END]

    def set_campaign_names(self, names: List[str]) -> TFilterOptions:
        self._options[self.__CAMPAIGN_NAMES] = names
        return self

    def get_campaign_names(self) -> List[str]:
        return self._options[self.__CAMPAIGN_NAMES]

    def set_campaign_start_date(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__CAMPAIGN_START] = start_date
        return self

    def get_campaign_start_date(self) -> datetime:
        return self._options[self.__CAMPAIGN_START]

    def set_campaign_end_date(self, end_date: datetime) -> TFilterOptions:
        self._options[self.__CAMPAIGN_END] = end_date
        return self

    def get_campaign_end_date(self) -> datetime:
        return self._options[self.__CAMPAIGN_END]

    def set_include_no_action(self, enable: bool) -> TFilterOptions:
        self._options[self.__NO_ACTION] = enable
        return self

    def get_include_no_action(self) -> bool:
        return self._options[self.__NO_ACTION]

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self._options[self.__USER_EMAILS] = emails
        return self

    def get_get_email_addresses(self) -> List[str]:
        return self._options[self.__USER_EMAILS]

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self._options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self._options[self.__DELETED_USERS]

    def set_include_archived_campaigns(self, enable: bool) -> TFilterOptions:
        self._options[self.__INCLUDE_ARCHIVED] = enable
        return self

    def get_include_archived_campaigns(self) -> bool:
        return self._options[self.__INCLUDE_ARCHIVED]

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