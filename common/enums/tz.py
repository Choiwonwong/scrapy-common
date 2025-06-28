from enum import Enum
from zoneinfo import ZoneInfo


class TimeZone(Enum):
    KST = ZoneInfo("Asia/Seoul")
    UTC = ZoneInfo("UTC")
    PST = ZoneInfo("America/Los_Angeles")
