from cgitb import handler
from prettytable import PrettyTable
from classes.YAPLDefs import *
from dist.YAPL.YAPLVisitor import YAPLVisitor
from classes.errors import Errors

"""
La tabla de tipos tendrá la siguiente estructura:
    NAME_TYPE | INHERTS | ATTRS | METHODS
    NAME_TYPE: str <determina el tipo de clase>
    INHERTIS: str <determina si tiene herencia y quién es su herencia>
    ATTRS: dict {name: type, name2, type ...} <diccionario los atributos con sus tipos>
    METHODS: dict -> {methodName : {type: 'Int', params: {name : 'int'}}} <almacena los métodos de una clase y la información de la firma>
La tabla de símbolos tendrá objetos de tipo símbolo que
almacenarán la siguiente información:
    NAME | TYPE | BELONGS_TO
    NAME:str <nombre de la variable>
    TYPE:str <determina el tipo de dicha variable>
    BELONGS_TO:str <determina el nombre de la clase a la que pertenece dicha variable>
"""


class TypeElement(object): #AKA a Class

    def __init__(self, name_type, inherits="Object", attrs = None, methods=None) -> None:
        self.cols = ["name", "inherits", "attrs", "methods"]
        self.name_type = name_type # ""
        self.inherits = inherits # ""
        self.attributes = attrs if attrs else dict() # {name : type}
        self.methods = methods if methods else dict() # {methodName : {"type":"", "params":[]}}

    def add_attribute(self, attr_name : str, _type : str, parent : str):
        if not attr_name in list(self.attributes.keys()):
            self.attributes[attr_name] = _type
        else:
            print("Attribute already defined, overwritting ...")

    def add_method(self, name : str, _type : str, params : dict):
        if not name in list(self.methods.keys()):
            self.methods[name] = {
                "type" : _type,
                "params" : params
            }
        else:
            print("Method already defined, overwritting ...")

    def get_values(self):
        return [
            self.name_type,
            self.inherits,
            self.attributes,
            list(self.methods.keys())
        ]

    def exists_method(self, method_name : str) -> bool:
        if method_name in self.methods.keys():
            return True
        return False

    def find_method(self, method_name : str) -> dict or str :
        if method_name in self.methods.keys():
            return self.methods[method_name]
        else:
            return 'Error'

class TypeTable(object):

    def __init__(self, error_handler : Errors) -> None:
        self.table = []
        self.generate_YAPL_types()
        self.error_handler = error_handler


    def generate_YAPL_types(self):
        self.table.append(TypeElement(YAPL_OBJECT["name_type"], YAPL_OBJECT["inherits"], YAPL_OBJECT["attrs"], YAPL_OBJECT["methods"]))
        self.table.append(TypeElement(YAPL_IO["name_type"], YAPL_IO["inherits"], YAPL_IO["attrs"], YAPL_IO["methods"]))
        self.table.append(TypeElement(YAPL_INT["name_type"], YAPL_INT["inherits"], YAPL_INT["attrs"], YAPL_INT["methods"]))
        self.table.append(TypeElement(YAPL_STRING["name_type"], YAPL_STRING["inherits"], YAPL_STRING["attrs"], YAPL_STRING["methods"]))
        self.table.append(TypeElement(YAPL_BOOL["name_type"], YAPL_BOOL["inherits"], YAPL_BOOL["attrs"], YAPL_BOOL["methods"]))
        self.table.append(TypeElement(YAPL_SELF_TYPE["name_type"], YAPL_SELF_TYPE["inherits"], YAPL_SELF_TYPE["attrs"], YAPL_SELF_TYPE["methods"]))

    def check_main(self):
        class_ = False
        method = False
        for i in self.table:
            if i.name_type == "Main":
                class_ = True
                if "main" in i.methods:
                    method = True
        
        return (class_, method)

    def update_attributes(self, name:str, _type:str, belongs_to : str) -> None: # Attribute: {name: "", type:""}
        #TODO: check if exists
        for i in self.table:
            if i.name_type == belongs_to:
                i.add_attribute(name, _type, belongs_to)


    def get_element(self, name : str):
        for i in self.table:
            if i.name_type == name:
                return i

    def update_methods(self, method_name:str, _type : str, params : dict, belongs_to:str) -> None:

        for i in self.table:
            if i.name_type == belongs_to:
                i.add_method(method_name, _type, params)


    def add_type(self, type_object : TypeElement) -> None:
        if not self.exists(type_object.name_type):
            if self.exists(type_object.inherits):
                self.table.append(type_object)
            else:
                self.error_handler.add_error(f"Class {type_object.inherits}, not defined, inherits from {type_object.name_type}")
        else:
            self.error_handler.add_error(f"Class {type_object.name_type} already defined")

    def exists(self, name_type):
        for i in self.table:
            if i.name_type == name_type:
                return True
        else:
            return False

    def check_method(self, method_name : str, current_class: str):
        _class = self.get_element(current_class)
        if _class:
            if _class.find_method(method_name) != 'Error':
                return _class.find_method(method_name)
            else:
                return self.check_inherit_method(method_name, current_class)
        return "Error"
        # for i in self.table:
        #     if i.exists_method(method_name):
        #         return i.find_method(method_name)
        # return None
    
    def check_specific_method(self, method_name:str, current_class : str, exp_class : str):# Current class is typeid
        _class = self.get_element(current_class)
        print("For class", current_class)
        if _class:
            if self.has_parent(exp_class, current_class) == None:
                return "Error1"
            return _class.find_method(method_name)
        return "Error2"

    def check_inherit_method(self, method_name : str, current_class : str) -> dict:
        _class = self.get_element(current_class)
        found_method = False
        inh = _class.inherits
        while not found_method:
            if inh == "Object":
                obj = self.get_element("Object")
                return obj.find_method(method_name)
            e = self.get_element(inh)
            method = e.find_method(method_name)
            if method != "Error":
                return method
            inh = e.inherits
        
        

    def has_parent(self, child : str, parent : str) -> (dict or None):
        found_object_parent = False
        print("Searching", child, parent)
        c = child
        p = self.get_element(c)
        if not p:
            return "Error"
        if p.inherits == parent:
            return self.get_element(parent)
        while not found_object_parent:
            element = self.get_element(p)
            if not element:
                return "Error"
            inh = element.inherits
            if inh == parent:
                return element
            c = p
            p = element.inherits
            if p == "Object":
                found_object_parent = True
        return None

    def get_table(self) -> str:
        pt = PrettyTable()
        if len(self.table) > 0:
            pt.field_names = self.table[0].cols
            vals = [i.get_values() for i in self.table]
            pt.add_rows(vals)
        return pt

class Symbol:

    def __init__(self,name : str, _type : str) -> None:
        self.name = name
        self._type = _type
    
    def __repr__(self) -> str:
        return self.name
        
    def __eq__(self, other: object) -> bool:
        if type(other) == str:
            if other == self.name:
                return True
            else:
                return False
        if other.name == self.name:
            return True
        else:
            return False


class SymbolTable:

    def __init__(self, error_handler:Errors, context : int) -> None:
        self.table = []
        self.error_handler = error_handler
        self._context = context

    def add_symbol(self, symbol : Symbol) -> None:
        if symbol.name in self.table:
            self.error_handler.add_error(f"Symbol {symbol.name} already defined")
        else:
            self.table.append(symbol)


    def find_symbol(self, symbol : Symbol) -> Symbol:

        for i in self.table:
            if i.name == symbol.name:
                return i
        
        return None

    def get_symbol(self, name) -> Symbol:
        for i in self.table:
            if i.name == name:
                return i

    def get_symbol_type(self, name) -> str:
        for i in self.table:
            if i.name == name:
                return i._type
        self.error_handler.add_error(f"Symbol not found in current scope {name}")
        return "Error"


    def exists(self, name :str) -> bool:
        for i in self.table:
            if i.name == name:
                return True
            
        return False

    def __repr__(self) -> str:
        return str(self.table)
    
