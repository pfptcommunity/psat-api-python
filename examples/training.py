from __future__ import annotations

from common import create_client, load_settings, show_page, show_resource, show_user_tags
from psat import AssignmentStatus
from psat.v0_3_0.reports import TrainingFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    show_resource("Training report resource", client.reports.training)

    training = client.reports.training.retrieve(
        TrainingFilter()
        .with_page(1, 5)
        .add_user_assignment_status(AssignmentStatus.COMPLETED)
        .enable_user_tags()
    )
    show_page(training)

    for attempt in training:
        attrs = attempt.attributes
        print(f"user={attrs.user_email_address}")
        print(f"assignment={attrs.assignment_name}")
        print(f"module={attrs.module_name_user}")
        print(f"status={attrs.module_attempt_status}")
        print(f"score={attrs.module_attempt_score}")
        show_user_tags(attrs.user_tags)


if __name__ == "__main__":
    main()
