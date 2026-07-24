from __future__ import annotations

from klarient import PagedResponse, PagedResponseModel, SyncResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.phishing_extended.models import PhishingExtendedRow
from psat.v0_3_0.reports.phishing_extended.requests import PhishingExtendedFilter


class PhishingExtendedResource(
    SyncResource[_SyncClientImpl],
):
    """Paged extended phishing report resource."""

    def retrieve(
            self,
            options: PhishingExtendedFilter | None = None,
    ) -> PagedResponse[PhishingExtendedRow]:
        """Retrieve extended phishing report rows."""
        return self._executor.get(
            PagedResponseModel(PhishingExtendedRow, PSATPagination()),
            options,
        )
