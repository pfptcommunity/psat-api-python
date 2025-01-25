"""
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""
from enum import Enum


class AssignmentStatus(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
