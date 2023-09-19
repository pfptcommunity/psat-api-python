"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from psat_api.v3.filters.PhishingFilter import PhishingFilter


class PhishingExtendedFilter(PhishingFilter):
    def __init__(self):
        super().__init__()
