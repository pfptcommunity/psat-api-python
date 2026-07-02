from __future__ import annotations

from datetime import date, datetime
from typing import Self

from klarient import QueryFieldSpec, QuerySerialization, RequestField, list_of
from psat.reports.base import DatedRecordFilter


class PhishingFilter(DatedRecordFilter):
    """Query filter for the phishing report."""

    def __init__(
            self,
            *,
            event_start_date: date | datetime | None = None,
            event_end_date: date | datetime | None = None,
            campaign_names: list[str] | None = None,
            campaign_start_date: date | datetime | None = None,
            campaign_end_date: date | datetime | None = None,
            include_no_action: bool | None = None,
            user_email_addresses: list[str] | None = None,
            include_deleted_users: bool | None = None,
            include_archived_campaigns: bool | None = None,
            **common: object,
    ) -> None:
        super().__init__(**common)
        self._set_defined_fields(
            event_start_date=event_start_date,
            event_end_date=event_end_date,
            campaign_names=campaign_names,
            campaign_start_date=campaign_start_date,
            campaign_end_date=campaign_end_date,
            include_no_action=include_no_action,
            user_email_addresses=user_email_addresses,
            include_deleted_users=include_deleted_users,
            include_archived_campaigns=include_archived_campaigns,
        )

    event_start_date = RequestField[date | datetime](
        name="filter[_eventtimestamp_start]",
        value_type=(date, datetime),
    )
    event_end_date = RequestField[date | datetime](
        name="filter[_eventtimestamp_end]",
        value_type=(date, datetime),
    )
    campaign_names = RequestField[list[str]](
        name="filter[_campaignname]",
        query=QueryFieldSpec(QuerySerialization.BRACKETED),
        value_type=list,
        validator=list_of(str),
    )
    campaign_start_date = RequestField[date | datetime](
        name="filter[_campaignstartdate_start]",
        value_type=(date, datetime),
    )
    campaign_end_date = RequestField[date | datetime](
        name="filter[_campaignstartdate_end]",
        value_type=(date, datetime),
    )
    include_no_action = RequestField[bool](
        name="filter[_includenoaction]",
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
    include_archived_campaigns = RequestField[bool](
        name="filter[_includearchivedcampaigns]",
        value_type=bool,
    )

    def with_event_start_date(self, value: date | datetime) -> Self:
        """Set the event timestamp start filter."""
        self.event_start_date = value
        return self

    def with_event_end_date(self, value: date | datetime) -> Self:
        """Set the event timestamp end filter."""
        self.event_end_date = value
        return self

    def add_campaign_name(self, value: str) -> Self:
        """Add a campaign name filter."""
        self.campaign_names = [*(self.campaign_names or []), value]
        return self

    def with_campaign_start_date(self, value: date | datetime) -> Self:
        """Set the campaign start date filter."""
        self.campaign_start_date = value
        return self

    def with_campaign_end_date(self, value: date | datetime) -> Self:
        """Set the campaign end date filter."""
        self.campaign_end_date = value
        return self

    def include_no_action_records(self, enabled: bool = True) -> Self:
        """Include rows where the user took no action."""
        self.include_no_action = enabled
        return self

    def add_user_email_address(self, value: str) -> Self:
        """Add a user email address filter."""
        self.user_email_addresses = [*(self.user_email_addresses or []), value]
        return self

    def include_deleted_user_records(self, enabled: bool = True) -> Self:
        """Include deleted users in the report."""
        self.include_deleted_users = enabled
        return self

    def include_archived_campaign_records(self, enabled: bool = True) -> Self:
        """Include archived campaigns in the report."""
        self.include_archived_campaigns = enabled
        return self
