"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.1
License: MIT
"""
from datetime import datetime
from typing import List, Dict
from typing import TypeVar

from requests import PreparedRequest

from psat_api.web.PageIterator import PageIterator
from psat_api.web.Resource import Resource

TFilterOptions = TypeVar('TFilterOptions', bound="FilterOptions")


class FilterOptions:
    __PAGE_NUMBER = 'page[number]'
    __PAGE_SIZE = 'page[size]'
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

    def set_report_date_start(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__REPORT_START] = start_date
        return self

    def get_report_date_start(self) -> datetime:
        return self.__options[self.__REPORT_START]

    def set_report_date_end(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__REPORT_END] = end_date
        return self

    def get_report_date_end(self) -> datetime:
        return self.__options[self.__REPORT_END]

    def set_received_date_start(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__RECEIVED_START] = start_date
        return self

    def get_received_date_start(self) -> datetime:
        return self.__options[self.__RECEIVED_START]

    def set_received_date_end(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__RECEIVED_END] = end_date
        return self

    def get_received_date_end(self) -> datetime:
        return self.__options[self.__RECEIVED_END]

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.__options[self.__USER_EMAILS] = emails
        return self

    def get_user_email_addresses(self) -> List[str]:
        return self.__options[self.__USER_EMAILS]

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.__options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self.__options[self.__DELETED_USERS]

    def set_actions(self, actions: List[str]) -> TFilterOptions:
        self.__options[self.__ACTIONS] = actions
        return self

    def get_actions(self) -> List[str]:
        return self.__options[self.__ACTIONS]

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

    def set_include_platform_notifications(self, enable: bool) -> TFilterOptions:
        self.__options[self.__PLATFORM_NOTIFICATIONS] = enable
        return self

    def get_include_platform_notifications(self) -> bool:
        return self.__options[self.__PLATFORM_NOTIFICATIONS]

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

    @property
    def params(self) -> Dict:
        param = {}
        for k, v in self.__options.items():
            if type(v) == list:
                if len(v):
                    if all(isinstance(n, str) for n in v):
                        param[k] = "[{}]".format(','.join(v))
            elif type(v) == datetime:
                param[k] = "[{}]".format(v.date())
            else:
                param[k] = v
        return param

    @property
    def params(self) -> Dict:
        param = {}
        for k, v in self.__options.items():
            if type(v) == list:
                if len(v):
                    if all(isinstance(n, str) for n in v):
                        param[k] = "[{}]".format(','.join(v))
            elif type(v) == datetime:
                param[k] = "[{}]".format(v.date())
            else:
                param[k] = v
        return param


class PhishAlarm(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: FilterOptions = FilterOptions()) -> PageIterator:
        request = PreparedRequest()
        request.prepare_url(self.uri, options.params)
        request.method = 'get'
        return PageIterator(self._session, request)
