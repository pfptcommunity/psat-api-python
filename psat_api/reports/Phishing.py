"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.0
License: MIT
"""
from psat_api.web.CollectionPage import CollectionPage
from psat_api.web.Resource import Resource
from urllib.parse import urljoin
from datetime import datetime
from typing import List, Optional
from typing import TypeVar

TFilterOptions = TypeVar('TFilterOptions', bound="FilterOptions")


class FilterOptions:
    __PAGE_NUMBER = 'page[number]'
    __PAGE_SIZE = 'page[size]'
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
    __options: dict[str]

    def __init__(self):
        self.__options = {}

    def clear(self):
        self.__options.clear()

    def set_page_number(self, page_number: int) -> TFilterOptions:
        self.__options[self.__PAGE_NUMBER] = page_number
        return self

    def get_page_number(self) -> int:
        return self.__options[self.__PAGE_NUMBER]

    def set_page_size(self, page_size: int) -> TFilterOptions:
        self.__options[self.__PAGE_SIZE] = page_size
        return self

    def get_page_size(self) -> int:
        return self.__options[self.__PAGE_SIZE]

    def set_event_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__EVENT_START] = start_date
        return self

    def get_event_start_date(self) -> datetime:
        return self.__options[self.__EVENT_START]

    def set_event_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__EVENT_END] = end_date
        return self

    def get_event_end_date(self) -> datetime:
        return self.__options[self.__EVENT_END]

    def set_campaign_names(self, names: List[str]) -> TFilterOptions:
        self.__options[self.__CAMPAIGN_NAMES] = names
        return self

    def get_campaign_names(self) -> List[str]:
        return self.__options[self.__CAMPAIGN_NAMES]

    def set_campaign_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__CAMPAIGN_START] = start_date
        return self

    def get_campaign_start_date(self) -> datetime:
        return self.__options[self.__CAMPAIGN_START]

    def set_campaign_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__CAMPAIGN_END] = end_date
        return self

    def get_campaign_end_date(self) -> datetime:
        return self.__options[self.__CAMPAIGN_END]

    def set_include_no_action(self, enable: bool) -> TFilterOptions:
        self.__options[self.__NO_ACTION] = enable
        return self

    def get_include_no_action(self) -> bool:
        return self.__options[self.__NO_ACTION]

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.__options[self.__USER_EMAILS] = emails
        return self

    def get_get_email_addresses(self) -> List[str]:
        return self.__options[self.__USER_EMAILS]

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.__options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self.__options[self.__DELETED_USERS]

    def set_include_archived_campaigns(self, enable: bool) -> TFilterOptions:
        self.__options[self.__INCLUDE_ARCHIVED] = enable
        return self

    def get_include_archived_campaigns(self, enable: bool) -> bool:
        return self.__options[self.__INCLUDE_ARCHIVED]

    def set_user_tags(self, tag: str, value: str) -> TFilterOptions:
        self.__options[self.__FILTER_USER_TAG.format(tag)] = "'{}'".format(value)
        return self

    def get_user_tags(self, tag: str) -> str:
        return self.__options[self.__FILTER_USER_TAG.format(tag)].lstrip().rstrip()

    def set_user_tag(self, enabled: bool) -> TFilterOptions:
        self.__options[self.__USER_TAG] = enabled
        return self

    def get_user_tag(self):
        return self.__options[self.__USER_TAG]

    def __str__(self) -> str:
        param = ''
        for k, v in self.__options.items():
            if type(v) == list:
                if len(v):
                    if all(isinstance(n, str) for n in v):
                        param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, ','.join(v))
            elif type(v) == datetime:
                param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, v.date())
            else:
                param += "{}{}={}".format(('', '&')[len(param) > 0], k, v)
        return param


class Phishing(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def get(self, options: FilterOptions = FilterOptions()) -> Optional[CollectionPage]:
        r = self.session.get(self.uri, params=str(options))
        r.raise_for_status()
        return CollectionPage(self.session, r)
