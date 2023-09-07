"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from posixpath import join
from typing import TypeVar, Union

from requests import Session

TResource = TypeVar('TResource', bound=Union['Resource', None])


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
    def session(self):
        return self.__session
