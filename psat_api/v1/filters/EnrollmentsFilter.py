"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from datetime import datetime
from typing import List
from enum import Enum
from psat_api.web.FilterOptions import FilterOptions, TFilterOptions

class EnrollmentStatus(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    OVERDUE_IN_PROGRESS = 'Overdue - In Progress'
    OVERDUE_NOT_STARTED = 'Overdue - Not Started'
    COMPLETED = 'Completed'


class EnrollmentsFilter(FilterOptions):
    __CREATED_START = 'filter[_created_start]'
    __CREATED_END = 'filter[_created_end]'
    __ASSIGNMENT_NAMES = 'filter[_assignmentname]'
    __USER_EMAILS = 'filter[_useremailaddress]'
    __STATUS = 'filter[_filter_status]'
    __USER_FIRST_NAMES = 'filter[_userfirstname]'
    __USER_LAST_NAMES = 'filter[_userlastname]'
    __MANAGER_EMAILS = 'filter[_manageremailaddress]'
    __FILTER_USER_TAG = 'filter[user_tag][{}]'
    __USER_TAG = 'user_tag_enable'

    def __init__(self):
        super().__init__()

    def set_created_date_start(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__CREATED_START] = start_date
        return self

    def get_created_date_start(self) -> datetime:
        return self._options[self.__CREATED_START]

    def set_created_date_end(self, start_date: datetime) -> TFilterOptions:
        self._options[self.__CREATED_END] = start_date
        return self

    def get_created_date_end(self) -> datetime:
        return self._options[self.__CREATED_END]

    def set_assignment_names(self, names: List[str]) -> TFilterOptions:
        self._options[self.__ASSIGNMENT_NAMES] = names
        return self

    def get_assignment_names(self) -> List[str]:
        return self._options[self.__ASSIGNMENT_NAMES]

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self._options[self.__USER_EMAILS] = emails
        return self

    def get_user_email_addresses(self) -> List[str]:
        return self._options[self.__USER_EMAILS]

    def set_stats(self, stats: List[EnrollmentStatus]) -> TFilterOptions:
        self._options[self.__STATUS] = stats
        return self

    def get_stats(self) -> List[EnrollmentStatus]:
        return self._options[self.__STATUS]

    def set_first_names(self, first_names: List[str]) -> TFilterOptions:
        self._options[self.__USER_FIRST_NAMES] = first_names
        return self

    def get_first_names(self) -> List[str]:
        return self._options[self.__USER_FIRST_NAMES]

    def set_last_names(self, last_names: List[str]) -> TFilterOptions:
        self._options[self.__USER_LAST_NAMES] = last_names
        return self

    def get_last_names(self) -> List[str]:
        return self._options[self.__USER_LAST_NAMES]

    def set_manager_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self._options[self.__MANAGER_EMAILS] = emails
        return self

    def get_manager_email_addresses(self) -> List[str]:
        return self._options[self.__MANAGER_EMAILS]

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