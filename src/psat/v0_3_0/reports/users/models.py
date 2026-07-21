from collections.abc import Mapping

from psat.reports.models import ReportAttributes, ReportRow


class UserAttributes(ReportAttributes):
    """Attributes for PSAT users report rows."""

    @property
    def locale(self) -> str:
        """User locale."""
        return self._string("userlocale")

    @property
    def timezone(self) -> str:
        """User time zone."""
        return self._string("usertimezone")

    @property
    def data_last_updated(self) -> str:
        """Timestamp when the row data was last updated."""
        return self._string("datalastupdated")


class UserRow(ReportRow[UserAttributes]):
    """Typed row from the users report."""

    @property
    def attributes(self) -> UserAttributes:
        """Typed users report attributes."""
        value = self.get("attributes", {})
        return UserAttributes(value if isinstance(value, Mapping) else {})
