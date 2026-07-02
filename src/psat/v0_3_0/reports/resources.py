from __future__ import annotations

from typing import Any

from klarient import SyncResource
from klarient.http.client import _SyncClientImpl
from psat.v0_3_0.reports.cyberstrength.resources import CyberStrengthResource
from psat.v0_3_0.reports.enrollments.resources import TrainingEnrollmentsResource
from psat.v0_3_0.reports.phishalarm.resources import PhishAlarmResource
from psat.v0_3_0.reports.phishing.resources import PhishingResource
from psat.v0_3_0.reports.phishing_extended.resources import PhishingExtendedResource
from psat.v0_3_0.reports.training.resources import TrainingResource
from psat.v0_3_0.reports.users.resources import UsersResource


class ReportsResource(SyncResource[_SyncClientImpl]):
    """PSAT Reporting API resource root."""

    def __init__(self, owner: Any, *, segment: str = "", **kwargs: Any) -> None:
        super().__init__(owner, segment=segment, **kwargs)
        self.__cyberstrength = CyberStrengthResource(self, segment="cyberstrength")
        self.__phishalarm = PhishAlarmResource(self, segment="phishalarm")
        self.__phishing = PhishingResource(self, segment="phishing")
        self.__phishing_extended = PhishingExtendedResource(
            self,
            segment="phishing_extended",
        )
        self.__training = TrainingResource(self, segment="training")
        self.__enrollments = TrainingEnrollmentsResource(
            self,
            segment="trainingenrollments",
        )
        self.__users = UsersResource(self, segment="users")

    @property
    def cyberstrength(self) -> CyberStrengthResource:
        """CyberStrength report resource."""
        return self.__cyberstrength

    @property
    def phishalarm(self) -> PhishAlarmResource:
        """PhishAlarm report resource."""
        return self.__phishalarm

    @property
    def phishing(self) -> PhishingResource:
        """Phishing report resource."""
        return self.__phishing

    @property
    def phishing_extended(self) -> PhishingExtendedResource:
        """Extended phishing report resource."""
        return self.__phishing_extended

    @property
    def training(self) -> TrainingResource:
        """Training report resource."""
        return self.__training

    @property
    def enrollments(self) -> TrainingEnrollmentsResource:
        """Training enrollments report resource."""
        return self.__enrollments

    @property
    def users(self) -> UsersResource:
        """Users report resource."""
        return self.__users
