from __future__ import annotations

from common import create_client, load_settings, show_page, show_resource, show_user_tags
from psat.v0_3_0.reports import PhishingExtendedFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    show_resource("Phishing extended report resource", client.reports.phishing_extended)

    phishing = client.reports.phishing_extended.retrieve(
        PhishingExtendedFilter()
        .with_page(1, 5)
        .enable_user_tags()
    )
    show_page(phishing)

    for event in phishing:
        attrs = event.attributes
        print(f"user={attrs.user_email_address}")
        print(f"campaign={attrs.campaign_name}")
        print(f"ip={attrs.ip_address}")
        print(f"browser={attrs.browser} {attrs.browser_version}")
        print(f"os={attrs.os} {attrs.os_version}")
        print(f"mobile={attrs.mobile_device_used}")
        print(f"afr={attrs.afr}")
        show_user_tags(attrs.user_tags)


if __name__ == "__main__":
    main()
