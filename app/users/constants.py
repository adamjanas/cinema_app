from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class UserRoleE(ChoiceEnum):
    CLIENT = 1
    RECEPTION = 2
    MANAGER = 3

