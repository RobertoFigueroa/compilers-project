from prettytable import PrettyTable


class TypeAlreadyDefined(Exception):
    """Exception raised when trying to add an already defined type."""

    def __init__(self, name_type, message=" class type already defined"):
        self.name_type = name_type
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name_type} -> {self.message}'

class ClassTypeNotFound(Exception):
    def __init__(self, name_type, message=" class not defined"):
        self.name_type = name_type
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name_type} -> {self.message}'


class Errors:

    def __init__(self) -> None:
        self.errors = []
        self.lines = []
    def add_error(self, msg : str, at : int = None) -> None:
        if at:
            self.errors.append(msg + f" near to line {at}")
            self.lines.append(at)
        else:
            self.errors.append(msg)

    def get_errors(self) -> list:
        pt = PrettyTable()
        if len(self.errors) > 0:
            pt.field_names = ["ID", "ERRORS"]
            vals = [[i,j] for i,j in zip(range(1, len(self.errors)+1), self.errors)]
            pt.add_rows(vals)
        return pt

    def dump(self) -> dict:
        return {
            "errors" : self.errors,
            "lines" : self.lines
        }