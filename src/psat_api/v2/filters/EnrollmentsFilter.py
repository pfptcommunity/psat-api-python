"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from psat_api.v1.filters.EnrollmentsFilter import EnrollmentsFilter as EnrollmentsFilterV1
from psat_api.web import TFilterOptions


class EnrollmentsFilter(EnrollmentsFilterV1):
    __DELETED_USERS = 'filter[_includedeletedusers]'
    __REMOVED_ENROLLMENTS = 'filter[_includeremovedenrollments]'
    __ENROLLMENT_REMOVE_REASON = 'filter[_enrollmentremovalreason]'

    def __init__(self):
        super().__init__()

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self._options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self._options[self.__DELETED_USERS]

    def set_include_removed_enrollments(self, enable: bool) -> TFilterOptions:
        self._options[self.__REMOVED_ENROLLMENTS] = enable
        return self

    def get_include_removed_enrollments(self) -> bool:
        return self._options[self.__REMOVED_ENROLLMENTS]

    def set_enrollment_remove_reason(self, reason: str) -> TFilterOptions:
        self._options[self.__ENROLLMENT_REMOVE_REASON] = reason
        return self

    def get_enrollment_remove_reason(self) -> str:
        return self._options[self.__ENROLLMENT_REMOVE_REASON]
