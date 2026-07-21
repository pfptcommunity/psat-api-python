from collections.abc import Mapping

from psat.reports.models import ReportAttributes, ReportRow


class TrainingEnrollmentsAttributes(ReportAttributes):
    """Attributes for PSAT training enrollment report rows."""

    @property
    def module_id(self) -> str:
        """Module identifier."""
        return self._string("module_id")

    @property
    def assignment_id(self) -> str:
        """Assignment identifier."""
        return self._string("assignment_id")

    @property
    def assignment_name(self) -> str:
        """Assignment name."""
        return self._string("assignmentname")

    @property
    def assignment_start_date(self) -> str:
        """Assignment start date."""
        return self._string("assignmentstartdate")

    @property
    def module_enrollment_date(self) -> str:
        """Module enrollment date."""
        return self._string("module_enrollment_date")

    @property
    def module_due_date(self) -> str:
        """Module due date."""
        return self._string("module_due_date")

    @property
    def user_assignment_completion_date_time(self) -> str | None:
        """User assignment completion timestamp when present."""
        return self._optional_string("userassignment_completion_date_time")

    @property
    def user_assignment_status(self) -> str:
        """User assignment status."""
        return self._string("userassignmentstatus")

    @property
    def assignment_due_date(self) -> str:
        """Assignment due date."""
        return self._string("assignmentduedate")

    @property
    def assignment_type(self) -> str:
        """Assignment type."""
        return self._string("assignment_type")

    @property
    def assignment_creation(self) -> str:
        """Assignment creation date."""
        return self._string("assignment_creation")

    @property
    def manager_email_address(self) -> str | None:
        """Manager email address when present."""
        return self._optional_string("manageremailaddress")

    @property
    def auto_enroll(self) -> bool | None:
        """Whether auto enrollment was enabled."""
        return self._boolean("is_auto_enroll")

    @property
    def module_name_admin(self) -> str:
        """Module name shown to administrators."""
        return self._string("modulename_admin")

    @property
    def module_name_user(self) -> str:
        """Module name shown to users."""
        return self._string("modulename_user")

    @property
    def module_attempt_status(self) -> str:
        """Module attempt status."""
        return self._string("module_attempt_status")

    @property
    def user_module_completion_date_time(self) -> str | None:
        """User module completion timestamp when present."""
        return self._optional_string("usermodule_completion_date_time")

    @property
    def enrollment_removal_reason(self) -> str | None:
        """Enrollment removal reason when present."""
        return self._optional_string("enrollmentremovalreason")

    @property
    def enrollment_removal_date(self) -> str | None:
        """Enrollment removal date when present."""
        return self._optional_string("enrollmentremovaldate")


class TrainingEnrollmentsRow(ReportRow[TrainingEnrollmentsAttributes]):
    """Typed row from the training enrollments report."""

    @property
    def attributes(self) -> TrainingEnrollmentsAttributes:
        """Typed training enrollment report attributes."""
        value = self.get("attributes", {})
        return TrainingEnrollmentsAttributes(value if isinstance(value, Mapping) else {})
