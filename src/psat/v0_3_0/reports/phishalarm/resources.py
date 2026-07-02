from __future__ import annotations

from typing import Any

from klarient import Page, PageNumberState, PageableResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.phishalarm.models import PhishAlarmRow
from psat.v0_3_0.reports.phishalarm.requests import PhishAlarmFilter


class PhishAlarmResource(PageableResource[_SyncClientImpl, PhishAlarmRow, PageNumberState]):
    """Paged PhishAlarm report resource."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(
            owner,
            segment=segment,
            page_item_model=PhishAlarmRow,
            pagination=PSATPagination(),
            **kwargs,
        )

    def retrieve(
            self,
            options: PhishAlarmFilter | None = None,
    ) -> Page[PhishAlarmRow]:
        """Retrieve a page of PhishAlarm report rows."""
        return self._retrieve_page(options=options)
