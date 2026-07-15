from __future__ import annotations

from datetime import date, datetime
from typing import Self

from klarient import QueryFieldSpec, QuerySerialization, RequestField, list_of
from psat.common import AssignmentStatus
from psat.reports.base import DatedRecordFilter


class TrainingFilter(DatedRecordFilter):
    """Query filter for the training report."""

    def __init__(
            self,
            *,
            attempt_date_start: date | datetime | None = None,
            attempt_date_end: date | datetime | None = None,
            assignment_names: list[str] | None = None,
            assignment_start_date: date | datetime | None = None,
            assignment_end_date: date | datetime | None = None,
            assignment_due_start_date: date | datetime | None = None,
            assignment_due_end_date: date | datetime | None = None,
            include_not_started: bool | None = None,
            user_email_addresses: list[str] | None = None,
            include_deleted_users: bool | None = None,
            include_deleted_assignments: bool | None = None,
            include_removed_users: bool | None = None,
            user_assignment_status: list[AssignmentStatus] | None = None,
            include_freeplay: bool | None = None,
            **common: object,
    ) -> None:
        super().__init__(**common)
        self._set_optional_fields(
            attempt_date_start=attempt_date_start,
            attempt_date_end=attempt_date_end,
            assignment_names=assignment_names,
            assignment_start_date=assignment_start_date,
            assignment_end_date=assignment_end_date,
            assignment_due_start_date=assignment_due_start_date,
            assignment_due_end_date=assignment_due_end_date,
            include_not_started=include_not_started,
            user_email_addresses=user_email_addresses,
            include_deleted_users=include_deleted_users,
            include_deleted_assignments=include_deleted_assignments,
            include_removed_users=include_removed_users,
            user_assignment_status=user_assignment_status,
            include_freeplay=include_freeplay,
        )

    attempt_date_start = RequestField[date | datetime](
        name="filter[_attemptdate_start]",
        value_type=(date, datetime),
    )
    attempt_date_end = RequestField[date | datetime](
        name="filter[_attemptdate_end]",
        value_type=(date, datetime),
    )
    assignment_names = RequestField[list[str]](
        name="filter[_assignmentname]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    assignment_start_date = RequestField[date | datetime](
        name="filter[_assignmentstartdate_start]",
        value_type=(date, datetime),
    )
    assignment_end_date = RequestField[date | datetime](
        name="filter[_assignmentstartdate_end]",
        value_type=(date, datetime),
    )
    assignment_due_start_date = RequestField[date | datetime](
        name="filter[_assignmentduedate_start]",
        value_type=(date, datetime),
    )
    assignment_due_end_date = RequestField[date | datetime](
        name="filter[_assignmentduedate_end]",
        value_type=(date, datetime),
    )
    include_not_started = RequestField[bool](
        name="filter[_includenotstarted]",
        value_type=bool,
    )
    user_email_addresses = RequestField[list[str]](
        name="filter[_useremailaddress]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    include_deleted_users = RequestField[bool](
        name="filter[_includedeletedusers]",
        value_type=bool,
    )
    include_deleted_assignments = RequestField[bool](
        name="filter[_includedeletedassignments]",
        value_type=bool,
    )
    include_removed_users = RequestField[bool](
        name="filter[_includeremovedusers]",
        value_type=bool,
    )
    user_assignment_status = RequestField[list[AssignmentStatus]](
        name="filter[_userassignmentstatus]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(AssignmentStatus),
    )
    include_freeplay = RequestField[bool](
        name="filter[_includefreeplay]",
        value_type=bool,
    )

    def with_attempt_date_start(self, value: date | datetime) -> Self:
        """Set the module attempt date start filter."""
        self.attempt_date_start = value
        return self

    def with_attempt_date_end(self, value: date | datetime) -> Self:
        """Set the module attempt date end filter."""
        self.attempt_date_end = value
        return self

    def add_assignment_name(self, value: str) -> Self:
        """Add an assignment name filter."""
        self.assignment_names = [*(self.assignment_names or []), value]
        return self

    def with_assignment_start_date(self, value: date | datetime) -> Self:
        """Set the assignment start date filter."""
        self.assignment_start_date = value
        return self

    def with_assignment_end_date(self, value: date | datetime) -> Self:
        """Set the assignment end date filter."""
        self.assignment_end_date = value
        return self

    def with_assignment_due_start_date(self, value: date | datetime) -> Self:
        """Set the assignment due date start filter."""
        self.assignment_due_start_date = value
        return self

    def with_assignment_due_end_date(self, value: date | datetime) -> Self:
        """Set the assignment due date end filter."""
        self.assignment_due_end_date = value
        return self

    def include_not_started_assignments(self, enabled: bool = True) -> Self:
        """Include not started assignments in the report."""
        self.include_not_started = enabled
        return self

    def add_user_email_address(self, value: str) -> Self:
        """Add a user email address filter."""
        self.user_email_addresses = [*(self.user_email_addresses or []), value]
        return self

    def include_deleted_user_records(self, enabled: bool = True) -> Self:
        """Include deleted users in the report."""
        self.include_deleted_users = enabled
        return self

    def include_deleted_assignment_records(self, enabled: bool = True) -> Self:
        """Include deleted assignments in the report."""
        self.include_deleted_assignments = enabled
        return self

    def include_removed_user_records(self, enabled: bool = True) -> Self:
        """Include removed users in the report."""
        self.include_removed_users = enabled
        return self

    def add_user_assignment_status(self, value: AssignmentStatus) -> Self:
        """Add a user assignment status filter."""
        self.user_assignment_status = [*(self.user_assignment_status or []), value]
        return self

    def include_freeplay_records(self, enabled: bool = True) -> Self:
        """Include freeplay records in the report."""
        self.include_freeplay = enabled
        return self
