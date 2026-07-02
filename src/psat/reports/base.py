from __future__ import annotations

from datetime import date, datetime
from typing import Self

from klarient import (
    HTTPRequestOptions,
    PageNumberState,
    QueryFields,
    QueryRequest,
    RequestField,
)
from psat.common import PSATValueEncoder


class ReportFilter(QueryRequest):
    """Base query filter for PSAT report endpoints."""

    def __init__(
            self,
            *,
            page_number: int | None = None,
            page_size: int | None = None,
            user_tag_enable: bool | None = None,
    ) -> None:
        super().__init__(encoder=PSATValueEncoder())
        self._set_defined_fields(
            page_number=page_number,
            page_size=page_size,
            user_tag_enable=user_tag_enable,
        )

    page_number = RequestField[int](name="page[number]", value_type=int)
    page_size = RequestField[int](name="page[size]", value_type=int)
    user_tag_enable = RequestField[bool](value_type=bool)

    def _to_request_options(self) -> HTTPRequestOptions:
        return HTTPRequestOptions(query=QueryFields().encode(self))

    def _to_page_state(self, default: PageNumberState) -> PageNumberState:
        """Return the page state represented by this filter."""
        return PageNumberState(
            page_number=self.page_number if self.page_number is not None else default.page_number,
            page_size=self.page_size if self.page_size is not None else default.page_size,
        )

    def with_page(self, number: int, size: int | None = None) -> Self:
        """Set the requested report page and optionally the page size."""
        self.page_number = number
        if size is not None:
            self.page_size = size
        return self

    def with_page_size(self, size: int) -> Self:
        """Set the requested report page size."""
        self.page_size = size
        return self

    def enable_user_tags(self, enabled: bool = True) -> Self:
        """Request custom user tag fields in report rows.

        PSAT only includes the ``usertags`` response object when this query
        flag is enabled. Returned tags are tenant-defined dynamic fields and
        are exposed from report rows as ``row.attributes.user_tags``.
        """
        self.user_tag_enable = enabled
        return self

    def with_user_tag(self, tag: str, value: str) -> Self:
        """Filter report rows by one tenant-defined user tag value.

        User tag names are dynamic tenant data, so this intentionally writes a
        custom query field instead of declaring a fixed ``RequestField``.
        """
        self.set_custom_field(f"filter[user_tag][{tag}]", f"'{value}'")
        return self


class DatedRecordFilter(ReportFilter):
    """Report filter with data warehouse record update date bounds."""

    def __init__(
            self,
            *,
            page_number: int | None = None,
            page_size: int | None = None,
            user_tag_enable: bool | None = None,
            record_start_date: date | datetime | None = None,
            record_end_date: date | datetime | None = None,
    ) -> None:
        super().__init__(
            page_number=page_number,
            page_size=page_size,
            user_tag_enable=user_tag_enable,
        )
        self._set_defined_fields(
            record_start_date=record_start_date,
            record_end_date=record_end_date,
        )

    record_start_date = RequestField[date | datetime](
        name="filter[_dw_record_update_start_dt]",
        value_type=(date, datetime),
    )
    record_end_date = RequestField[date | datetime](
        name="filter[_dw_record_update_end_dt]",
        value_type=(date, datetime),
    )

    def with_record_start_date(self, value: date | datetime) -> Self:
        """Set the record update start date filter."""
        self.record_start_date = value
        return self

    def with_record_end_date(self, value: date | datetime) -> Self:
        """Set the record update end date filter."""
        self.record_end_date = value
        return self
