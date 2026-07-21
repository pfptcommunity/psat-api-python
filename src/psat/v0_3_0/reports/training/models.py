from collections.abc import Mapping

from psat.reports.models import ReportAttributes, ReportRow


class TrainingAttributes(ReportAttributes):
    """Attributes for PSAT training report rows."""

    @property
    def user_assignment_status(self) -> str:
        """User assignment status."""
        return self._string("userassignmentstatus")

    @property
    def assignment_name(self) -> str:
        """Assignment name."""
        return self._string("assignmentname")

    @property
    def assignment_start_date(self) -> str:
        """Assignment start date."""
        return self._string("assignmentstartdate")

    @property
    def assignment_deleted_date(self) -> str | None:
        """Assignment deleted date when present."""
        return self._optional_string("assignmentdeleteddate")

    @property
    def assignment_due_date(self) -> str:
        """Assignment due date."""
        return self._string("assignmentduedate")

    @property
    def assignment_status(self) -> str:
        """Assignment status."""
        return self._string("assignmentstatus")

    @property
    def assignment_method(self) -> str:
        """Assignment method."""
        return self._string("assignmentmethod")

    @property
    def duration(self) -> str:
        """Training duration."""
        return self._string("duration")

    @property
    def auto_enroll(self) -> bool | None:
        """Whether auto enrollment was enabled."""
        return self._boolean("isautoenroll")

    @property
    def module_name_admin(self) -> str:
        """Module name shown to administrators."""
        return self._string("modulename_admin")

    @property
    def module_name_user(self) -> str:
        """Module name shown to users."""
        return self._string("modulename_user")

    @property
    def module_type(self) -> str:
        """Module type."""
        return self._string("moduletype")

    @property
    def module_attempt_date(self) -> str | None:
        """Module attempt date when present."""
        return self._optional_string("moduleattemptdate")

    @property
    def module_last_action(self) -> str | None:
        """Last module action when present."""
        return self._optional_string("modulelastaction")

    @property
    def seconds_in_module_attempt(self) -> int | None:
        """Seconds spent in the module attempt."""
        return self._integer("secondsinmoduleattempt")

    @property
    def module_attempt_end_status(self) -> str | None:
        """Module attempt end status when present."""
        return self._optional_string("moduleattemptendstatus")

    @property
    def module_attempt_status(self) -> str:
        """Module attempt status."""
        return self._string("moduleattemptstatus")

    @property
    def module_attempt_score(self) -> float | None:
        """Module attempt score."""
        return self._float("moduleattemptscore")

    @property
    def module_attempt_score_correct(self) -> int | None:
        """Number of correct answers in the module attempt."""
        return self._integer("moduleattemptscorecorrect")

    @property
    def module_attempt_score_answered(self) -> int | None:
        """Number of answered questions in the module attempt."""
        return self._integer("moduleattemptscoreanswered")

    @property
    def assignment_deleted(self) -> bool | None:
        """Whether the assignment was deleted."""
        return self._boolean("assignmentdeleted")

    @property
    def user_removed_from_assignment(self) -> bool | None:
        """Whether the user was removed from the assignment."""
        return self._boolean("userremovedfromassignment")

    @property
    def freeplay(self) -> bool | None:
        """Whether the row is from freeplay training."""
        return self._boolean("isfreeplay")

    @property
    def force_completed_date(self) -> str | None:
        """Forced completion date when present."""
        return self._optional_string("forcecompleteddate")


class TrainingRow(ReportRow[TrainingAttributes]):
    """Typed row from the training report."""

    @property
    def attributes(self) -> TrainingAttributes:
        """Typed training report attributes."""
        value = self.get("attributes", {})
        return TrainingAttributes(value if isinstance(value, Mapping) else {})
