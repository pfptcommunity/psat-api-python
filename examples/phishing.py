from __future__ import annotations

from common import create_client, load_settings, show_page, show_resource, show_user_tags
from psat.v0_3_0.reports import PhishingFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    show_resource("Phishing report resource", client.reports.phishing)

    phishing = client.reports.phishing.retrieve(
        PhishingFilter()
        .with_page(1, 5)
        .enable_user_tags()
    )

    show_page(phishing)

    for event in phishing:
        attrs = event.attributes
        print(f"user={attrs.user_email_address}")
        print(f"campaign={attrs.campaign_name}")
        print(f"event={attrs.event_type}")
        print(f"template={attrs.template_subject}")
        print(f"archived={attrs.assessment_archived}")
        show_user_tags(attrs.user_tags)


if __name__ == "__main__":
    main()
