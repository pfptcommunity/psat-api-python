from __future__ import annotations

from datetime import date, datetime
from typing import Self

from klarient import QueryFieldSpec, QuerySerialization, RequestField, list_of
from psat.reports.base import DatedRecordFilter


class CyberStrengthFilter(DatedRecordFilter):
    """Query filter for the CyberStrength report."""

    def __init__(
            self,
            *,
            assignment_names: list[str] | None = None,
            assignment_start_date: date | datetime | None = None,
            assignment_end_date: date | datetime | None = None,
            question_start_date: date | datetime | None = None,
            question_end_date: date | datetime | None = None,
            include_not_started: bool | None = None,
            include_deleted_users: bool | None = None,
            include_deleted_assignments: bool | None = None,
            full_question: bool | None = None,
            assessment_types: list[str] | None = None,
            user_email_addresses: list[str] | None = None,
            **common: object,
    ) -> None:
        super().__init__(**common)
        self._set_defined_fields(
            assignment_names=assignment_names,
            assignment_start_date=assignment_start_date,
            assignment_end_date=assignment_end_date,
            question_start_date=question_start_date,
            question_end_date=question_end_date,
            include_not_started=include_not_started,
            include_deleted_users=include_deleted_users,
            include_deleted_assignments=include_deleted_assignments,
            full_question=full_question,
            assessment_types=assessment_types,
            user_email_addresses=user_email_addresses,
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
    question_start_date = RequestField[date | datetime](
        name="filter[_questiondate_start]",
        value_type=(date, datetime),
    )
    question_end_date = RequestField[date | datetime](
        name="filter[_questiondate_end]",
        value_type=(date, datetime),
    )
    include_not_started = RequestField[bool](
        name="filter[_includenotstarted]",
        value_type=bool,
    )
    include_deleted_users = RequestField[bool](
        name="filter[_includedeletedusers]",
        value_type=bool,
    )
    include_deleted_assignments = RequestField[bool](
        name="filter[_includedeletedassignments]",
        value_type=bool,
    )
    full_question = RequestField[bool](name="filter[_fullquestion]", value_type=bool)
    assessment_types = RequestField[list[str]](
        name="filter[_assessmenttype]",
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

    def with_question_start_date(self, value: date | datetime) -> Self:
        """Set the question date start filter."""
        self.question_start_date = value
        return self

    def with_question_end_date(self, value: date | datetime) -> Self:
        """Set the question date end filter."""
        self.question_end_date = value
        return self

    def include_not_started_assignments(self, enabled: bool = True) -> Self:
        """Include not started assignments in the report."""
        self.include_not_started = enabled
        return self

    def include_deleted_user_records(self, enabled: bool = True) -> Self:
        """Include deleted users in the report."""
        self.include_deleted_users = enabled
        return self

    def include_deleted_assignment_records(self, enabled: bool = True) -> Self:
        """Include deleted assignments in the report."""
        self.include_deleted_assignments = enabled
        return self

    def include_full_question(self, enabled: bool = True) -> Self:
        """Include full question text in the report."""
        self.full_question = enabled
        return self

    def add_assessment_type(self, value: str) -> Self:
        """Add an assessment type filter."""
        self.assessment_types = [*(self.assessment_types or []), value]
        return self

    def add_user_email_address(self, value: str) -> Self:
        """Add a user email address filter."""
        self.user_email_addresses = [*(self.user_email_addresses or []), value]
        return self
