from __future__ import annotations

from typing import Self

from klarient import QueryFieldSpec, QuerySerialization, RequestField, list_of
from psat.reports.base import ReportFilter


class UsersFilter(ReportFilter):
    """Query filter for the users report."""

    def __init__(
            self,
            *,
            user_email_addresses: list[str] | None = None,
            include_deleted_users: bool | None = None,
            **common: object,
    ) -> None:
        super().__init__(**common)
        self._set_defined_fields(
            user_email_addresses=user_email_addresses,
            include_deleted_users=include_deleted_users,
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

    def add_user_email_address(self, value: str) -> Self:
        """Add a user email address filter."""
        self.user_email_addresses = [*(self.user_email_addresses or []), value]
        return self

    def include_deleted_user_records(self, enabled: bool = True) -> Self:
        """Include deleted users in the report."""
        self.include_deleted_users = enabled
        return self
