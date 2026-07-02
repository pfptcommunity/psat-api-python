from __future__ import annotations

from typing import Any

from klarient import Page, PageNumberState, PageableResource
from klarient.http.client import _SyncClientImpl
from psat.reports.paging import PSATPagination
from psat.v0_3_0.reports.users.models import UserRow
from psat.v0_3_0.reports.users.requests import UsersFilter


class UsersResource(PageableResource[_SyncClientImpl, UserRow, PageNumberState]):
    """Paged users report resource."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(
            owner,
            segment=segment,
            page_item_model=UserRow,
            pagination=PSATPagination(),
            **kwargs,
        )

    def retrieve(
            self,
            options: UsersFilter | None = None,
    ) -> Page[UserRow]:
        """Retrieve a page of users report rows."""
        return self._retrieve_page(options=options)
