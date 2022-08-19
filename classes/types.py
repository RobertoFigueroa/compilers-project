from enum import Enum
from dataclasses import dataclass

class VarType(Enum):
    INT = 0
    STRING = 1
    BOOL = 2
    SELF_TYPE = 3
    OBJETC = 4
    IO = 5

@dataclass
class YaplType:
    type: VarType
    value: any = None
    name: str = None

    def __repr__(self):
        if self.name:
            return f'{self.type.name}: {self.name}'
        return self.type.name + (f':{self.value}' if self.value != None else '')