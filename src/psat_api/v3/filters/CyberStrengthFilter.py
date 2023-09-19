"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from datetime import datetime
from typing import List

from psat_api.web import FilterOptions, TFilterOptions


class CyberStrengthFilter(FilterOptions):
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
    __RECORD_START = 'filter[_dw_record_update_start_dt]'
    __RECORD_END = 'filter[_dw_record_update_end_dt]'

    def __init__(self):
        super().__init__()

    @property
    def assignment_names(self) -> List[str]:
        return self._options[self.__ASSIGNMENT_NAMES]

    @assignment_names.setter
    def assignment_names(self, names: List[str]):
        self._options[self.__ASSIGNMENT_NAMES] = names

    def set_assignment_names(self, names: List[str]) -> TFilterOptions:
        self.assignment_names = names
        return self

    @property
    def assignment_start_date(self) -> datetime:
        return self._options[self.__ASSIGNMENT_START]

    @assignment_start_date.setter
    def assignment_start_date(self, start_date: datetime):
        self._options[self.__ASSIGNMENT_START] = start_date

    def set_assignment_start_date(self, start_date: datetime) -> TFilterOptions:
        self.assignment_start_date = start_date
        return self

    @property
    def assignment_end_date(self) -> datetime:
        return self._options[self.__ASSIGNMENT_END]

    @assignment_end_date.setter
    def assignment_end_date(self, end_date: datetime):
        self._options[self.__ASSIGNMENT_END] = end_date

    def set_assignment_end_date(self, end_date: datetime) -> TFilterOptions:
        self.assignment_end_date = end_date
        return self

    @property
    def question_start_date(self) -> datetime:
        return self._options[self.__QUESTION_START]

    @question_start_date.setter
    def question_start_date(self, start_date: datetime):
        self._options[self.__QUESTION_START] = start_date

    def set_question_start_date(self, start_date: datetime) -> TFilterOptions:
        self.question_start_date = start_date
        return self

    @property
    def question_end_date(self) -> datetime:
        return self._options[self.__QUESTION_END]

    @question_end_date.setter
    def question_end_date(self, end_date: datetime):
        self._options[self.__QUESTION_END] = end_date

    def set_question_end_date(self, end_date: datetime) -> TFilterOptions:
        self.question_end_date = end_date
        return self

    @property
    def include_not_started(self) -> bool:
        return self._options[self.__NOT_STARTED]

    @include_not_started.setter
    def include_not_started(self, enable: bool):
        self._options[self.__NOT_STARTED] = enable

    def set_include_not_started(self, enable: bool) -> TFilterOptions:
        self.include_not_started = enable
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
    def include_deleted_assignments(self) -> bool:
        return self._options[self.__DELETED_ASSIGNMENTS]

    @include_deleted_assignments.setter
    def include_deleted_assignments(self, enable: bool):
        self._options[self.__DELETED_ASSIGNMENTS] = enable

    def set_include_deleted_assignments(self, enable: bool) -> TFilterOptions:
        self.include_deleted_assignments = enable
        return self

    @property
    def full_question(self) -> bool:
        return self._options[self.__FULL_QUESTION]

    @full_question.setter
    def full_question(self, enable: bool):
        self._options[self.__FULL_QUESTION] = enable

    def set_full_question(self, enable: bool) -> TFilterOptions:
        self.full_question = enable
        return self

    @property
    def assessment_types(self) -> List[str]:
        return self._options[self.__ASSIGNMENT_TYPES]

    @assessment_types.setter
    def assessment_types(self, types: List[str]):
        self._options[self.__ASSIGNMENT_TYPES] = types

    def set_assessment_types(self, types: List[str]) -> TFilterOptions:
        self.assessment_types = types
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
    def record_end_date(self, start_date: datetime):
        self._options[self.__RECORD_END] = start_date

    def set_record_end_date(self, start_date: datetime) -> TFilterOptions:
        self.record_end_date = start_date
        return self
