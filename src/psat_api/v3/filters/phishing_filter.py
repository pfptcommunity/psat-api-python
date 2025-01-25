"""
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
    __RECORD_START = 'filter[_dw_record_update_start_dt]'
    __RECORD_END = 'filter[_dw_record_update_end_dt]'

    def __init__(self):
        super().__init__()

    @property
    def event_start_date(self) -> datetime:
        return self._options.get(self.__EVENT_START)

    @event_start_date.setter
    def event_start_date(self, start_date: datetime):
        self._options[self.__EVENT_START] = start_date

    def set_event_start_date(self, start_date: datetime) -> TFilterOptions:
        self.event_start_date = start_date
        return self

    @property
    def event_end_date(self) -> datetime:
        return self._options.get(self.__EVENT_END)

    @event_end_date.setter
    def event_end_date(self, end_date: datetime):
        self._options[self.__EVENT_END] = end_date

    def set_event_end_date(self, end_date: datetime) -> TFilterOptions:
        self.event_end_date = end_date
        return self

    @property
    def campaign_names(self) -> List[str]:
        return self._options.get(self.__CAMPAIGN_NAMES)

    @campaign_names.setter
    def campaign_names(self, names: List[str]):
        self._options[self.__CAMPAIGN_NAMES] = names

    def set_campaign_names(self, names: List[str]) -> TFilterOptions:
        self.campaign_names = names
        return self

    @property
    def campaign_start_date(self) -> datetime:
        return self._options.get(self.__CAMPAIGN_START)

    @campaign_start_date.setter
    def campaign_start_date(self, start_date: datetime):
        self._options[self.__CAMPAIGN_START] = start_date

    def set_campaign_start_date(self, start_date: datetime) -> TFilterOptions:
        self.campaign_start_date = start_date
        return self

    @property
    def campaign_end_date(self) -> datetime:
        return self._options.get(self.__CAMPAIGN_END)

    @campaign_end_date.setter
    def campaign_end_date(self, end_date: datetime):
        self._options[self.__CAMPAIGN_END] = end_date

    def set_campaign_end_date(self, end_date: datetime) -> TFilterOptions:
        self.campaign_end_date = end_date
        return self

    @property
    def include_no_action(self) -> bool:
        return self._options.get(self.__NO_ACTION)

    @include_no_action.setter
    def include_no_action(self, enable: bool):
        self._options[self.__NO_ACTION] = enable

    def set_include_no_action(self, enable: bool) -> TFilterOptions:
        self.include_no_action = enable
        return self

    @property
    def user_email_addresses(self) -> List[str]:
        return self._options.get(self.__USER_EMAILS)

    @user_email_addresses.setter
    def user_email_addresses(self, emails: List[str]):
        self._options[self.__USER_EMAILS] = emails

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.user_email_addresses = emails
        return self

    @property
    def include_deleted_users(self) -> bool:
        return self._options.get(self.__DELETED_USERS)

    @include_deleted_users.setter
    def include_deleted_users(self, enable: bool):
        self._options[self.__DELETED_USERS] = enable

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.include_deleted_users = enable
        return self

    @property
    def include_archived_campaigns(self) -> bool:
        return self._options.get(self.__INCLUDE_ARCHIVED)

    @include_archived_campaigns.setter
    def include_archived_campaigns(self, enable: bool):
        self._options[self.__INCLUDE_ARCHIVED] = enable

    def set_include_archived_campaigns(self, enable: bool) -> TFilterOptions:
        self.include_archived_campaigns = enable
        return self

    def set_user_tags(self, tag: str, value: str) -> TFilterOptions:
        self._options[self.__FILTER_USER_TAG.format(tag)] = "'{}'".format(value)
        return self

    def get_user_tags(self, tag: str) -> str:
        return self._options.get(self.__FILTER_USER_TAG.format(tag)).lstrip().rstrip()

    @property
    def user_tag(self):
        return self._options.get(self.__USER_TAG)

    @user_tag.setter
    def user_tag(self, enabled: bool):
        self._options[self.__USER_TAG] = enabled

    def set_user_tag(self, enabled: bool) -> TFilterOptions:
        self.user_tag = enabled
        return self

    @property
    def record_start_date(self) -> datetime:
        return self._options.get(self.__RECORD_START)

    @record_start_date.setter
    def record_start_date(self, start_date: datetime):
        self._options[self.__RECORD_START] = start_date

    def set_record_start_date(self, start_date: datetime) -> TFilterOptions:
        self.record_start_date = start_date
        return self

    @property
    def record_end_date(self) -> datetime:
        return self._options.get(self.__RECORD_END)

    @record_end_date.setter
    def record_end_date(self, start_date: datetime):
        self._options[self.__RECORD_END] = start_date

    def set_record_end_date(self, start_date: datetime) -> TFilterOptions:
        self.record_end_date = start_date
        return self
