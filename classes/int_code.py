
from prettytable import PrettyTable
from dataclasses import dataclass

@dataclass
class Quadruple:
    arg1 : str
    arg2 : str = None
    result : str = None
    op : str = None

    def get_value(self):
        return [
            self.op,
            self.arg1,
            self.arg2,
            self.result
        ]

class IC:

    def __init__(self) -> None:
        self.table = []
        self.row_count = 0

    def add(self, instruction : Quadruple):
        self.table.append(instruction)
        self.row_count += 1

    def get_table(self):
        pt = PrettyTable()
        if len(self.table) > 0:
            pt.field_names = ["op", "arg1", "arg2", "result"]
            vals = [i.get_value() for i in self.table]
            pt.add_rows(vals)
        return pt



