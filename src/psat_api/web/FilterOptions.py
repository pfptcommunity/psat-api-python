"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from datetime import datetime
from typing import TypeVar, Dict

TFilterOptions = TypeVar('TFilterOptions', bound='FilterOptions')

class FilterOptions:
    __PAGE_NUMBER = 'page[number]'
    __PAGE_SIZE = 'page[size]'
    _options: dict[str]
    
    def __init__(self):
        self._options = {}

    def clear(self):
        self._options.clear()

    def set_page_number(self, page_number: int) -> TFilterOptions:
        self._options[self.__PAGE_NUMBER] = page_number
        return self

    def get_page_number(self) -> int:
        return self._options[self.__PAGE_NUMBER]

    def set_page_size(self, page_size: int) -> TFilterOptions:
        self._options[self.__PAGE_SIZE] = page_size
        return self

    def get_page_size(self) -> int:
        return self._options[self.__PAGE_SIZE]
    
    def __str__(self) -> str:
        param = ''
        for k, v in self._options.items():
            if type(v) == list:
                if len(v):
                    if all(isinstance(n, str) for n in v):
                        param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, ','.join(v))
            elif type(v) == datetime:
                param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, v.strftime('%Y-%m-%dT%H:%M:%S'))
            else:
                param += "{}{}={}".format(('', '&')[len(param) > 0], k, v)
        return param

    @property
    def params(self) -> Dict:
        param = {}
        for k, v in self._options.items():
            if type(v) == list:
                if len(v):
                    if all(isinstance(n, str) for n in v):
                        param[k] = "[{}]".format(','.join(v))
            elif type(v) == datetime:
                param[k] = "[{}]".format(v.strftime('%Y-%m-%dT%H:%M:%S'))
            else:
                param[k] = v
        return param
