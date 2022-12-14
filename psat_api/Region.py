"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.0
License: MIT
"""
from enum import Enum


class Region(Enum):
    US = 'results.us.securityeducation.com'
    EU = 'results.eu.securityeducation.com'
    AP = 'results.ap.securityeducation.com'
