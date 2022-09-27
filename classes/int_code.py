
from prettytable import PrettyTable

class IC:

    def __init__(self) -> None:
        self.table = {}
        self.order = []
        self.row_count = 0

    def add_instruction(self, arg1 : str, arg2 : str, op : str, result : str):
        # print("Added new int code instr")
        self.table[self.row_count] = {
            "index" : self.row_count,
            "op" : op,
            "arg1" : arg1,
            "arg2" : arg2,
            "result" : result
        }
    
        self.order.append(self.row_count)
        self.row_count += 1
    
    def get_value(self, index : int):
        if index in self.order:
            return self.table[index]
        return None

    def get_table(self):
        pt = PrettyTable()
        if len(self.order) > 0:
            pt.field_names = ["index", "op", "arg1", "arg2", "result"]
            vals = [self.get_value(i).values() for i in self.order]
            pt.add_rows(vals)
        return pt