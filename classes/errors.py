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
