from enum import StrEnum


class Region(StrEnum):
    """PSAT reporting API regions."""

    US = "results.us.securityeducation.com"
    EU = "results.eu.securityeducation.com"
    AP = "results.ap.securityeducation.com"
    CA = "results.zenguide.ca"
    IN = "results.securityeducation.in"


class AssignmentStatus(StrEnum):
    """Training assignment status filter values."""

    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class EnrollmentStatus(StrEnum):
    """Training enrollment status filter values."""

    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    OVERDUE_IN_PROGRESS = "Overdue - In Progress"
    OVERDUE_NOT_STARTED = "Overdue - Not Started"
    COMPLETED = "Completed"
