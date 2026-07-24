from __future__ import annotations

from common import create_client, load_settings
from psat import AssignmentStatus
from psat.v0_3_0.reports import TrainingFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)
    try:
        print("Training report resource:")
        print(f"  path: {client.reports.training.path}")
        print(f"  url:  {client.reports.training.url}")

        training = client.reports.training.retrieve(
            TrainingFilter()
            .with_page(1, 5)
            .add_user_assignment_status(AssignmentStatus.COMPLETED)
            .enable_user_tags()
        ).page
        print(f"status={training.status}")
        print(
            "page="
            f"{training.current_page_number} "
            f"size={training.page_size} "
            f"total_items={training.record_count}"
        )
        print(f"links.self={training.self_link}")
        print(f"links.next={training.next_link}")

        for attempt in training:
            attrs = attempt.attributes
            print(f"user={attrs.user_email_address}")
            print(f"assignment={attrs.assignment_name}")
            print(f"module={attrs.module_name_user}")
            print(f"status={attrs.module_attempt_status}")
            print(f"score={attrs.module_attempt_score}")
            if attrs.user_tags:
                print("user_tags:")
                for name, value in attrs.user_tags.items():
                    print(f"  {name}={value}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
