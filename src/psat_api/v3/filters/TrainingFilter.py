"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from psat_api.v2.filters.TrainingFilter import TrainingFilter as TrainingFilterV2

class TrainingFilter(TrainingFilterV2):
    def __init__(self):
        super().__init__()
