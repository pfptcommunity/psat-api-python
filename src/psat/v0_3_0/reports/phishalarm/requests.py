from __future__ import annotations

from datetime import date, datetime
from typing import Self

from klarient import QueryFieldSpec, QuerySerialization, RequestField, list_of
from psat.reports.base import DatedRecordFilter


class PhishAlarmFilter(DatedRecordFilter):
    """Query filter for the PhishAlarm report."""

    def __init__(
            self,
            *,
            report_date_start: date | datetime | None = None,
            report_date_end: date | datetime | None = None,
            received_date_start: date | datetime | None = None,
            received_date_end: date | datetime | None = None,
            user_email_addresses: list[str] | None = None,
            include_deleted_users: bool | None = None,
            actions: list[str] | None = None,
            include_platform_notifications: bool | None = None,
            include_deleted_campaigns: bool | None = None,
            **common: object,
    ) -> None:
        super().__init__(**common)
        self._set_optional_fields(
            report_date_start=report_date_start,
            report_date_end=report_date_end,
            received_date_start=received_date_start,
            received_date_end=received_date_end,
            user_email_addresses=user_email_addresses,
            include_deleted_users=include_deleted_users,
            actions=actions,
            include_platform_notifications=include_platform_notifications,
            include_deleted_campaigns=include_deleted_campaigns,
        )

    report_date_start = RequestField[date | datetime](
        name="filter[_reporteddate_start]",
        value_type=(date, datetime),
    )
    report_date_end = RequestField[date | datetime](
        name="filter[_reporteddate_end]",
        value_type=(date, datetime),
    )
    received_date_start = RequestField[date | datetime](
        name="filter[_receiveddate_start]",
        value_type=(date, datetime),
    )
    received_date_end = RequestField[date | datetime](
        name="filter[_receiveddate_end]",
        value_type=(date, datetime),
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
    actions = RequestField[list[str]](
        name="filter[_action]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    include_platform_notifications = RequestField[bool](
        name="filter[_includeplatformnotifications]",
        value_type=bool,
    )
    include_deleted_campaigns = RequestField[bool](
        name="filter[_includedeletedcampaigns]",
        value_type=bool,
    )

    def with_report_date_start(self, value: date | datetime) -> Self:
        """Set the reported date start filter."""
        self.report_date_start = value
        return self

    def with_report_date_end(self, value: date | datetime) -> Self:
        """Set the reported date end filter."""
        self.report_date_end = value
        return self

    def with_received_date_start(self, value: date | datetime) -> Self:
        """Set the received date start filter."""
        self.received_date_start = value
        return self

    def with_received_date_end(self, value: date | datetime) -> Self:
        """Set the received date end filter."""
        self.received_date_end = value
        return self

    def add_user_email_address(self, value: str) -> Self:
        """Add a user email address filter."""
        self.user_email_addresses = [*(self.user_email_addresses or []), value]
        return self

    def include_deleted_user_records(self, enabled: bool = True) -> Self:
        """Include deleted users in the report."""
        self.include_deleted_users = enabled
        return self

    def add_action(self, value: str) -> Self:
        """Add a PhishAlarm action filter."""
        self.actions = [*(self.actions or []), value]
        return self

    def include_platform_notification_records(self, enabled: bool = True) -> Self:
        """Include platform notification records."""
        self.include_platform_notifications = enabled
        return self

    def include_deleted_campaign_records(self, enabled: bool = True) -> Self:
        """Include deleted campaigns in the report."""
        self.include_deleted_campaigns = enabled
        return self
