"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from psat_api.v1.filters.PhishingFilter import PhishingFilter as PhishingFilterV1

class PhishingFilter(PhishingFilterV1):
    def __init__(self):
        super().__init__()