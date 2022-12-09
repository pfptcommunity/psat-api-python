from psat_api.web.Resource import Resource
from urllib.parse import urljoin
from datetime import datetime
from typing import List
from typing import TypeVar

TFilterOptions = TypeVar('TFilterOptions', bound="FilterOptions")


class FilterOptions:
    __PAGE_NUMBER = 'page[number]'
    __PAGE_SIZE = 'page[size]'
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

    def set_created_date_start(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__CREATED_START] = start_date
        return self

    def get_created_date_start(self) -> datetime:
        return self.__options[self.__CREATED_START]

    def set_created_date_end(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__CREATED_END] = start_date
        return self

    def get_created_date_end(self) -> datetime:
        return self.__options[self.__CREATED_END]

    def set_assignment_names(self, names: List[str]) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_NAMES] = names
        return self

    def get_assignment_names(self) -> List[str]:
        return self.__options[self.__ASSIGNMENT_NAMES]

    def set_user_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.__options[self.__USER_EMAILS] = emails
        return self

    def get_user_email_addresses(self) -> List[str]:
        return self.__options[self.__USER_EMAILS]

    def set_stats(self, stats: List[str]) -> TFilterOptions:
        self.__options[self.__STATUS] = stats
        return self

    def get_stats(self) -> List[str]:
        return self.__options[self.__STATUS]

    def set_first_names(self, stats: List[str]) -> TFilterOptions:
        self.__options[self.__USER_FIRST_NAMES] = stats
        return self

    def get_first_names(self) -> List[str]:
        return self.__options[self.__USER_FIRST_NAMES]

    def set_last_names(self, names: List[str]) -> TFilterOptions:
        self.__options[self.__USER_LAST_NAMES] = names
        return self

    def get_last_names(self) -> List[str]:
        return self.__options[self.__USER_LAST_NAMES]

    def set_manager_email_addresses(self, emails: List[str]) -> TFilterOptions:
        self.__options[self.__MANAGER_EMAILS] = emails
        return self

    def get_manager_email_addresses(self) -> List[str]:
        return self.__options[self.__MANAGER_EMAILS]

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

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.__options[self.__DELETED_USERS] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self.__options[self.__DELETED_USERS]

    def set_include_removed_enrollments(self, enable: bool) -> TFilterOptions:
        self.__options[self.__REMOVED_ENROLLMENTS] = enable
        return self

    def get_include_removed_enrollments(self) -> bool:
        return self.__options[self.__REMOVED_ENROLLMENTS]

    def set_user_tags(self, reason: str) -> TFilterOptions:
        self.__options[self.__ENROLLMENT_REMOVE_REASON] = reason
        return self

    def get_user_tags(self) -> str:
        return self.__options[self.__ENROLLMENT_REMOVE_REASON]

    def __str__(self) -> str:
        param = ''
        for k, v in self.__options.items():
            if type(v) == list:
                param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, ','.join(v))
            elif type(v) == datetime:
                param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, v.date())
            else:
                param += "{}{}={}".format(('', '&')[len(param) > 0], k, v)
        return param


class Enrollments(Resource):

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def query(self, options: FilterOptions = FilterOptions()):
        print(options)
        new_results = True
        uri = self.uri
        while new_results:
            response = self.session.get(uri, params=str(options))
            results = response.json()
            yield results['data']
            if 'next' not in results['links']:
                break
            uri = urljoin(uri, results['links']['next'])
