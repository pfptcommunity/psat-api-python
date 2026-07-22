from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from psat import Region
from psat.v0_3_0 import PSATClient


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
