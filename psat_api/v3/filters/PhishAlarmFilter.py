"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from psat_api.v2.filters.PhishAlarmFilter import PhishAlarmFilter as PhishAlarmFilterV2


class PhishAlarmFilter(PhishAlarmFilterV2):
    def __init__(self):
        super().__init__()