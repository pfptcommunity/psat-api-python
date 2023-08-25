"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-apiLicense: MIT
"""
from typing import List
from psat_api.web import FilterOptions, TFilterOptions

class UsersFilter(FilterOptions):
    __USER_EMAILS = 'filter[_useremailaddress]'
    __DELETED_USERS = 'filter[_includedeletedusers]'
    __FILTER_USER_TAG = 'filter[user_tag][{}]'
    __USER_TAG = 'user_tag_enable'

    def __init__(self):
        super().__init__()

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self._options[self.__USER_EMAILS] = emails
        return self

    def get_user_email_addresses(self) -> List[str]:
        return self._options[self.__USER_EMAILS]

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self._options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self._options[self.__DELETED_USERS]

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
