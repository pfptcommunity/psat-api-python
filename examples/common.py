from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SOURCE_ROOT = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SOURCE_ROOT))

from klarient import Resource  # noqa: E402
from psat import Region  # noqa: E402
from psat.v0_3_0 import PSATClient  # noqa: E402


def load_settings(path: str | Path = "settings.json") -> dict[str, Any]:
    settings_path = Path(path)
    if not settings_path.is_absolute():
        settings_path = Path(__file__).resolve().parent / settings_path
    if not settings_path.exists():
        settings_path = Path(__file__).resolve().parents[1] / "settings.json"
    return json.loads(settings_path.read_text())


def create_client(settings: dict[str, Any]) -> PSATClient:
    return PSATClient(
        region=Region(str(settings.get("region", Region.US))),
        api_token=str(settings["api_token"]),
    )


def show_resource(label: str, resource: Resource) -> None:
    # Every Klarient resource knows the URI path it models and the final URL
    # that will be called. Printing both is useful when learning how the Python
    # object tree maps to the REST API tree.
    print(f"{label}:")
    print(f"  path: {resource.path}")
    print(f"  url:  {resource.url}")


def show_page(response: object) -> None:
    print(f"status={getattr(response, 'status')}")
    print(
        "page="
        f"{getattr(response, 'current_page_number')} "
        f"size={getattr(response, 'page_size')} "
        f"total_items={getattr(response, 'record_count')}"
    )
    print(f"links.self={getattr(response, 'self_link')}")
    print(f"links.next={getattr(response, 'next_link')}")


def show_user_tags(tags: object) -> None:
    if not isinstance(tags, dict) or not tags:
        return
    print("user_tags:")
    for name, value in tags.items():
        print(f"  {name}={value}")
