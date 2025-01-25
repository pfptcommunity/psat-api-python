"""
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from psat_api.v3.filters.phishing_filter import PhishingFilter


class PhishingExtendedFilter(PhishingFilter):
    def __init__(self):
        super().__init__()
