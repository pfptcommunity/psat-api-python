from __future__ import annotations

from typing import Any

from klarient import Page, PageNumberState, PageableResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.enrollments.models import TrainingEnrollmentsRow
from psat.v0_3_0.reports.enrollments.requests import TrainingEnrollmentsFilter


class TrainingEnrollmentsResource(
    PageableResource[_SyncClientImpl, TrainingEnrollmentsRow, PageNumberState],
):
    """Paged training enrollments report resource."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(
            owner,
            segment=segment,
            page_item_model=TrainingEnrollmentsRow,
            pagination=PSATPagination(),
            **kwargs,
        )

    def retrieve(
            self,
            options: TrainingEnrollmentsFilter | None = None,
    ) -> Page[TrainingEnrollmentsRow]:
        """Retrieve a page of training enrollment report rows."""
        return self._retrieve_page(options=options)
