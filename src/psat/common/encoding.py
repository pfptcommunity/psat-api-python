from __future__ import annotations

from datetime import date, datetime

from klarient import RequestValueEncoder


class PSATValueEncoder(RequestValueEncoder):
    """PSAT request value encoder for booleans and date values."""

    def __init__(self) -> None:
        super().__init__()
        self.register(bool, self._encode_bool)
        self.register(date, self._encode_date)
        self.register(datetime, self._encode_datetime)

    @staticmethod
    def _encode_bool(value: bool) -> str:
        return "TRUE" if value else "FALSE"

    @staticmethod
    def _encode_date(value: date) -> str:
        return value.strftime("%Y-%m-%d")

    @staticmethod
    def _encode_datetime(value: datetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S")
