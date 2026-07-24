from __future__ import annotations

from klarient import PagedResponse, PagedResponseModel, SyncResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.phishing.models import PhishingRow
from psat.v0_3_0.reports.phishing.requests import PhishingFilter


class PhishingResource(SyncResource[_SyncClientImpl]):
    """Paged phishing report resource."""

    def retrieve(
            self,
            options: PhishingFilter | None = None,
    ) -> PagedResponse[PhishingRow]:
        """Retrieve phishing report rows."""
        return self._executor.get(
            PagedResponseModel(PhishingRow, PSATPagination()),
            options,
        )
