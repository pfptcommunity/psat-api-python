from __future__ import annotations

from klarient import PagedResponse, PagedResponseModel, SyncResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.users.models import UserRow
from psat.v0_3_0.reports.users.requests import UsersFilter


class UsersResource(SyncResource[_SyncClientImpl]):
    """Paged users report resource."""

    def retrieve(
            self,
            options: UsersFilter | None = None,
    ) -> PagedResponse[UserRow]:
        """Retrieve users report rows."""
        return self._executor.get(
            PagedResponseModel(UserRow, PSATPagination()),
            options,
        )
