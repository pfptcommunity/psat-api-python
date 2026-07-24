from __future__ import annotations

from klarient import PagedResponse, PagedResponseModel, SyncResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.training.models import TrainingRow
from psat.v0_3_0.reports.training.requests import TrainingFilter


class TrainingResource(SyncResource[_SyncClientImpl]):
    """Paged training report resource."""

    def retrieve(
            self,
            options: TrainingFilter | None = None,
    ) -> PagedResponse[TrainingRow]:
        """Retrieve training report rows."""
        return self._executor.get(
            PagedResponseModel(TrainingRow, PSATPagination()),
            options,
        )
