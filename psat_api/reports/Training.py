from psat_api.web.CollectionPage import CollectionPage
from psat_api.web.Resource import Resource
from urllib.parse import urljoin
from datetime import datetime
from typing import List, Optional
from typing import TypeVar
from enum import Enum


class AssignmentStatus(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'


TFilterOptions = TypeVar('TFilterOptions', bound="FilterOptions")


class FilterOptions:
    __PAGE_NUMBER = 'page[number]'
    __PAGE_SIZE = 'page[size]'
    __ATTEMPT_START = 'filter[_attemptdate_start]'
    __ATTEMPT_END = 'filter[_attemptdate_end]'
    __ASSIGNMENT_NAMES = 'filter[_assignmentname]'
    __ASSIGNMENT_START = 'filter[_assignmentstartdate_start]'
    __ASSIGNMENT_END = 'filter[_assignmentstartdate_end]'
    __ASSIGNMENT_DUE_START = 'filter[_assignmentduedate_start]'
    __ASSIGNMENT_DUE_END = 'filter[_assignmentduedate_end]'
    __NOT_STARTED = 'filter[_includenotstarted]'
    __USER_EMAILS = 'filter[_useremailaddress]'
    __DELETED_USERS = 'filter[_includedeletedusers]'
    __DELETED_ASSIGNMENTS = 'filter[_includedeletedassignments]'
    __REMOVED_USERS = 'filter[_includeremovedusers]'
    __ASSIGNMENT_STATUS = 'filter[_userassignmentstatus]'
    __FREEPLAY = 'filter[_includefreeplay]'
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

    def set_report_date_start(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__ATTEMPT_START] = start_date
        return self

    def get_report_date_start(self) -> datetime:
        return self.__options[self.__ATTEMPT_START]

    def set_report_date_end(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__ATTEMPT_END] = end_date
        return self

    def get_report_date_end(self) -> datetime:
        return self.__options[self.__ATTEMPT_END]

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

    def set_assignment_due_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_DUE_START] = start_date
        return self

    def get_assignment_due_start_date(self) -> datetime:
        return self.__options[self.__ASSIGNMENT_DUE_START]

    def set_assignment_due_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_DUE_END] = end_date
        return self

    def get_assignment_due_end_date(self) -> datetime:
        return self.__options[self.__ASSIGNMENT_DUE_END]

    def set_include_not_started(self, enable: bool) -> TFilterOptions:
        self.__options[self.__NOT_STARTED] = enable
        return self

    def get_include_not_started(self) -> bool:
        return self.__options[self.__NOT_STARTED]

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

    def set_include_deleted_assignments(self, enable: bool) -> TFilterOptions:
        self.__options[self.__DELETED_ASSIGNMENTS] = enable
        return self

    def get_include_deleted_assignments(self, enable: bool) -> bool:
        return self.__options[self.__DELETED_ASSIGNMENTS]

    def set_include_removed_users(self, enable: bool) -> TFilterOptions:
        self.__options[self.__REMOVED_USERS] = enable
        return self

    def get_include_removed_users(self, enable: bool) -> bool:
        return self.__options[self.__REMOVED_USERS]

    def set_user_tags(self, tag: str, value: str) -> TFilterOptions:
        self.__options[self.__FILTER_USER_TAG.format(tag)] = "'{}'".format(value)
        return self

    def set_user_assignment_stats(self, stats: List[AssignmentStatus]) -> TFilterOptions:
        self.__options[self.__ASSIGNMENT_STATUS] = stats
        return self

    def get_user_assignment_stats(self) -> List[AssignmentStatus]:
        return self.__options[self.__ASSIGNMENT_STATUS]

    def get_user_tags(self, tag: str) -> str:
        return self.__options[self.__FILTER_USER_TAG.format(tag)].lstrip().rstrip()

    def set_include_freeplay(self, enable: bool) -> TFilterOptions:
        self.__options[self.__FREEPLAY] = enable
        return self

    def get_include_freeplay(self) -> bool:
        return self.__options[self.__FREEPLAY]

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
                    elif all(isinstance(n, AssignmentStatus) for n in v):
                        param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, ','.join([s.value for s in v]))
            elif type(v) == datetime:
                param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, v.date())
            else:
                param += "{}{}={}".format(('', '&')[len(param) > 0], k, v)
        return param


class Training(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def get(self, options: FilterOptions = FilterOptions()) -> Optional[CollectionPage]:
        r = self.session.get(self.uri, params=str(options))
        r.raise_for_status()
        return CollectionPage(self.session, r)
