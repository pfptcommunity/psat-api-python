from __future__ import annotations

from typing import Any

from klarient import Page, PageNumberState, PageableResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.phishing.models import PhishingRow
from psat.v0_3_0.reports.phishing.requests import PhishingFilter


class PhishingResource(PageableResource[_SyncClientImpl, PhishingRow, PageNumberState]):
    """Paged phishing report resource."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(
            owner,
            segment=segment,
            page_item_model=PhishingRow,
            pagination=PSATPagination(),
            **kwargs,
        )

    def retrieve(
            self,
            options: PhishingFilter | None = None,
    ) -> Page[PhishingRow]:
        """Retrieve a page of phishing report rows."""
        return self._retrieve_page(options=options)
