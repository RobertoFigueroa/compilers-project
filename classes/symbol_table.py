from prettytable import PrettyTable
from classes.errors import TypeAlreadyDefined, ClassTypeNotFound
from utils.YAPLDefs import *

"""
La tabla de tipos tendrá la siguiente estructura:
    NAME_TYPE | INHERTS | ATTRS | METHODS
    NAME_TYPE: str <determina el tipo de clase>
    INHERTIS: str <determina si tiene herencia y quién es su herencia>
    ATTRS: dict {name: type, name2, type ...} <diccionario los atributos con sus tipos>
    METHODS: dict -> {methodsName : {type: 'Int', params: {name : 'int'}}} <almacena los métodos de una clase y la información de la firma>
La tabla de símbolos tendrá objetos de tipo símbolo que
almacenarán la siguiente información:
    NAME | TYPE | BELONGS_TO
    NAME:str <nombre de la variable>
    TYPE:str <determina el tipo de dicha variable>
    BELONGS_TO:str <determina el nombre de la clase a la que pertenece dicha variable>
"""

class TypeTable:

    def __init__(self) -> None:
        self.table = []
        self.key_name_types = []

    def generate_YAPL_types(self):
        #self.add_type(YAPL_OBJECT["name_type"], YAPL_OBJECT["inherits"], YAPL_OBJECT["attrs"], YAPL_OBJECT["methods"])
        self.table.append(YAPL_OBJECT)
        self.add_type(YAPL_IO["name_type"], YAPL_IO["inherits"], YAPL_IO["attrs"], YAPL_IO["methods"])
        self.add_type(YAPL_INT["name_type"], YAPL_INT["inherits"], YAPL_INT["attrs"], YAPL_INT["methods"])
        self.add_type(YAPL_BOOL["name_type"], YAPL_BOOL["inherits"], YAPL_BOOL["attrs"], YAPL_BOOL["methods"])
        self.add_type(YAPL_STRING["name_type"], YAPL_STRING["inherits"], YAPL_STRING["attrs"], YAPL_STRING["methods"])
        self.add_type(YAPL_SELF_TYPE["name_type"], YAPL_SELF_TYPE["inherits"], YAPL_SELF_TYPE["attrs"], YAPL_SELF_TYPE["methods"])
        

    def add_type(self, name_type : str, 
                inherits: str = "Object", attrs: dict = {}, methods : dict = {}) -> None:
        if not self.exists(name_type):
            if self.exists(inherits):
                self.table.append(
                    {
                        "name_type" : name_type,
                        "inherits": inherits,
                        "attrs": attrs,
                        "mothods": methods
                    }
                )
                self.key_name_types.append(name_type)
            else:
                raise ClassTypeNotFound(name_type)
        else:
            raise TypeAlreadyDefined(name_type)

        

    def find_symbol():
        pass

    def get_symbol():
        pass

    def exists(self, name_type):
        if name_type in self.key_name_types:
            return True
        else:
            return False

