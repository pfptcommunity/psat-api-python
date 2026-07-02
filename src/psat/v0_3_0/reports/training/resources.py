from __future__ import annotations

from typing import Any

from klarient import Page, PageNumberState, PageableResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.training.models import TrainingRow
from psat.v0_3_0.reports.training.requests import TrainingFilter


class TrainingResource(PageableResource[_SyncClientImpl, TrainingRow, PageNumberState]):
    """Paged training report resource."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(
            owner,
            segment=segment,
            page_item_model=TrainingRow,
            pagination=PSATPagination(),
            **kwargs,
        )

    def retrieve(
            self,
            options: TrainingFilter | None = None,
    ) -> Page[TrainingRow]:
        """Retrieve a page of training report rows."""
        return self._retrieve_page(options=options)
