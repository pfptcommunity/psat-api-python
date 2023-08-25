"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from psat_api.v2.filters.CyberStrengthFilter import CyberStrengthFilter as CyberStrengthFilterV2

class CyberStrengthFilter(CyberStrengthFilterV2):
    def __init__(self):
        super().__init__()