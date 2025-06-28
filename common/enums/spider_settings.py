from enum import auto

from common.enums.constant_enum import ConstantEnum


class SystemSettings(ConstantEnum):
    DOMAIN = auto()
    OBJECTIVE = auto()
    STRATEGY = auto()
    MODE = auto()


class SpiderSettings(ConstantEnum):
    DOWNLOAD_DELAY = auto()
