from __future__ import annotations

from common import create_client, load_settings
from psat.v0_3_0.reports import PhishingExtendedFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)
    try:
        print("Phishing extended report resource:")
        print(f"  path: {client.reports.phishing_extended.path}")
        print(f"  url:  {client.reports.phishing_extended.url}")

        phishing = client.reports.phishing_extended.retrieve(
            PhishingExtendedFilter()
            .with_page(1, 5)
            .enable_user_tags()
        ).page
        print(f"status={phishing.status}")
        print(
            "page="
            f"{phishing.current_page_number} "
            f"size={phishing.page_size} "
            f"total_items={phishing.record_count}"
        )
        print(f"links.self={phishing.self_link}")
        print(f"links.next={phishing.next_link}")

        for event in phishing:
            attrs = event.attributes
            print(f"user={attrs.user_email_address}")
            print(f"campaign={attrs.campaign_name}")
            print(f"ip={attrs.ip_address}")
            print(f"browser={attrs.browser} {attrs.browser_version}")
            print(f"os={attrs.os} {attrs.os_version}")
            print(f"mobile={attrs.mobile_device_used}")
            print(f"afr={attrs.afr}")
            if attrs.user_tags:
                print("user_tags:")
                for name, value in attrs.user_tags.items():
                    print(f"  {name}={value}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
