YAPL_OBJECT = {
    "name_type" : "Object",
    "inherits": "Object",
    "attrs": {},
    "methods"   : {
        "abort" : {"type" : "Object", "params" : {}},
        "type_name" : {"type" : "String", "params" : {}},
        "copy" : {"type" : "SELF_TYPE", "params":{}}
    }
}

YAPL_IO = {
    "name_type" : "IO",
    "inherits": "Object",
    "attrs": {},
    "methods": {        
        "out_string": {"type":"SELF_TYPE", "params" : {"x" : "String"}},
        "out_int":{"type": "SELF_TYPE", "params" : {"x" : "Int"}},
        "in_string" : {"type": "String", "params":{}},
        "in_int" : {"type":"Int", "params":{}}
    }
}


YAPL_INT = {
    "name_type" : "Int",
    "inherits": "Object",
    "attrs": {},
    "methods": {}
}

YAPL_STRING = {
    "name_type" : "String",
    "inherits": "Object",
    "attrs": {},
    "methods": {
        "length" : {"type": "Int", "params": {}},
        "concat" : {"type":"String", "params":{}},
        "substr" : {"type" : "String", "params":{"i":"Int", "l":"Int"}}
    }
}


YAPL_BOOL = {
    "name_type" : "Bool",
    "inherits": "Object",
    "attrs": {},
    "methods": {}
}


YAPL_SELF_TYPE = {
    "name_type" : "SELF_TYPE",
    "inherits": "Object",
    "attrs": {},
    "methods": {}
}