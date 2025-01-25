"""
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from requests import PreparedRequest

from psat_api.v3.filters.phishing_filter import PhishingFilter
from psat_api.web import PageIterator, Resource


class Phishing(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: PhishingFilter = PhishingFilter()) -> PageIterator:
        request = PreparedRequest()
        request.prepare_url(self.uri, options.params)
        request.method = 'get'
        return PageIterator(self.session, request)
