from abc import ABC, ABCMeta
from enum import Enum, EnumMeta


MultiValueEnumMeta = type('MultiValueEnumMeta', (ABCMeta, EnumMeta), {})

class ABCEnumMeta(ABCMeta, EnumMeta):
    pass

class MultiValueEnum(ABC, Enum, metaclass=ABCEnumMeta):
    def __new__(cls, *values):
        obj = object.__new__(cls)
        for other_val in values[1:]:
            cls._value2member_map_[other_val] = obj
        obj._value_ = values[0]
        obj._values = values
        return obj
    
    def __getitem__(self, idx):
        return self._values[idx]