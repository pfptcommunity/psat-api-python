from __future__ import annotations

from klarient import PagedResponse, PagedResponseModel, SyncResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.cyberstrength.models import CyberStrengthRow
from psat.v0_3_0.reports.cyberstrength.requests import CyberStrengthFilter


class CyberStrengthResource(SyncResource[_SyncClientImpl]):
    """Paged CyberStrength report resource."""

    def retrieve(
            self,
            options: CyberStrengthFilter | None = None,
    ) -> PagedResponse[CyberStrengthRow]:
        """Retrieve CyberStrength report rows."""
        return self._executor.get(
            PagedResponseModel(CyberStrengthRow, PSATPagination()),
            options,
        )
