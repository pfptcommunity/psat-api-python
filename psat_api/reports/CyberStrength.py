"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.1
License: MIT
"""
import urllib.parse
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
    __ASSIGNMENT_NAMES = 'filter[_assignmentname]'
    __ASSIGNMENT_START = 'filter[_assignmentstartdate_start]'
    __ASSIGNMENT_END = 'filter[_assignmentstartdate_end]'
    __QUESTION_START = 'filter[_questiondate_start]'
    __QUESTION_END = 'filter[_questiondate_end]'
    __NOT_STARTED = 'filter[_includenotstarted]'
    __DELETED_USERS = 'filter[_includedeletedusers]'
    __DELETED_ASSIGNMENTS = 'filter[_includedeletedassignments]'
    __FULL_QUESTION = 'filter[_fullquestion]'
    __ASSIGNMENT_TYPES = 'filter[_assessmenttype]'
    __USER_EMAILS = 'filter[_useremailaddress]'
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

    def set_assignment_names(self, names: List[str]) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_NAMES] = names
        return self

    def get_assignment_names(self) -> List[str]:
        return self.__options[self.__ASSIGNMENT_NAMES]

    def set_assignment_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_START] = start_date
        return self

    def get_assignment_start_date(self) -> datetime:
        return self.__options[self.__ASSIGNMENT_START]

    def set_assignment_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_END] = end_date
        return self

    def get_assignment_end_date(self) -> datetime:
        return self.__options[self.__ASSIGNMENT_END]

    def set_question_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__QUESTION_START] = start_date
        return self

    def get_question_start_date(self) -> datetime:
        return self.__options[self.__QUESTION_START]

    def set_question_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__QUESTION_END] = end_date
        return self

    def get_question_end_date(self) -> datetime:
        return self.__options[self.__QUESTION_END]

    def set_include_not_started(self, enable: bool) -> TFilterOptions:
        self.__options[self.__NOT_STARTED] = enable
        return self

    def get_include_not_started(self) -> bool:
        return self.__options[self.__NOT_STARTED]

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.__options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self.__options[self.__DELETED_USERS]

    def set_include_deleted_assignments(self, enable: bool) -> TFilterOptions:
        self.__options[self.__DELETED_ASSIGNMENTS] = enable
        return self

    def get_include_deleted_assignments(self, enable: bool) -> bool:
        return self.__options[self.__DELETED_ASSIGNMENTS]

    def set_full_question(self, enable: bool) -> TFilterOptions:
        self.__options[self.__FULL_QUESTION] = enable
        return self

    def get_full_question(self) -> bool:
        return self.__options[self.__FULL_QUESTION]

    def set_assessment_types(self, types: List[str]) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_TYPES] = types
        return self

    def get_assessment_types(self) -> List[str]:
        return self.__options[self.__ASSIGNMENT_TYPES]

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.__options[self.__USER_EMAILS] = emails
        return self

    def get_user_email_addresses(self) -> List[str]:
        return self.__options[self.__USER_EMAILS]

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


class CyberStrength(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: FilterOptions = FilterOptions()):
        request = PreparedRequest()
        request.prepare_url(self.uri, options.params)
        request.method = 'get'
        return PageIterator(self._session, request)
