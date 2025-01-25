"""
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from requests import PreparedRequest

from psat_api.v3.filters.cyber_strength_filter import CyberStrengthFilter
from psat_api.web import PageIterator, Resource


class CyberStrength(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: CyberStrengthFilter = CyberStrengthFilter()):
        request = PreparedRequest()
        request.prepare_url(self.uri, options.params)
        request.method = 'get'
        return PageIterator(self.session, request)
