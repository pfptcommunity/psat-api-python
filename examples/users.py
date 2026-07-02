from __future__ import annotations

from common import create_client, load_settings, show_page, show_resource, show_user_tags
from psat.v0_3_0.reports import UsersFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    show_resource("Reports root resource", client.reports)
    show_resource("Users report resource", client.reports.users)

    users = client.reports.users.retrieve(
        UsersFilter()
        .with_page(1, 5)
        .enable_user_tags()
    )
    show_page(users)

    for user in users:
        attrs = user.attributes
        print(f"user={attrs.user_email_address}")
        print(f"name={attrs.user_first_name} {attrs.user_last_name}")
        print(f"timezone={attrs.timezone}")
        show_user_tags(attrs.user_tags)


if __name__ == "__main__":
    main()
