"""
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from enum import Enum


class Region(Enum):
    US = 'results.us.securityeducation.com'
    EU = 'results.eu.securityeducation.com'
    AP = 'results.ap.securityeducation.com'
