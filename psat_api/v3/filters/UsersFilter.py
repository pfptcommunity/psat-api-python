"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat_apiLicense: MIT
"""
from psat_api.v2.filters.UsersFilter import UsersFilter as UsersFilterV2
class UsersFilter(UsersFilterV2):
    def __init__(self):
        super().__init__()