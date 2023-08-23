"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: psat_api
License: MIT
"""
from enum import Enum


class EnrollmentStatus(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    OVERDUE_IN_PROGRESS = 'Overdue - In Progress'
    OVERDUE_NOT_STARTED = 'Overdue - Not Started'
    COMPLETED = 'Completed'
