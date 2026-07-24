from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from klarient import PagedResponse
from psat import AssignmentStatus, EnrollmentStatus, Region
from psat.v0_3_0 import PSATClient
from psat.v0_3_0.reports import (
    CyberStrengthFilter,
    PhishAlarmFilter,
    PhishingExtendedFilter,
    PhishingFilter,
    TrainingEnrollmentsFilter,
    TrainingFilter,
    UsersFilter,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_settings() -> dict[str, Any]:
    for path in (
            PROJECT_ROOT / "settings.json",
            PROJECT_ROOT / "examples" / "settings.json",
            Path(__file__).resolve().parent / "settings.json",
    ):
        if path.exists():
            return json.loads(path.read_text())
    raise FileNotFoundError("settings.json was not found")


def create_client(settings: dict[str, Any]) -> PSATClient:
    return PSATClient(
        region=Region(str(settings.get("region", Region.US))),
        api_token=str(settings["api_token"]),
    )


def check(name: str, call: Callable[[], PagedResponse[Any]]) -> bool:
    try:
        result = call()
        page = result.page
    except Exception as exc:
        print(f"FAIL {name}: {type(exc).__name__}: {exc}")
        return False

    print(
        f"PASS {name}: "
        f"status={page.status} "
        f"page={page.current_page_number} "
        f"size={page.page_size} "
        f"items={len(page.data)} "
        f"total={page.record_count}"
    )
    print(f"  self={page.self_link}")
    print(f"  next={page.next_link}")
    if page.data:
        row = page.data[0]
        attributes = getattr(row, "attributes", {})
        keys = list(attributes.keys())[:8] if isinstance(attributes, dict) else []
        print(f"  first_row_type={getattr(row, 'type', '')} attributes={keys}")
    return True


def main() -> int:
    settings = load_settings()
    client = create_client(settings)
    ok = True

    try:
        print("PSAT Reporting API live smoke test")
        print(f"reports_path={client.reports.path}")
        print(f"reports_url={client.reports.url}")

        # GET https://{region-host}/api/reporting/v0.3.0/cyberstrength
        ok &= check(
            "reports.cyberstrength",
            lambda: client.reports.cyberstrength.retrieve(
                CyberStrengthFilter()
                .with_page(1, 5)
                .enable_user_tags()
            ),
        )

        # GET https://{region-host}/api/reporting/v0.3.0/trainingenrollments
        ok &= check(
            "reports.enrollments",
            lambda: client.reports.enrollments.retrieve(
                TrainingEnrollmentsFilter()
                .with_page(1, 5)
                .add_status(EnrollmentStatus.COMPLETED)
                .enable_user_tags()
            ),
        )

        # GET https://{region-host}/api/reporting/v0.3.0/phishalarm
        ok &= check(
            "reports.phishalarm",
            lambda: client.reports.phishalarm.retrieve(
                PhishAlarmFilter()
                .with_page(1, 5)
                .enable_user_tags()
            ),
        )

        # GET https://{region-host}/api/reporting/v0.3.0/phishing
        ok &= check(
            "reports.phishing",
            lambda: client.reports.phishing.retrieve(
                PhishingFilter()
                .with_page(1, 5)
                .enable_user_tags()
            ),
        )

        # GET https://{region-host}/api/reporting/v0.3.0/phishing_extended
        ok &= check(
            "reports.phishing_extended",
            lambda: client.reports.phishing_extended.retrieve(
                PhishingExtendedFilter()
                .with_page(1, 5)
                .enable_user_tags()
            ),
        )

        # GET https://{region-host}/api/reporting/v0.3.0/training
        ok &= check(
            "reports.training",
            lambda: client.reports.training.retrieve(
                TrainingFilter()
                .with_page(1, 5)
                .add_user_assignment_status(AssignmentStatus.COMPLETED)
                .enable_user_tags()
            ),
        )

        # GET https://{region-host}/api/reporting/v0.3.0/users
        ok &= check(
            "reports.users",
            lambda: client.reports.users.retrieve(
                UsersFilter()
                .with_page(1, 5)
                .enable_user_tags()
            ),
        )
    finally:
        client.close()

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
