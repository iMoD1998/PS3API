from enum import IntEnum

class CEnum(IntEnum):
    @classmethod
    def from_param(cls, self):
        if not isinstance(self, cls):
            raise TypeError
        return self