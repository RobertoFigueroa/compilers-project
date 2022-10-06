
from prettytable import PrettyTable
from dataclasses import dataclass

@dataclass
class Quadruple:
    arg1 : str = ""
    arg2 : str = ""
    result : str = ""
    op : str = ""

    def get_value(self):
        return [
            self.op,
            self.arg1,
            self.arg2,
            self.result
        ]

    def get_text(self):
        return self.op + self.result + self.arg1 + self.arg2 

    def dump(self):
        return {
            "arg1": self.arg1,
            "arg2" : self.arg2,
            "op" : self.op,
            "result" : self.result
        }

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

    def concat(self, ic_code):
        for q in ic_code.table:
            self.table.append(q)

    def dump(self):
        return [i.dump() for i in self.table]


