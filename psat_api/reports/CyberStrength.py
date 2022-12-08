from psat_api.web.Resource import Resource
from urllib.parse import urljoin
from datetime import datetime
from typing import List
from typing import TypeVar

TFilterOptions = TypeVar('TFilterOptions', bound="FilterOptions")

class FilterOptions:
    __options: dict[str]

    def __init__(self):
        self.__options = {}

    def set_page_number(self, page_number: int) -> TFilterOptions:
        self.__options['page[number]'] = page_number
        return self

    def get_page_number(self) -> int:
        return self.__options['page[number]']

    def set_page_size(self, page_size: int) -> TFilterOptions:
        self.__options['page[size]'] = page_size
        return self

    def get_page_size(self) -> int:
        return self.__options['page[size]']

    def add_assignment_name(self, name: str) -> TFilterOptions:
        if self.__options.get('filter[_assignmentname]') is None:
            self.__options['filter[_assignmentname]'] = list()
        self.__options['filter[_assignmentname]'].append(name)
        return self

    def get_assignment_name(self) -> List[str]:
        return self.__options['filter[_assignmentname]']

    def set_assignment_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options['filter[_assignmentstartdate_start]'] = start_date
        return self

    def get_assignment_start_date(self) -> datetime:
        return self.__options['filter[_assignmentstartdate_start]']

    def set_assignment_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options['filter[_assignmentstartdate_end]'] = end_date
        return self

    def get_assignment_end_date(self) -> datetime:
        return self.__options['filter[_assignmentstartdate_end]']

    def set_question_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options['filter[_questiondate_start]'] = start_date
        return self

    def get_question_start_date(self) -> datetime:
        return self.__options['filter[_questiondate_start]']

    def set_question_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options['filter[_questiondate_end]'] = end_date
        return self

    def get_question_end_date(self) -> datetime:
        return self.__options['filter[_questiondate_end]']

    def set_include_not_started(self, enable: bool) -> TFilterOptions:
        self.__options['filter[_includenotstarted]'] = enable
        return self

    def get_include_not_started(self) -> bool:
        return self.__options['filter[_includenotstarted]']

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.__options['filter[_includedeletedusers]'] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self.__options['filter[_includedeletedusers]']

    def set_include_deleted_assignments(self, enable: bool) -> TFilterOptions:
        self.__options['filter[_includedeletedassignments]'] = enable
        return self

    def get_include_deleted_assignments(self, enable: bool) -> bool:
        return self.__options['filter[_includedeletedassignments]']

    def set_full_question(self, enable: bool) -> TFilterOptions:
        self.__options['filter[_fullquestion]'] = enable
        return self

    def get_full_question(self) -> bool:
        return self.__options['filter[_fullquestion]']

    def add_assessment_type(self, name: str) -> TFilterOptions:
        if self.__options.get('filter[_assessmenttype]') is None:
            self.__options['filter[_assessmenttype]'] = list()
        self.__options['filter[_assessmenttype]'].append(name)
        return self

    def get_assessment_type(self) -> List[str]:
        return self.__options['filter[_assessmenttype]']

    def add_user_mail_address(self, email: str) -> TFilterOptions:
        if self.__options.get('filter[_useremailaddress]') is None:
            print("Make List")
            self.__options['filter[_useremailaddress]'] = list()
        self.__options['filter[_useremailaddress]'].append(email)
        return self

    def get_get_mail_address(self) -> List[str]:
        return self.__options['filter[_useremailaddress]']

    def set_filter_user_tag(self, tag: str, value: str) -> TFilterOptions:
        self.__options['filter[user_tag][{}]'.format(tag)] = "'{}'".format(value)
        return self

    def get_filter_user_tag(self, tag: str) -> str:
        return self.__options['filter[user_tag][{}]'.format(tag)]

    def set_user_tag_enabled(self, enabled: bool) -> TFilterOptions:
        self.__options['user_tag_enable'] = enabled
        return self

    def get_user_tag_enabled(self):
        return self.__options['user_tag_enable']

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


class CyberStrength(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def query(self, options: FilterOptions):
        new_results = True
        uri = self.uri
        while new_results:
            response = self.session.get(uri, params=str(options))
            results = response.json()
            yield results['data']
            if 'next' not in results['links']:
                break
            uri = urljoin(uri, results['links']['next'])