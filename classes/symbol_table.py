from prettytable import PrettyTable


class Symbol:

    def __init__(self, name) -> None:
        self.name



class SymbolTable:

    def __init__(self) -> None:
        self.table = []


    def add_symbol():
        pass


class AttributeSymbol(Symbol):

    def __init__(self, name, sym_type, scope, belongs_to) -> None:
        super().__init__(name)
        self.type = sym_type
        self.scope = scope
        self.belongs_to = belongs_to
    

class FuncSymbol(AttributeSymbol):

    def __init__(self, name, sym_type, scope, belongs_to, params) -> None:
        super().__init__(name, sym_type, scope, belongs_to)
        self.params = params

class ClassSymbol(Symbol):

    def __init__(self, name, inherits) -> None:
        super().__init__(name)
        self.inherits = inherits


class AttributeTable:

    def __init__(self) -> None:
        self.table = []


    def add(self, name, sym_type, scope, belongs_to):

        self.table.append({
            'name' : name,
            'type': sym_type,
            'scope' : scope,
            'belongs_to' : belongs_to
        })

    def get_table(self) -> str:
        pt = PrettyTable()
        if len(self.table) > 0:
            pt.field_names = list(self.table[0].keys())
            vals = [list(i.values()) for i in self.table]
            pt.add_rows(vals)
        return pt



class FuncTable:

    def __init__(self) -> None:
        self.table = []

    def add(self, name, params, scope, ret_type, belongs_to):
        self.table.append({
            'name' : name,
            'params': params,
            'type': ret_type,
            'scope' : scope,
            'belongs_to' : belongs_to
        })

    def get_table(self) -> str:
        pt = PrettyTable()
        if len(self.table) > 0:
            pt.field_names = list(self.table[0].keys())
            vals = [list(i.values()) for i in self.table]
            pt.add_rows(vals)
        return pt

class ClassTable:

    def __init__(self) -> None:
        self.table = []

    def add(self, name, inherits):

        self.table.append({
            'name': name,
            'inherits': inherits
        })


    def get_table(self) -> str:
        pt = PrettyTable()
        if len(self.table) > 0:
            pt.field_names = list(self.table[0].keys())
            vals = [list(i.values()) for i in self.table]
            pt.add_rows(vals)
        return pt

    

