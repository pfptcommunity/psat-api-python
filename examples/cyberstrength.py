from __future__ import annotations

from common import create_client, load_settings, show_page, show_resource, show_user_tags
from psat.v0_3_0.reports import CyberStrengthFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    show_resource("CyberStrength report resource", client.reports.cyberstrength)

    cyber_strength = client.reports.cyberstrength.retrieve(
        CyberStrengthFilter()
        .with_page(1, 5)
        .enable_user_tags()
    )

    show_page(cyber_strength)

    for assessment in cyber_strength:
        attrs = assessment.attributes
        print(f"user={attrs.user_email_address}")
        print(f"assignment={attrs.assignment_name}")
        print(f"assessment={attrs.assessment_name}")
        print(f"status={attrs.user_assignment_status}")
        print(f"question={attrs.question_text}")
        show_user_tags(attrs.user_tags)


if __name__ == "__main__":
    main()
