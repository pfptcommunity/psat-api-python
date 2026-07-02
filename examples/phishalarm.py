from __future__ import annotations

from common import create_client, load_settings, show_page, show_resource, show_user_tags
from psat.v0_3_0.reports import PhishAlarmFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    show_resource("PhishAlarm report resource", client.reports.phishalarm)

    reports = client.reports.phishalarm.retrieve(
        PhishAlarmFilter()
        .with_page(1, 5)
        .enable_user_tags()
    )
    show_page(reports)

    for report in reports:
        attrs = report.attributes
        print(f"user={attrs.user_email_address}")
        print(f"campaign={attrs.campaign_name}")
        print(f"action={attrs.action}")
        print(f"reported={attrs.reported_date}")
        print(f"email_client={attrs.email_client_version}")
        show_user_tags(attrs.user_tags)


if __name__ == "__main__":
    main()
