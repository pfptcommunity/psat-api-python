from collections.abc import Mapping

from psat.reports.models import ReportRow
from psat.v0_3_0.reports.phishing.models import PhishingAttributes


class PhishingExtendedAttributes(PhishingAttributes):
    """Attributes for PSAT extended phishing report rows."""

    @property
    def campaign_guid(self) -> str:
        """Campaign GUID."""
        return self._string("campaign_guid")

    @property
    def user_guid(self) -> str:
        """User GUID."""
        return self._string("user_guid")

    @property
    def ip_address(self) -> str:
        """IP address."""
        return self._string("ip_address")

    @property
    def browser(self) -> str:
        """Browser name."""
        return self._string("browser")

    @property
    def browser_version(self) -> str:
        """Browser version."""
        return self._string("browser_version")

    @property
    def os(self) -> str:
        """Operating system."""
        return self._string("os")

    @property
    def os_version(self) -> str:
        """Operating system version."""
        return self._string("os_version")

    @property
    def user_agent(self) -> str:
        """User agent string."""
        return self._string("user_agent")

    @property
    def mobile_device_used(self) -> bool | None:
        """Whether a mobile device was used."""
        return self._boolean("mobile_device_used")

    @property
    def whois_latitude(self) -> str:
        """WHOIS latitude value."""
        return self._string("whois_latitude")

    @property
    def whois_longitude(self) -> str:
        """WHOIS longitude value."""
        return self._string("whois_longitude")

    @property
    def whois_city(self) -> str:
        """WHOIS city value."""
        return self._string("whois_city")

    @property
    def whois_state(self) -> str:
        """WHOIS state value."""
        return self._string("whois_state")

    @property
    def whois_country(self) -> str:
        """WHOIS country value."""
        return self._string("whois_country")

    @property
    def whois_continent(self) -> str:
        """WHOIS continent value."""
        return self._string("whois_continent")

    @property
    def whois_domain(self) -> str:
        """WHOIS domain value."""
        return self._string("whois_domain")

    @property
    def whois_isp(self) -> str:
        """WHOIS ISP value."""
        return self._string("whois_isp")

    @property
    def whois_organization(self) -> str:
        """WHOIS organization value."""
        return self._string("whois_organization")

    @property
    def afr(self) -> float | None:
        """Attack failure rate value."""
        return self._float("afr")


class PhishingExtendedRow(ReportRow[PhishingExtendedAttributes]):
    """Typed row from the extended phishing report."""

    @property
    def attributes(self) -> PhishingExtendedAttributes:
        """Typed extended phishing report attributes."""
        value = self.get("attributes", {})
        return PhishingExtendedAttributes(value if isinstance(value, Mapping) else {})
