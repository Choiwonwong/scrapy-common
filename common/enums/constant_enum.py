from enum import Enum


class ConstantEnum(Enum):
    def __str__(self):
        return self.name

    # auto() 사용 시 value를 name과 같게 지정
    def _generate_next_value_(name, start, count, last_values):  # noqa
        return name
