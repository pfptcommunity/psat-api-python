"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from psat_api.v2.filters.EnrollmentsFilter import EnrollmentsFilter as EnrollmentsFilterV2

class EnrollmentsFilter(EnrollmentsFilterV2):
    def __init__(self):
        super().__init__()