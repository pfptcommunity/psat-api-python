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
        parent = self.parent
        while parent is not None:
            uri = join(parent.name, uri)
            parent = parent.parent
        return uri

    @property
    def parent(self):
        return self.__parent

    @property
    def session(self):
        return self.__session
