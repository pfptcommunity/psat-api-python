"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from requests import PreparedRequest

from psat_api.v1.filters.EnrollmentsFilter import EnrollmentsFilter
from psat_api.web.PageIterator import PageIterator
from psat_api.web.Resource import Resource

class Enrollments(Resource):

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: EnrollmentsFilter = EnrollmentsFilter()) -> PageIterator:
        request = PreparedRequest()
        request.prepare_url(self.uri, options.params)
        request.method = 'get'
        return PageIterator(self._session, request)
