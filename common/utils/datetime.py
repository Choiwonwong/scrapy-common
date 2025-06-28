from datetime import datetime

from tzlocal import get_localzone


class CustomDateTime:
    FORMAT_ISO8601_DATETIME_MICRO = "%Y-%m-%dT%H:%M:%S.%f"
    FORMAT_EXECUTION_ID = "%Y%m%d%H%M%S"

    tz = None

    def __init__(self, tz=None):
        self.tz = tz

    def now(self) -> datetime:
        if self.tz is None:
            return datetime.now()
        else:
            return datetime.now(tz=self.tz)

    def get_tz(self, dt: datetime) -> str:
        if self.tz is None:
            return get_localzone().key
        else:
            return self.tz.key

    def transform_started_at(self, dt: datetime) -> str:
        return dt.strftime(self.FORMAT_ISO8601_DATETIME_MICRO)

    def transform_execution_id(self, dt: datetime) -> str:
        return dt.strftime(self.FORMAT_EXECUTION_ID)

    def get_collected_at(self) -> str:
        if self.tz is None:
            now = datetime.now()
        else:
            now = datetime.now(tz=self.tz)
        return now.strftime(self.FORMAT_ISO8601_DATETIME_MICRO)
