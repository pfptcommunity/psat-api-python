from __future__ import annotations

from common import create_client, load_settings
from psat import EnrollmentStatus
from psat.v0_3_0.reports import TrainingEnrollmentsFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)
    try:
        print("Training enrollments report resource:")
        print(f"  path: {client.reports.enrollments.path}")
        print(f"  url:  {client.reports.enrollments.url}")

        enrollments = client.reports.enrollments.retrieve(
            TrainingEnrollmentsFilter()
            .with_page(1, 5)
            .add_status(EnrollmentStatus.COMPLETED)
            .enable_user_tags()
        ).page
        print(f"status={enrollments.status}")
        print(
            "page="
            f"{enrollments.current_page_number} "
            f"size={enrollments.page_size} "
            f"total_items={enrollments.record_count}"
        )
        print(f"links.self={enrollments.self_link}")
        print(f"links.next={enrollments.next_link}")

        for enrollment in enrollments:
            attrs = enrollment.attributes
            print(f"user={attrs.user_email_address}")
            print(f"assignment={attrs.assignment_name}")
            print(f"module={attrs.module_name_user}")
            print(f"status={attrs.module_attempt_status}")
            print(f"removed_reason={attrs.enrollment_removal_reason}")
            if attrs.user_tags:
                print("user_tags:")
                for name, value in attrs.user_tags.items():
                    print(f"  {name}={value}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
