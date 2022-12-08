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

    def set_event_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options['filter[_eventtimestamp_start]'] = start_date
        return self

    def get_event_start_date(self) -> datetime:
        return self.__options['filter[_eventtimestamp_start]']

    def set_event_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options['filter[_eventtimestamp_end]'] = end_date
        return self

    def get_event_end_date(self) -> datetime:
        return self.__options['filter[_eventtimestamp_end]']

    def add_campaign_name(self, name: str) -> TFilterOptions:
        if self.__options.get('filter[_campaignname]') is None:
            self.__options['filter[_campaignname]'] = list()
        self.__options['filter[_campaignname]'].append(name)
        return self

    def get_campaign_name(self) -> List[str]:
        return self.__options['filter[_campaignname]']

    def set_campaign_start_date(self, start_date: datetime) -> TFilterOptions:
        self.__options['filter[_campaignstartdate_start]'] = start_date
        return self

    def get_campaign_start_date(self) -> datetime:
        return self.__options['filter[_campaignstartdate_start]']

    def set_campaign_end_date(self, end_date: datetime) -> TFilterOptions:
        self.__options['filter[_campaignstartdate_end]'] = end_date
        return self

    def get_campaign_end_date(self) -> datetime:
        return self.__options['filter[_campaignstartdate_end]']

    def set_include_no_action(self, enable: bool) -> TFilterOptions:
        self.__options['filter[_includenoaction]'] = enable
        return self

    def get_include_no_action(self) -> bool:
        return self.__options['filter[_includenoaction]']

    def add_user_mail_address(self, email: str) -> TFilterOptions:
        if self.__options.get('filter[_useremailaddress]') is None:
            print("Make List")
            self.__options['filter[_useremailaddress]'] = list()
        self.__options['filter[_useremailaddress]'].append(email)
        return self

    def get_get_mail_address(self) -> List[str]:
        return self.__options['filter[_useremailaddress]']

    def set_include_deleted_users(self, enable: bool) -> TFilterOptions:
        self.__options['filter[_includedeletedusers]'] = enable
        return self

    def get_include_deleted_users(self) -> bool:
        return self.__options['filter[_includedeletedusers]']

    def set_include_archived_campaigns(self, enable: bool) -> TFilterOptions:
        self.__options['filter[_includearchivedcampaigns]'] = enable
        return self

    def get_include_archived_campaigns(self, enable: bool) -> bool:
        return self.__options['filter[_includearchivedcampaigns]']

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


class Phishing(Resource):
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