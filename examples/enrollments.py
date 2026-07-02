from __future__ import annotations

from common import create_client, load_settings, show_page, show_resource, show_user_tags
from psat import EnrollmentStatus
from psat.v0_3_0.reports import TrainingEnrollmentsFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    show_resource("Training enrollments report resource", client.reports.enrollments)

    enrollments = client.reports.enrollments.retrieve(
        TrainingEnrollmentsFilter()
        .with_page(1, 5)
        .add_status(EnrollmentStatus.COMPLETED)
        .enable_user_tags()
    )
    show_page(enrollments)

    for enrollment in enrollments:
        attrs = enrollment.attributes
        print(f"user={attrs.user_email_address}")
        print(f"assignment={attrs.assignment_name}")
        print(f"module={attrs.module_name_user}")
        print(f"status={attrs.module_attempt_status}")
        print(f"removed_reason={attrs.enrollment_removal_reason}")
        show_user_tags(attrs.user_tags)


if __name__ == "__main__":
    main()
