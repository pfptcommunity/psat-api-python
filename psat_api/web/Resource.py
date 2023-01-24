"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.1
License: MIT
"""
from posixpath import join
from requests import Session
from typing import TypeVar

TResource = TypeVar('TResource', bound="Resource")


class Resource:
    __parent = TResource
    __name: str
    __session = Session()

    def __init__(self, parent: TResource, uri: str):
        self.__parent = parent
        self.__name = uri

    @property
    def name(self) -> str:
        return self.__name

    @property
    def uri(self) -> str:
        uri = self.__name
        parent = self.__parent
        while parent is not None:
            uri = join(parent.name, uri)
            parent = parent.__parent
        return uri

    @property
    def parent(self):
        return self.__parent

    @property
    def _session(self):
        return self.__session
