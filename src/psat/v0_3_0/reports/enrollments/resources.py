from __future__ import annotations

from klarient import PagedResponse, PagedResponseModel, SyncResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.enrollments.models import TrainingEnrollmentsRow
from psat.v0_3_0.reports.enrollments.requests import TrainingEnrollmentsFilter


class TrainingEnrollmentsResource(
    SyncResource[_SyncClientImpl],
):
    """Paged training enrollments report resource."""

    def retrieve(
            self,
            options: TrainingEnrollmentsFilter | None = None,
    ) -> PagedResponse[TrainingEnrollmentsRow]:
        """Retrieve training enrollment report rows."""
        return self._executor.get(
            PagedResponseModel(TrainingEnrollmentsRow, PSATPagination()),
            options,
        )
