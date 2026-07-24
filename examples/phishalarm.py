from __future__ import annotations

from common import create_client, load_settings
from psat.v0_3_0.reports import PhishAlarmFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)
    try:
        print("PhishAlarm report resource:")
        print(f"  path: {client.reports.phishalarm.path}")
        print(f"  url:  {client.reports.phishalarm.url}")

        reports = client.reports.phishalarm.retrieve(
            PhishAlarmFilter()
            .with_page(1, 5)
            .enable_user_tags()
        ).page
        print(f"status={reports.status}")
        print(
            "page="
            f"{reports.current_page_number} "
            f"size={reports.page_size} "
            f"total_items={reports.record_count}"
        )
        print(f"links.self={reports.self_link}")
        print(f"links.next={reports.next_link}")

        for report in reports:
            attrs = report.attributes
            print(f"user={attrs.user_email_address}")
            print(f"campaign={attrs.campaign_name}")
            print(f"action={attrs.action}")
            print(f"reported={attrs.reported_date}")
            print(f"email_client={attrs.email_client_version}")
            if attrs.user_tags:
                print("user_tags:")
                for name, value in attrs.user_tags.items():
                    print(f"  {name}={value}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
