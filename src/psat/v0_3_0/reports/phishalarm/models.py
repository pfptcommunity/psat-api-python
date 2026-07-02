from psat.reports.models import ReportAttributes, ReportRow


class PhishAlarmAttributes(ReportAttributes):
    """Attributes for PSAT PhishAlarm report rows."""

    @property
    def campaign_name(self) -> str:
        """Campaign name."""
        return self._string("campaignname")

    @property
    def action(self) -> str:
        """PhishAlarm action."""
        return self._string("action")

    @property
    def email_type(self) -> str:
        """Reported email type."""
        return self._string("emailtype")

    @property
    def received_date(self) -> str:
        """Email received date."""
        return self._string("receiveddate")

    @property
    def reported_date(self) -> str:
        """Email reported date."""
        return self._string("reporteddate")

    @property
    def elapsed_hours(self) -> str:
        """Elapsed hours between receipt and report."""
        return self._string("elapsedhours")

    @property
    def os(self) -> str:
        """Operating system value."""
        return self._string("os")

    @property
    def email_client_version(self) -> str:
        """Email client version."""
        return self._string("emailclientversion")

    @property
    def assessment_soft_deleted_date(self) -> str | None:
        """Assessment soft deleted date when present."""
        return self._optional_string("assessmentsoftdeleteddate")


class PhishAlarmRow(ReportRow[PhishAlarmAttributes]):
    """Typed row from the PhishAlarm report."""

    attributes_model = PhishAlarmAttributes
