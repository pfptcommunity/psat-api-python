"""
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from datetime import datetime
from typing import List

from psat_api.common.enrollment_status import EnrollmentStatus
from psat_api.web import FilterOptions, TFilterOptions


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
    __DELETED_USERS = 'filter[_includedeletedusers]'
    __REMOVED_ENROLLMENTS = 'filter[_includeremovedenrollments]'
    __ENROLLMENT_REMOVE_REASON = 'filter[_enrollmentremovalreason]'

    def __init__(self):
        super().__init__()

    @property
    def created_date_start(self) -> datetime:
        return self._options.get(self.__CREATED_START)

    @created_date_start.setter
    def created_date_start(self, start_date: datetime):
        self._options[self.__CREATED_START] = start_date

    def set_created_date_start(self, start_date: datetime) -> TFilterOptions:
        self.created_date_start = start_date
        return self

    @property
    def created_date_end(self) -> datetime:
        return self._options.get(self.__CREATED_END)

    @created_date_end.setter
    def created_date_end(self, end_date: datetime):
        self._options[self.__CREATED_END] = end_date

    def set_created_date_end(self, end_date: datetime) -> TFilterOptions:
        self.created_date_end = end_date
        return self

    @property
    def assignment_names(self) -> List[str]:
        return self._options.get(self.__ASSIGNMENT_NAMES)

    @assignment_names.setter
    def assignment_names(self, names: List[str]):
        self._options[self.__ASSIGNMENT_NAMES] = names

    def set_assignment_names(self, names: List[str]) -> TFilterOptions:
        self.assignment_names = names
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
    def stats(self) -> List[EnrollmentStatus]:
        return self._options.get(self.__STATUS)

    @stats.setter
    def stats(self, stats: List[EnrollmentStatus]):
        self._options[self.__STATUS] = stats

    def set_stats(self, stats: List[EnrollmentStatus]) -> TFilterOptions:
        self.stats = stats
        return self

    @property
    def first_names(self) -> List[str]:
        return self._options.get(self.__USER_FIRST_NAMES)

    @first_names.setter
    def first_names(self, first_names: List[str]):
        self._options[self.__USER_FIRST_NAMES] = first_names

    def set_first_names(self, first_names: List[str]) -> TFilterOptions:
        self.first_names = first_names
        return self

    @property
    def last_names(self) -> List[str]:
        return self._options.get(self.__USER_LAST_NAMES)

    @last_names.setter
    def last_names(self, last_names: List[str]):
        self._options[self.__USER_LAST_NAMES] = last_names

    def set_last_names(self, last_names: List[str]) -> TFilterOptions:
        self.last_names = last_names
        return self

    @property
    def manager_email_addresses(self) -> List[str]:
        return self._options.get(self.__MANAGER_EMAILS)

    @manager_email_addresses.setter
    def manager_email_addresses(self, emails: List[str]):
        self._options[self.__MANAGER_EMAILS] = emails

    def set_manager_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.manager_email_addresses = emails
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
    def include_deleted_users(self) -> bool:
        return self._options.get(self.__DELETED_USERS)

    @include_deleted_users.setter
    def include_deleted_users(self, enable: bool):
        self._options[self.__DELETED_USERS] = enable

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.include_deleted_users = enable
        return self

    @property
    def include_removed_enrollments(self) -> bool:
        return self._options.get(self.__REMOVED_ENROLLMENTS)

    @include_removed_enrollments.setter
    def include_removed_enrollments(self, enable: bool):
        self._options[self.__REMOVED_ENROLLMENTS] = enable

    def set_include_removed_enrollments(self, enable: bool) -> TFilterOptions:
        self.include_removed_enrollments = enable
        return self

    @property
    def enrollment_remove_reason(self) -> str:
        return self._options.get(self.__ENROLLMENT_REMOVE_REASON)

    @enrollment_remove_reason.setter
    def enrollment_remove_reason(self, reason: str):
        self._options[self.__ENROLLMENT_REMOVE_REASON] = reason

    def set_enrollment_remove_reason(self, reason: str) -> TFilterOptions:
        self.enrollment_remove_reason = reason
        return self
