from __future__ import annotations

from typing import Any

from klarient import Page, PageNumberState, PageableResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.cyberstrength.models import CyberStrengthRow
from psat.v0_3_0.reports.cyberstrength.requests import CyberStrengthFilter


class CyberStrengthResource(PageableResource[_SyncClientImpl, CyberStrengthRow, PageNumberState]):
    """Paged CyberStrength report resource."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(
            owner,
            segment=segment,
            page_item_model=CyberStrengthRow,
            pagination=PSATPagination(),
            **kwargs,
        )

    def retrieve(
            self,
            options: CyberStrengthFilter | None = None,
    ) -> Page[CyberStrengthRow]:
        """Retrieve a page of CyberStrength report rows."""
        return self._retrieve_page(options=options)
