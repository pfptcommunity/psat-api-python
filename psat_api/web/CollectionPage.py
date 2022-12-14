"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.0
License: MIT
"""
from urllib.parse import urljoin
from requests import Response
from requests import Session


class CollectionPage:
    __response: Response
    __session: Session
    __initial: bool
    __initial_url: str

    def __init__(self, session: Session, response: Response):
        self.__session = session
        self.__response = response
        self.__initial = True
        self.__initial_url = self.get_self()

    def __iter__(self):
        if not self.__initial:
            self.__initial = True
            self.__response = self.__session.get(self.__initial_url)
        return self

    def __next__(self):
        if self.__initial:
            self.__initial = False
            return self.__response.json().get('data', {})
        elif self.get_next() is not None:
            self.__response = self.__session.get(self.get_next())
            return self.__response.json().get('data', {})
        else:
            raise StopIteration

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
        return int((self.get_record_count() + self.get_page_size() - 1) / self.get_page_size())

    def get_record_count(self) -> int:
        return int(self.__response.json().get('meta', {}).get('count', 0))
