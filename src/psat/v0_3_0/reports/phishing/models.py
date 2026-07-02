from psat.reports.models import ReportAttributes, ReportRow


class PhishingAttributes(ReportAttributes):
    """Attributes for PSAT phishing report rows."""

    @property
    def sent_timestamp(self) -> str:
        """Message sent timestamp."""
        return self._string("senttimestamp")

    @property
    def event_timestamp(self) -> str:
        """Phishing event timestamp."""
        return self._string("eventtimestamp")

    @property
    def event_type(self) -> str:
        """Phishing event type."""
        return self._string("eventtype")

    @property
    def campaign_name(self) -> str:
        """Campaign name."""
        return self._string("campaignname")

    @property
    def auto_enrollment(self) -> bool | None:
        """Whether the user was automatically enrolled."""
        return self._boolean("autoenrollment")

    @property
    def campaign_start_date(self) -> str:
        """Campaign start date."""
        return self._string("campaignstartdate")

    @property
    def campaign_end_date(self) -> str:
        """Campaign end date."""
        return self._string("campaignenddate")

    @property
    def campaign_type(self) -> str:
        """Campaign type."""
        return self._string("campaigntype")

    @property
    def campaign_status(self) -> str:
        """Campaign status."""
        return self._string("campaignstatus")

    @property
    def template_name(self) -> str:
        """Template name."""
        return self._string("templatename")

    @property
    def template_subject(self) -> str:
        """Template subject."""
        return self._string("templatesubject")

    @property
    def assessment_archived(self) -> bool | None:
        """Whether the assessment is archived."""
        return self._boolean("assessmentisarchived")


class PhishingRow(ReportRow[PhishingAttributes]):
    """Typed row from the phishing report."""

    attributes_model = PhishingAttributes
