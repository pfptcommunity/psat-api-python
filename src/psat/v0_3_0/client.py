from __future__ import annotations

from klarient import (
    RequestsClient,
    RequestsOptions,
)
from psat.common import Region, base_url_for
from psat.v0_3_0.reports.resources import ReportsResource

REPORTING_API_ROOT = "api/reporting/v0.3.0"


class PSATClient(RequestsClient):
    """Synchronous PSAT Reporting API client for version 0.3.0.

    The client exposes report resources under ``reports``. Use ``options`` to
    tune timeout, proxy, or SSL behavior when the local network environment
    requires it.
    """

    reports: ReportsResource

    def __init__(
            self,
            region: Region | str,
            api_token: str,
            *,
            options: RequestsOptions | None = None,
    ) -> None:
        """Create a PSAT reporting client.

        ``region`` selects the PSAT API host and may be a ``Region`` enum value
        or its string form. ``api_token`` is sent as the ``x-apikey-token``
        header. ``options`` configures network behavior without exposing
        transport internals.
        """
        super().__init__(
            base_url=base_url_for(region),
            headers={
                "Content-Type": "application/json",
                "x-apikey-token": api_token,
            },
            options=options,
        )
        self.__reports = self._bind_resource(
            ReportsResource,
            segment=REPORTING_API_ROOT,
        )

    @property
    def reports(self) -> ReportsResource:
        """Reporting API resource root."""
        return self.__reports
