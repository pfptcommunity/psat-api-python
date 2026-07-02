from __future__ import annotations

from collections.abc import Mapping
from typing import Any, ClassVar, Generic, TypeVar, cast

AttributesT = TypeVar("AttributesT", bound="ReportAttributes")


class ReportAttributes(dict[str, Any]):
    """Base attribute mapping for PSAT report rows."""

    def _string(self, name: str) -> str:
        value = self.get(name)
        return "" if value is None else str(value)

    def _optional_string(self, name: str) -> str | None:
        value = self.get(name)
        return None if value is None else str(value)

    def _integer(self, name: str) -> int | None:
        value = self.get(name)
        if value is None:
            return None
        try:
            return int(str(value))
        except (TypeError, ValueError):
            return None

    def _float(self, name: str) -> float | None:
        value = self.get(name)
        if value is None:
            return None
        try:
            return float(str(value))
        except (TypeError, ValueError):
            return None

    def _boolean(self, name: str) -> bool | None:
        value = self.get(name)
        return value if isinstance(value, bool) else None

    @property
    def user_first_name(self) -> str:
        """User first name."""
        return self._string("userfirstname")

    @property
    def user_last_name(self) -> str:
        """User last name."""
        return self._string("userlastname")

    @property
    def user_email_address(self) -> str:
        """User email address."""
        return self._string("useremailaddress")

    @property
    def user_active(self) -> bool | None:
        """Whether the user is active when provided by the report."""
        return self._boolean("useractiveflag")

    @property
    def user_deleted_date(self) -> str | None:
        """User deleted date when present."""
        return self._optional_string("userdeleteddate")

    @property
    def user_tags(self) -> dict[str, Any]:
        """User tags included on the row."""
        value = self.get("usertags", {})
        return dict(value) if isinstance(value, Mapping) else {}

    @property
    def sso_id(self) -> str:
        """User SSO identifier."""
        return self._string("sso_id")


class ReportRow(dict[str, Any], Generic[AttributesT]):
    """Base data row returned by PSAT report endpoints."""

    attributes_model: ClassVar[type[ReportAttributes]] = ReportAttributes

    @property
    def id(self) -> str:
        """Row identifier."""
        value = self.get("id")
        return "" if value is None else str(value)

    @property
    def type(self) -> str:
        """Row type value."""
        return str(self.get("type") or "")

    @property
    def attributes(self) -> AttributesT:
        """Typed row attributes."""
        value = self.get("attributes", {})
        if not isinstance(value, Mapping):
            value = {}
        return cast(AttributesT, self.attributes_model(value))

    @property
    def email(self) -> str:
        """Convenience access to the user email address."""
        value = self.get("useremailaddress")
        if value is not None:
            return str(value)
        return self.attributes.user_email_address
