"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from typing import List
from urllib.parse import urljoin
from requests import Response, PreparedRequest
from requests import Session


class PageIterator:
    __response: Response
    __session: Session
    __first_request: bool
    __initial_request: PreparedRequest
    def __init__(self, session: Session, request: PreparedRequest):
        self.__session = session
        self.__initial_request = request
        self.__first_request = True
        self.__response = self.__session.get(self.__initial_request.url)

    def __iter__(self):
        if not self.__first_request:
            self.__first_request = True
            self.__response = self.__session.get(self.__initial_request.url)
        return self

    def __next__(self) -> List:
        if self.__first_request:
            self.__first_request = False
        elif self.get_next() is not None:
            self.__response = self.__session.get(self.get_next())
        else:
            raise StopIteration
        return self.__response.json().get('data', [])

    def get_self(self) -> str:
        url = self.__response.json().get('links', {}).get('self', None)
        return (urljoin(self.__response.url, url), None)[url is None]

    def get_first(self) -> str:
        url = self.__response.json().get('links', {}).get('first', None)
        return (urljoin(self.__response.url, url), None)[url is None]

    def get_last(self) -> str:
        url = self.__response.json().get('links', {}).get('last', None)
        return (urljoin(self.__response.url, url), None)[url is None]

    def get_next(self) -> str:
        url = self.__response.json().get('links', {}).get('next', None)
        return (urljoin(self.__response.url, url), None)[url is None]

    def get_current_page_number(self) -> int:
        return int(self.__response.json().get('meta', {}).get('page_number', 0))

    def get_page_size(self) -> int:
        return int(self.__response.json().get('meta', {}).get('page_size', 0))

    def get_last_page_number(self) -> int:
        if self.get_page_size() == 0:
            return 0
        if self.get_record_count() == 0:
            return 1
        return int((self.get_record_count() + self.get_page_size() - 1) / self.get_page_size())

    def get_record_count(self) -> int:
        return int(self.__response.json().get('meta', {}).get('count', 0))

    def get_status(self) -> int:
        return self.__response.status_code

    def get_reason(self) -> str:
        return self.__response.reason

    def get_response(self) -> Response:
        return self.__response
