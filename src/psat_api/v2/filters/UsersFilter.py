"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-apiLicense: MIT
"""
from psat_api.v1.filters.UsersFilter import UsersFilter as UsersFilterV1


class UsersFilter(UsersFilterV1):
    def __init__(self):
        super().__init__()
