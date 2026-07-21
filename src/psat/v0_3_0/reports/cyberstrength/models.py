from collections.abc import Mapping

from psat.reports.models import ReportAttributes, ReportRow


class CyberStrengthAttributes(ReportAttributes):
    """Attributes for PSAT CyberStrength report rows."""

    @property
    def assignment_name(self) -> str:
        """Assignment name."""
        return self._string("assignmentname")

    @property
    def assessment_name(self) -> str:
        """Assessment name."""
        return self._string("assessmentname")

    @property
    def assignment_status(self) -> str:
        """Assignment status."""
        return self._string("assignmentstatus")

    @property
    def assessment_status(self) -> str:
        """Assessment status."""
        return self._string("assessmentstatus")

    @property
    def assessment_type(self) -> str:
        """Assessment type."""
        return self._string("assessmenttype")

    @property
    def assignment_start_date(self) -> str:
        """Assignment start date."""
        return self._string("assignmentstartdate")

    @property
    def assignment_due_date(self) -> str:
        """Assignment due date."""
        return self._string("assignmentduedate")

    @property
    def assignment_deleted_date(self) -> str | None:
        """Assignment deleted date when present."""
        return self._optional_string("assignmentdeleteddate")

    @property
    def category(self) -> str | None:
        """CyberStrength category when present."""
        return self._optional_string("category")

    @property
    def category_benchmark_all(self) -> float | None:
        """Benchmark score across all companies for the category."""
        return self._float("categorybenchmarkall")

    @property
    def category_benchmark_industry(self) -> float | None:
        """Benchmark score for the industry category."""
        return self._float("categorybenchmarkindustry")

    @property
    def questions_in_category(self) -> int | None:
        """Number of questions in the category."""
        return self._integer("questionsincategory")

    @property
    def is_ae_enabled(self) -> bool | None:
        """Whether adaptive education is enabled."""
        return self._boolean("isaeenabled")

    @property
    def attempt_date(self) -> str | None:
        """Assessment attempt date when present."""
        return self._optional_string("attemptdate")

    @property
    def user_assignment_status(self) -> str:
        """User assignment status."""
        return self._string("userassignmentstatus")

    @property
    def question_id(self) -> str | None:
        """Question identifier when present."""
        return self._optional_string("questionid")

    @property
    def question_type(self) -> str | None:
        """Question type when present."""
        return self._optional_string("questiontype")

    @property
    def custom_question(self) -> bool | None:
        """Whether the question is custom."""
        return self._boolean("iscustomquestion")

    @property
    def question_text(self) -> str | None:
        """Question text when present."""
        return self._optional_string("questiontext")

    @property
    def selected_answer(self) -> str | None:
        """Selected answer when present."""
        return self._optional_string("selectedanswer")

    @property
    def correct(self) -> bool | None:
        """Whether the selected answer was correct."""
        return self._boolean("correct")

    @property
    def seconds_in_attempt(self) -> int | None:
        """Seconds spent in the attempt."""
        return self._integer("secondsinattempt")

    @property
    def user_correct_on_assignment(self) -> int | None:
        """Number correct for the user on the assignment."""
        return self._integer("usercorrectonassignment")

    @property
    def user_answered_on_assignment(self) -> int | None:
        """Number answered by the user on the assignment."""
        return self._integer("useransweredonassignment")

    @property
    def user_score_on_assignment(self) -> float | None:
        """User score on the assignment."""
        return self._float("userscoreonassignment")

    @property
    def user_removed_from_assignment(self) -> bool | None:
        """Whether the user was removed from the assignment."""
        return self._boolean("userremovedfromassignment")

    @property
    def question_latency(self) -> int | None:
        """Question latency value."""
        return self._integer("questionlatency")

    @property
    def question_date(self) -> str | None:
        """Question date when present."""
        return self._optional_string("questiondate")

    @property
    def assignment_average_score(self) -> float | None:
        """Average score for the assignment."""
        return self._float("assignmentaveragescore")

    @property
    def company_average_score(self) -> float | None:
        """Average company score."""
        return self._float("companyaveragescore")


class CyberStrengthRow(ReportRow[CyberStrengthAttributes]):
    """Typed row from the CyberStrength report."""

    @property
    def attributes(self) -> CyberStrengthAttributes:
        """Typed CyberStrength report attributes."""
        value = self.get("attributes", {})
        return CyberStrengthAttributes(value if isinstance(value, Mapping) else {})
