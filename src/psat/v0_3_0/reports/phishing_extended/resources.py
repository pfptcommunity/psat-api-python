from __future__ import annotations

from typing import Any

from klarient import Page, PageNumberState, PageableResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.phishing_extended.models import PhishingExtendedRow
from psat.v0_3_0.reports.phishing_extended.requests import PhishingExtendedFilter


class PhishingExtendedResource(
    PageableResource[_SyncClientImpl, PhishingExtendedRow, PageNumberState],
):
    """Paged extended phishing report resource."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(
            owner,
            segment=segment,
            page_item_model=PhishingExtendedRow,
            pagination=PSATPagination(),
            **kwargs,
        )

    def retrieve(
            self,
            options: PhishingExtendedFilter | None = None,
    ) -> Page[PhishingExtendedRow]:
        """Retrieve a page of extended phishing report rows."""
        return self._retrieve_page(options=options)
