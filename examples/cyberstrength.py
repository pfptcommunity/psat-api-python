from __future__ import annotations

from common import create_client, load_settings
from psat.v0_3_0.reports import CyberStrengthFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    print("CyberStrength report resource:")
    print(f"  path: {client.reports.cyberstrength.path}")
    print(f"  url:  {client.reports.cyberstrength.url}")

    cyber_strength = client.reports.cyberstrength.retrieve(
        CyberStrengthFilter()
        .with_page(1, 5)
        .enable_user_tags()
    )

    print(f"status={cyber_strength.status}")
    print(
        "page="
        f"{cyber_strength.current_page_number} "
        f"size={cyber_strength.page_size} "
        f"total_items={cyber_strength.record_count}"
    )
    print(f"links.self={cyber_strength.self_link}")
    print(f"links.next={cyber_strength.next_link}")

    for assessment in cyber_strength:
        attrs = assessment.attributes
        print(f"user={attrs.user_email_address}")
        print(f"assignment={attrs.assignment_name}")
        print(f"assessment={attrs.assessment_name}")
        print(f"status={attrs.user_assignment_status}")
        print(f"question={attrs.question_text}")
        if attrs.user_tags:
            print("user_tags:")
            for name, value in attrs.user_tags.items():
                print(f"  {name}={value}")


if __name__ == "__main__":
    main()
