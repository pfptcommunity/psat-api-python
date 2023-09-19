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

    @property
    def user_email_addresses(self) -> List[str]:
        return self._options[self.__USER_EMAILS]

    @user_email_addresses.setter
    def user_email_addresses(self, emails: List[str]):
        self._options[self.__USER_EMAILS] = emails

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.user_email_addresses = emails
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
