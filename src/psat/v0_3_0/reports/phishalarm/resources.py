from __future__ import annotations

from klarient import PagedResponse, PagedResponseModel, SyncResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.phishalarm.models import PhishAlarmRow
from psat.v0_3_0.reports.phishalarm.requests import PhishAlarmFilter


class PhishAlarmResource(SyncResource[_SyncClientImpl]):
    """Paged PhishAlarm report resource."""

    def retrieve(
            self,
            options: PhishAlarmFilter | None = None,
    ) -> PagedResponse[PhishAlarmRow]:
        """Retrieve PhishAlarm report rows."""
        return self._executor.get(
            PagedResponseModel(PhishAlarmRow, PSATPagination()),
            options,
        )
