from __future__ import annotations

from datetime import date, datetime
from typing import Self

from klarient import QueryFieldSpec, QuerySerialization, RequestField, list_of
from psat.common import EnrollmentStatus
from psat.reports.base import ReportFilter


class TrainingEnrollmentsFilter(ReportFilter):
    """Query filter for the training enrollments report."""

    def __init__(
            self,
            *,
            created_date_start: date | datetime | None = None,
            created_date_end: date | datetime | None = None,
            assignment_names: list[str] | None = None,
            user_email_addresses: list[str] | None = None,
            status: list[EnrollmentStatus] | None = None,
            first_names: list[str] | None = None,
            last_names: list[str] | None = None,
            manager_email_addresses: list[str] | None = None,
            include_deleted_users: bool | None = None,
            include_removed_enrollments: bool | None = None,
            enrollment_removal_reason: str | None = None,
            **common: object,
    ) -> None:
        super().__init__(**common)
        self._set_defined_fields(
            created_date_start=created_date_start,
            created_date_end=created_date_end,
            assignment_names=assignment_names,
            user_email_addresses=user_email_addresses,
            status=status,
            first_names=first_names,
            last_names=last_names,
            manager_email_addresses=manager_email_addresses,
            include_deleted_users=include_deleted_users,
            include_removed_enrollments=include_removed_enrollments,
            enrollment_removal_reason=enrollment_removal_reason,
        )

    created_date_start = RequestField[date | datetime](
        name="filter[_created_start]",
        value_type=(date, datetime),
    )
    created_date_end = RequestField[date | datetime](
        name="filter[_created_end]",
        value_type=(date, datetime),
    )
    assignment_names = RequestField[list[str]](
        name="filter[_assignmentname]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    user_email_addresses = RequestField[list[str]](
        name="filter[_useremailaddress]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    status = RequestField[list[EnrollmentStatus]](
        name="filter[_filter_status]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(EnrollmentStatus),
    )
    first_names = RequestField[list[str]](
        name="filter[_userfirstname]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    last_names = RequestField[list[str]](
        name="filter[_userlastname]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    manager_email_addresses = RequestField[list[str]](
        name="filter[_manageremailaddress]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    include_deleted_users = RequestField[bool](
        name="filter[_includedeletedusers]",
        value_type=bool,
    )
    include_removed_enrollments = RequestField[bool](
        name="filter[_includeremovedenrollments]",
        value_type=bool,
    )
    enrollment_removal_reason = RequestField[str](
        name="filter[_enrollmentremovalreason]",
        value_type=str,
    )

    def with_created_date_start(self, value: date | datetime) -> Self:
        """Set the enrollment created date start filter."""
        self.created_date_start = value
        return self

    def with_created_date_end(self, value: date | datetime) -> Self:
        """Set the enrollment created date end filter."""
        self.created_date_end = value
        return self

    def add_assignment_name(self, value: str) -> Self:
        """Add an assignment name filter."""
        self.assignment_names = [*(self.assignment_names or []), value]
        return self

    def add_user_email_address(self, value: str) -> Self:
        """Add a user email address filter."""
        self.user_email_addresses = [*(self.user_email_addresses or []), value]
        return self

    def add_status(self, value: EnrollmentStatus) -> Self:
        """Add an enrollment status filter."""
        self.status = [*(self.status or []), value]
        return self

    def add_first_name(self, value: str) -> Self:
        """Add a user first name filter."""
        self.first_names = [*(self.first_names or []), value]
        return self

    def add_last_name(self, value: str) -> Self:
        """Add a user last name filter."""
        self.last_names = [*(self.last_names or []), value]
        return self

    def add_manager_email_address(self, value: str) -> Self:
        """Add a manager email address filter."""
        self.manager_email_addresses = [
            *(self.manager_email_addresses or []),
            value,
        ]
        return self

    def include_deleted_user_records(self, enabled: bool = True) -> Self:
        """Include deleted users in the report."""
        self.include_deleted_users = enabled
        return self

    def include_removed_enrollment_records(self, enabled: bool = True) -> Self:
        """Include removed enrollments in the report."""
        self.include_removed_enrollments = enabled
        return self

    def with_enrollment_removal_reason(self, value: str) -> Self:
        """Set the enrollment removal reason filter."""
        self.enrollment_removal_reason = value
        return self
