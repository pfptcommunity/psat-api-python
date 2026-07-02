from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, replace
from typing import Any
from urllib.parse import urljoin

from klarient import (
    DecodedResponsePaginationStrategy,
    PageInfo,
    PageParseContext,
    PageNumberRequest,
    PageNumberState,
    RequestOptionsProvider,
)


@dataclass(frozen=True, slots=True)
class PSATPagination(DecodedResponsePaginationStrategy[PageNumberState, Any]):
    """Pagination strategy for PSAT report responses."""

    page_size: int = 5000
    path: str = ""

    def bind(self, resource_path: str) -> PSATPagination:
        if self.path:
            return self
        return replace(self, path=resource_path)

    def initial_state(self, resource: object) -> PageNumberState:
        return PageNumberState(page_number=1, page_size=self.page_size)

    def request(self, state: PageNumberState) -> RequestOptionsProvider:
        return PageNumberRequest(state, "page[number]", "page[size]")

    def _extract_items(
            self,
            context: PageParseContext[PageNumberState, Any],
    ) -> tuple[Mapping[str, Any], ...]:
        rows = context.decoded.get("data", []) if isinstance(context.decoded, Mapping) else []
        return tuple(row for row in rows if isinstance(row, Mapping))

    def _build_page_info(
            self,
            context: PageParseContext[PageNumberState, Any],
            items: tuple[Any, ...],
    ) -> PageInfo:
        meta = context.decoded.get("meta", {}) if isinstance(context.decoded, Mapping) else {}
        links = context.decoded.get("links", {}) if isinstance(context.decoded, Mapping) else {}
        page_number = context.reader.integer(
            meta.get("page_number") if isinstance(meta, Mapping) else None,
            context.state.page_number,
        )
        page_size = context.reader.integer(
            meta.get("page_size") if isinstance(meta, Mapping) else None,
            context.state.page_size,
        )
        total = context.reader.integer(meta.get("count") if isinstance(meta, Mapping) else None)
        total_pages = max(1, (total + page_size - 1) // page_size) if page_size else 0
        return PageInfo(
            number=page_number,
            size=len(items),
            total_pages=total_pages,
            total_items=total,
            self_link=self._link(context.response.url, links, "self"),
            first_link=self._link(context.response.url, links, "first"),
            next_link=self._link(context.response.url, links, "next"),
            last_link=self._link(context.response.url, links, "last"),
        )

    def _next_state(
            self,
            context: PageParseContext[PageNumberState, Any],
            info: PageInfo,
    ) -> PageNumberState | None:
        if info.next_link or (info.total_pages is not None and info.number < info.total_pages):
            meta = context.decoded.get("meta", {}) if isinstance(context.decoded, Mapping) else {}
            page_size = context.reader.integer(
                meta.get("page_size") if isinstance(meta, Mapping) else None,
                context.state.page_size,
            )
            return PageNumberState(info.number + 1, page_size)
        return None

    @staticmethod
    def _link(base: str, links: object, name: str) -> str:
        if not isinstance(links, Mapping):
            return ""
        value = links.get(name)
        if not isinstance(value, str) or not value:
            return ""
        return urljoin(base, value)
