from enum import Enum


class ConstantEnum(Enum):
    def __str__(self):
        return self.name
