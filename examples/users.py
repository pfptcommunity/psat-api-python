from __future__ import annotations

from common import create_client, load_settings
from psat.v0_3_0.reports import UsersFilter


def main() -> None:
    settings = load_settings()
    client = create_client(settings)

    print("Reports root resource:")
    print(f"  path: {client.reports.path}")
    print(f"  url:  {client.reports.url}")
    print("Users report resource:")
    print(f"  path: {client.reports.users.path}")
    print(f"  url:  {client.reports.users.url}")

    users = client.reports.users.retrieve(
        UsersFilter()
        .with_page(1, 5)
        .enable_user_tags()
    )
    print(f"status={users.status}")
    print(
        "page="
        f"{users.current_page_number} "
        f"size={users.page_size} "
        f"total_items={users.record_count}"
    )
    print(f"links.self={users.self_link}")
    print(f"links.next={users.next_link}")

    for user in users:
        attrs = user.attributes
        print(f"user={attrs.user_email_address}")
        print(f"name={attrs.user_first_name} {attrs.user_last_name}")
        print(f"timezone={attrs.timezone}")
        if attrs.user_tags:
            print("user_tags:")
            for name, value in attrs.user_tags.items():
                print(f"  {name}={value}")


if __name__ == "__main__":
    main()
