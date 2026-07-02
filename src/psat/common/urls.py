from __future__ import annotations

from psat.common.enums import Region


def base_url_for(region: Region | str) -> str:
    if isinstance(region, Region):
        host = region.value
    else:
        host = str(region).removeprefix("https://").removeprefix("http://").rstrip("/")
    return f"https://{host}"
