from antlr4 import *
from dist.YAPL.YAPLLexer import YAPLLexer
from dist.YAPL.YAPLParser import YAPLParser
from dist.YAPL.YAPLVisitor import YAPLVisitor
from classes.symbol_table import TypeTable, SymbolTable, TypeElement, Symbol
from classes.stack import Stack
from classes.errors import Errors

TYPE_INT = "Int"
TYPE_BOOL = "Bool"
TYPE_STRING = "String"
OBJECT = "Object"
ERROR = "Error"

ANTLR = "/usr/local/lib/antlr-4.10.1-complete.jar"
GRAMMAR_NAME = "YAPL"
ANTLR_FLAGS = "-no-visitor -no-listener"
OUT_DIR = "jdist"
START_RULE = "program"
CL_FILE = "input/cool.cl"
GRUN_FLAGS = "-gui -tokens"
JAVA_COM = "java -Xmx500M -cp"
PKG = "org.antlr.v4.Tool"
G_PKG = "org.antlr.v4.gui.TestRig"
CLASSPATH = ".:/usr/local/lib/antlr-4.10.1-complete.jar:.:/usr/local/lib/antlr-4.10.1-complete.jar:"
#antlr4 -Dlanguage=Python3 YAPL/YAPL.g4 -visitor -o dist

class InitCustomVisitor(YAPLVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.errors = Errors()
        self.types_table = TypeTable(self.errors)



    def visitClassDefine(self, ctx: YAPLParser.ClassDefineContext):
        self.class_def = ctx.TYPEID()[0].getText()
        if ctx.INHERITS():
            _type = TypeElement(ctx.TYPEID()[0].getText(), ctx.TYPEID()[1].getText())
            self.types_table.add_type(_type)
        else:
            _type = TypeElement(ctx.TYPEID()[0].getText())
            self.types_table.add_type(_type)
        return super().visitClassDefine(ctx)

    def visitProperty(self, ctx: YAPLParser.PropertyContext):
        belongs_to = ctx.parentCtx.TYPEID()[0].getText()
        self.types_table.update_attributes(ctx.OBJECTID().getText(), ctx.TYPEID().getText(), belongs_to)
        return super().visitProperty(ctx)

    def visitMethod(self, ctx: YAPLParser.MethodContext):        
        params = ctx.formal()
        tparams = {}
        belongs_to = ctx.parentCtx.TYPEID()[0].getText()
        for i in params:
            tparams[i.OBJECTID().getText()] = i.TYPEID().getText() 
        self.types_table.update_methods(ctx.OBJECTID().getText(), ctx.TYPEID().getText(), tparams, belongs_to)
        return super().visitMethod(ctx)


class CustomVisitor(YAPLVisitor):

    def __init__(self) -> None:
        super().__init__()
        self.errors = Errors()
        self.symbol_table = Stack()
        self.types_table = TypeTable(self.errors)
        self.class_def = None

    def visitProgram(self, ctx: YAPLParser.ProgramContext):
        c, m = self.types_table.check_main()
        if not c:
            self.errors.add_error("No Main class found")
        if not m:
            self.errors.add_error("No main method found")

        return super().visitProgram(ctx)

    def exist_till_global(self, name : str) -> any :
        temp_stack = Stack()
        class_found = False
        result = None
        while not class_found:
            t = self.symbol_table.pop()
            temp_stack.push(t)
            # print("Searching in ", t._context)
            if self.symbol_table.is_empty():
                result = None
                class_found = True
            if t.exists(name):
                class_found = True
                result = t.get_symbol_type(name)
                # print("founded!", name, result)
        while not temp_stack.is_empty():
            self.symbol_table.push(temp_stack.pop())
        return result

    def exists_local_global_scope(self, name : str) -> any:
        if self.symbol_table.top()._context == 2:
            return self.exist_till_global(name)
        local = self.symbol_table.pop()                
        if local.exists(name): # Check in local scope
            symb = local.get_symbol_type(name)
            self.symbol_table.push(local)
            return symb
        if self.symbol_table.top().exists(name): # Check in global scope
            symb = self.symbol_table.top().get_symbol_type(name)
            self.symbol_table.push(local)
            return symb
        self.symbol_table.push(local)
        return None

    def visitLetIn(self, ctx: YAPLParser.LetInContext):
        self.symbol_table.push(SymbolTable(self.errors, 2))
        ids = [i.getText() for i in ctx.OBJECTID()]
        types = [i.getText() for i in ctx.TYPEID()]
        if len(ids) == 0:
            self.errors.add_error("Expression Let must have at least one assigment", ctx.start.line)
        
        for i,t in zip(ids, types):
            self.symbol_table.top().add_symbol(Symbol(i, t))
        # print("This is last in expre child nodes in let", exprChildrenNodes[-1])

        return self.visit(ctx.expression()[-1])

    def visitClassDefine(self, ctx: YAPLParser.ClassDefineContext): # Class definition
        self.class_def = ctx.TYPEID()[0].getText()
        self.symbol_table.clear()
        self.symbol_table.push(SymbolTable(self.errors, 0))
        # if self.symbol_table.is_empty():
        #     self.symbol_table.push(SymbolTable(self.error, 0))
        # else:
        #     _exit = False
        #     while not self.symbol_table.is_empty() or _exit:
        #         sym_table = self.symbol_table.pop()
        #         if sym_table.context == 0:
        #             _exit = True
        
        return super().visitClassDefine(ctx)    

    

    def visitProperty(self, ctx: YAPLParser.PropertyContext): # Attributes of a class
        if ctx.expression():
            expr = self.visit(ctx.expression())
            if type(expr) == list:
                childNode = [self.visit(i) for i in expr]
                if childNode[0] != ctx.TYPEID().getText():
                    self.errors.add_error(f"Invalid assigment in property of class {self.class_def}, {ctx.TYPEID().getText()} type expected {childNode[0]} found", ctx.start.line)
            else:
                if expr != ctx.TYPEID().getText():
                    self.errors.add_error(f"Invalid assigment in property of class {self.class_def}, {ctx.TYPEID().getText()} type expected {expr} found", ctx.start.line)
        self.symbol_table.top().add_symbol(Symbol(ctx.OBJECTID().getText(), ctx.TYPEID().getText()))
        return ctx.TYPEID().getText()

    def visitParentheses(self, ctx: YAPLParser.ParenthesesContext):
        return self.visit(ctx.expression())

    def visitBlock(self, ctx: YAPLParser.BlockContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        return childrenNodes[-1]
        #return self.visit(ctx.expression()[-1])
    
    def visitMethod(self, ctx: YAPLParser.MethodContext): # Function within a class
        if self.symbol_table.is_empty():
            self.errors.add_error(f"Function declaration out of a parent class {ctx.OBJECTID().getText()}", ctx.start.line)
        if self.symbol_table.top()._context == 0: # Means is the first method found in class
            self.symbol_table.push(SymbolTable(self.errors, 1))
        else:
            class_found = True
            while self.symbol_table.is_empty() or class_found:
                sym_table = self.symbol_table.pop()
                if sym_table._context == 0: # Means it found parent class
                    class_found = not class_found
                    self.symbol_table.push(sym_table)
                    self.symbol_table.push(SymbolTable(self.errors, 1))
            if self.symbol_table.is_empty():
                print("Fatal error, parent class not found")
                self.symbol_table.push(SymbolTable(self.errors, 1))
        params = ctx.formal()

        for i in params:
            # print("Adding", i.OBJECTID().getText(), i.TYPEID().getText())
            self.symbol_table.top().add_symbol(Symbol(i.OBJECTID().getText(), i.TYPEID().getText()))
        # tparams["type"] = ctx.TYPEID().getText()
        
        # self.symbol_table.top().add_symbol(Symbol(ctx.OBJECTID().getText(), ctx.TYPEID().getText()))
        _type = self.visit(ctx.expression()) # Type of return
        if ctx.TYPEID().getText() == TYPE_STRING and _type == TYPE_INT:
            self.errors.add_error(f"Erorr in function, type {ctx.TYPEID().getText()} expected but {_type} returned", ctx.start.line)
        if ctx.TYPEID().getText() == TYPE_INT and _type == TYPE_BOOL:
            self.errors.add_error(f"Erorr in function, type {ctx.TYPEID().getText()} expected but {_type} returned", ctx.start.line)
        if ctx.TYPEID().getText() == "SELF_TYPE":
            return _type
        if _type != ctx.TYPEID().getText():
            if self.types_table.has_parent(_type, ctx.TYPEID().getText()):
                return ctx.TYPEID().getText()
            self.errors.add_error(f"Erorr in function, type {ctx.TYPEID().getText()} expected but {_type} returned", ctx.start.line)
        return _type


    def visitAssignment(self, ctx: YAPLParser.AssignmentContext):
        name = ctx.OBJECTID().getText()
        # Check if exists in scope
        type_ = self.exists_local_global_scope(name)
        right_side = self.visit(ctx.expression())

        if type_:
            if type_ == right_side:
                return type_
            elif type_ == TYPE_BOOL and right_side == TYPE_INT:
                return type_
            elif type_ == TYPE_INT and right_side == TYPE_BOOL:
                return type_
            if type_ != right_side:
                if type_ == TYPE_INT and right_side == TYPE_STRING:
                    self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side} can't found inhertiance relation", ctx.start.line)
                    return ERROR
                if type_ == TYPE_STRING and right_side == TYPE_INT:
                    self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side} can't found inhertiance relation", ctx.start.line)
                    return ERROR
                if self.types_table.has_parent(right_side, type_):
                    return type_
                else:
                    self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side} can't found inhertiance relation", ctx.start.line)
            else:
                self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side}", ctx.start.line)
        
        else:
            self.errors.add_error(f"Error in assignment, no variable {name} in the scope", ctx.start.line)
            return ERROR
    
    def visitId(self, ctx: YAPLParser.IdContext):
        value = ctx.OBJECTID().getText()
        # Check if exists in local context
        # if self.symbol_table.top().exists(value): 
        #     return self.symbol_table.top().get_symbol_type(value)
        # # Check in global context

        if value == "self":
            return self.class_def

        result = self.exists_local_global_scope(value)
        if result:
            return result
        else:
            self.errors.add_error(f"Invalid id, not defined in scope {value}", ctx.start.line)
            return ERROR
        # local_scope = self.symbol_table.pop()
        # if self.symbol_table.top().exists(value):
        #     _type = self.symbol_table.top().get_symbol_type(value)
        #     self.symbol_table.push(local_scope)
        #     return _type


    def visitIf(self, ctx: YAPLParser.IfContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_BOOL or childrenNodes[0] == TYPE_INT:
            if childrenNodes[1] == childrenNodes[2]:
                return childrenNodes[1]
            else:
                return OBJECT        
        else:
            self.errors.add_error(f"Invalid expression on if statement {childrenNodes[0]} found, expected Bool type", ctx.start.line)
            return ERROR

    def visitWhile(self, ctx: YAPLParser.WhileContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_BOOL:
            return TYPE_BOOL
        else:
            self.errors.add_error(f"Invalid expression on while statement, {childrenNodes[0]} found, expected Bool type", ctx.start.line)
            return ERROR

    def visitAdd(self, ctx: YAPLParser.AddContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            return TYPE_INT
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} + {childrenNodes[1]} types missmatch", ctx.start.line)
            return ERROR

    def visitMinus(self, ctx: YAPLParser.MinusContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            return TYPE_INT
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} - {childrenNodes[1]} types missmatch", ctx.start.line)
            return ERROR

    def visitMultiply(self, ctx: YAPLParser.MultiplyContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            return TYPE_INT
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} * {childrenNodes[1]} types missmatch", ctx.start.line)
            return ERROR
    
    def visitDivision(self, ctx: YAPLParser.DivisionContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            return TYPE_INT
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} * {childrenNodes[1]} types missmatch", ctx.start.line)
            return ERROR

    def visitBoolNot(self, ctx: YAPLParser.BoolNotContext):
        expr = self.visit(ctx.expression())
        if type(expr) == list:
            childNode = [self.visit(i) for i in expr]
            if childNode[0] == TYPE_BOOL:
                return TYPE_BOOL
            else:
                self.errors.add_error(f"Invalid expression ~{childNode[0]} types missmatch", ctx.start.line)
        else:
            if expr == TYPE_BOOL:
                return TYPE_BOOL
            else:
                self.errors.add_error(f"Invalid expression ~{expr} types missmatch", ctx.start.line)
                return ERROR

    def visitNegative(self, ctx: YAPLParser.NegativeContext):
        expr = self.visit(ctx.expression())
        if type(expr) == list:
            childNode = [self.visit(i) for i in expr]
            if childNode[0] == TYPE_INT:
                return TYPE_INT
            else:
                self.errors.add_error(f"Invalid expression ~{childNode[0]} types missmatch", ctx.start.line)
        else:
            if expr == TYPE_INT:
                return TYPE_INT
            else:
                self.errors.add_error(f"Invalid expression ~{expr} types missmatch", ctx.start.line)
                return ERROR

    def visitEqual(self, ctx: YAPLParser.EqualContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == childrenNodes[1]:
            return TYPE_BOOL
        else:
            self.errors.add_error(f"Invalid comparition {childrenNodes[0]} = {childrenNodes[1]} types missmatch", ctx.start.line)
            return ERROR


    def visitMethodCall(self, ctx: YAPLParser.MethodCallContext):
        curr_class = self.class_def
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        # Check if first exp type exists
        if not self.types_table.exists(childrenNodes[0]):
            self.errors.add_error(f"Type {childrenNodes[0]} does not exists in method call", ctx.start.line)
        method = ctx.OBJECTID().getText()
        if ctx.TYPEID():
            curr_class = ctx.TYPEID().getText()
            # Find type of the method and its params in the class specified <curr_class>
            m = self.types_table.check_specific_method(method, curr_class, childrenNodes[0])
            if m == "Error2":
                self.errors.add_error(f"No such method named {method} in class {curr_class}", ctx.start.line)
                return ERROR
            elif m == "Error1":
                self.errors.add_error(f"No parent class named {curr_class} for {childrenNodes[0]}", ctx.start.line)
            else:
                # Check params
                if len(childrenNodes) < 2: #no params
                    return m["type"]
                params = m["params"]
                if len(params) != len(childrenNodes[1:]):
                    self.errors.add_error(f"Error in method call, {len(params)} params needed but {len(childrenNodes[1:])} were given", ctx.start.line)
                    if m["type"] == "SELF_TYPE":
                        return curr_class
                    return m["type"]
                for p,g,i in zip(params.values(), childrenNodes[1:], range(len(params))):
                    if p != g:
                        self.errors.add_error(f"Params missmatch in method call {method}, {i+1}th param must be {p} but {g} was given", ctx.start.line)
                if m["type"] == "SELF_TYPE":
                        return curr_class
                return m["type"]
                
        else:
            curr_class = childrenNodes[0]
            m = self.types_table.check_method(method, curr_class)
            if m != "Error":
                if len(childrenNodes) < 2: #no params
                    if m["type"] == "SELF_TYPE":
                        return curr_class
                    return m["type"]
                params = m["params"]
                if len(params) != len(childrenNodes[1:]):
                    self.errors.add_error(f"Error in method call, {len(params)} params needed but {len(childrenNodes[1:])} were given", ctx.start.line)
                    if m["type"] == "SELF_TYPE":
                        return curr_class
                    return m["type"]
                for p,g,i in zip(params.values(), childrenNodes[1:], range(len(params))):
                    if p != g:
                        self.errors.add_error(f"Params missmatch in method call {method}, {i+1}th param must be {p} but {g} was given", ctx.start.line)
                if m["type"] == "SELF_TYPE":
                        return curr_class
                return m["type"]
            else:
                self.errors.add_error(f"No such method named {method} in class {curr_class} or parent classes", ctx.start.line)
                return ERROR

    def visitOwnMethodCall(self, ctx: YAPLParser.OwnMethodCallContext):
        name = ctx.OBJECTID().getText()
        method = self.types_table.check_method(name, self.class_def)
        # print("Checking", method, name)
        if method != "Error":
            # Check params
            childrenNodes = childrenNodes = [self.visit(i) for i in ctx.expression()]
            params = method["params"]
            num_params = len(params)
            if num_params < 1:
                if method["type"] == "SELF_TYPE":
                    return self.class_def
                return method["type"]
            if num_params == len(childrenNodes):
                for m_p,e_p,i in zip(params.values(), childrenNodes, range(num_params)):
                    if m_p != e_p:
                        self.errors.add_error(f"Error, in method call {name}, {i+1}th param missmatch, {m_p} expected but {e_p} was given", ctx.start.line)
            else:
                self.errors.add_error(f"Error in method call, {num_params} params needed but {len(childrenNodes)} were given", ctx.start.line)
            if method["type"] == "SELF_TYPE":
                return self.class_def
            return method["type"]
        else:
            self.errors.add_error(f"No method named {name} defined", ctx.start.line)
            return ERROR

    def visitLessThan(self, ctx: YAPLParser.LessThanContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == childrenNodes[1]:
            return TYPE_BOOL
        else:
            self.errors.add_error(f"Invalid comparition {childrenNodes[0]} < {childrenNodes[1]} types missmatch", ctx.start.line)
            return ERROR

    def visitLessEqual(self, ctx: YAPLParser.LessEqualContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == childrenNodes[1]:
            return TYPE_BOOL
        else:
            self.errors.add_error(f"Invalid comparition {childrenNodes[0]} <= {childrenNodes[1]} types missmatch", ctx.start.line)
            return ERROR

    def visitInt(self, ctx: YAPLParser.IntContext):
        return TYPE_INT
    
    def visitString(self, ctx: YAPLParser.StringContext):
        return TYPE_STRING

    def visitTrue(self, ctx: YAPLParser.TrueContext):
        return TYPE_BOOL
    
    def visitFalse(self, ctx: YAPLParser.FalseContext):
        return TYPE_BOOL
    

    def visitNew(self, ctx: YAPLParser.NewContext):
        #Check if type exists
        type_ = ctx.TYPEID().getText()
        if self.types_table.exists(type_):
            return type_
        else:
            self.errors.add_error(f"Type not defined: {type_} in new expression", ctx.start.line)
            return ERROR
    

def compile_cmd():

    file_name = input("Ingrese el nombre del programa YAPL >>")
    # TODO: Check if file exists
    _file = open("input/"+file_name)
    str_file = _file.read()
    _file.close()
    data = InputStream(str_file)
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    parser = YAPLParser(stream)
    tree = parser.program()

    first_visitor = InitCustomVisitor()
    first_visitor.visit(tree)

    visitor = CustomVisitor()
    visitor.types_table = first_visitor.types_table
    output = visitor.visit(tree)

    print(visitor.types_table.get_table())
    print("------Errors------")
    print(visitor.errors.get_errors())


    # os.system(f"{JAVA_COM} {ANTLR} org.antlr.v4.Tool {ANTLR_FLAGS} -o {OUT_DIR} ./{GRAMMAR_NAME}/{GRAMMAR_NAME}.g4")
    # os.system(f"cd {OUT_DIR}/{GRAMMAR_NAME}; javac ./*.java; {JAVA_COM} {ANTLR}:{CLASSPATH} {G_PKG} {GRAMMAR_NAME} {START_RULE} ../../input/{file_name} {GRUN_FLAGS}")
    # os.system(f"rm -r ./{OUT_DIR}")
    


def compile_server(program : str, ):

    data = InputStream(program)
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    parser = YAPLParser(stream)
    tree = parser.program()
    # from antlr4.tree.Trees import Trees
    # print(Trees.toStringTree(tree, None, parser))
    first_visitor = InitCustomVisitor()
    first_visitor.visit(tree)

    visitor = CustomVisitor()
    visitor.types_table = first_visitor.types_table
    output = visitor.visit(tree)

    response = visitor.errors.dump()
    response["table"] = visitor.types_table.dump()

    return response
    # print(visitor.types_table.get_table())
    # print("------Errors------")
    # print(visitor.errors.get_errors())


    # os.system(f"{JAVA_COM} {ANTLR} org.antlr.v4.Tool {ANTLR_FLAGS} -o {OUT_DIR} ./{GRAMMAR_NAME}/{GRAMMAR_NAME}.g4")
    # os.system(f"cd {OUT_DIR}/{GRAMMAR_NAME}; javac ./*.java; {JAVA_COM} {ANTLR}:{CLASSPATH} {G_PKG} {GRAMMAR_NAME} {START_RULE} ../../input/{file_name} {GRUN_FLAGS}")
    # os.system(f"rm -r ./{OUT_DIR}")
    
