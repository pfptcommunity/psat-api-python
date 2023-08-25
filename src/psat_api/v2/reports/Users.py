"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat-apiLicense: MIT
"""
from requests import PreparedRequest
from psat_api.v2.filters.UsersFilter import UsersFilter
from psat_api.web import PageIterator, Resource


class Users(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: UsersFilter = UsersFilter()) -> PageIterator:
        request = PreparedRequest()
        request.prepare_url(self.uri, options.params)
        request.method = 'get'
        return PageIterator(self._session, request)
