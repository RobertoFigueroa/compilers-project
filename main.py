from dataclasses import dataclass

from antlr4 import *

from classes.errors import Errors
from classes.int_code import IC, Quadruple
from classes.stack import Stack
from classes.symbol_table import Symbol, SymbolTable, TypeElement, TypeTable
from dist.YAPL.YAPLLexer import YAPLLexer
from dist.YAPL.YAPLParser import YAPLParser
from dist.YAPL.YAPLVisitor import YAPLVisitor

TYPE_INT = "Int"
TYPE_BOOL = "Bool"
TYPE_STRING = "String"
OBJECT = "Object"
ERROR = "Error"
MAX_TEMP_VARS = 10

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

@dataclass
class ReturnNode:
    """Class for managing return values from nodes"""
    type : str
    value : str = None
    code : IC = None
    addr : str = None

    def __repr__(self) -> str:
        return self.type

    def __eq__(self, other: object) -> bool:
        if other == None:
            return False
        if type(other) == str:
            return self.type == other

        return self.type == other.type

#**************************************
#            CODE GENERATOR
#**************************************
class CodeGenerator(YAPLVisitor):

    def __init__(self) -> None:
        super().__init__()
        self.errors = Errors()
        self.symbol_table = Stack()
        self.types_table = TypeTable(self.errors)
        self.class_def = None
        self.int_code = IC()
        self.bp = -1
        self.init_bp = 0
        self.temp_index = 0
        self.label_index = -1
        self.heap_offset = 0

    def get_temp_var(self):
        self.temp_index = (self.temp_index + 1) % MAX_TEMP_VARS
        return "t"+str(self.temp_index)

    def get_new_label(self):
        self.label_index += 1
        return "l_"+str(self.label_index)

    def get_size(self, _type : str) -> int:
        if _type == TYPE_INT:
            return 4
        elif _type == TYPE_BOOL:
            return 2
        elif _type == TYPE_STRING:
            return 4
        else:
            return 6

    def update_bp(self, size:int) -> None:
        if self.bp == -1:
            self.bp = self.init_bp
            return
        self.bp += size
        return

    def visitProgram(self, ctx: YAPLParser.ProgramContext):
        top = self.visit(ctx.programBlocks())
        return top

    def visitClasses(self, ctx: YAPLParser.ClassesContext):
        top = self.visit(ctx.classDefine())
        return top

    def get_var_size(self, name : str) -> tuple:
        temp_stack = Stack()
        class_found = False
        result = (0,0)
        while not class_found:
            # print("Searching for", name)
            t = self.symbol_table.pop()
            temp_stack.push(t)
            # print("Top sym t is", t._context)
            if self.symbol_table.is_empty():
                result = (0,0)
                class_found = True
            if t.exists(name):
                class_found = True
                result = t.get_symbol_size(name)
                # print("Found size of var, ", name, result)
        while not temp_stack.is_empty():
            self.symbol_table.push(temp_stack.pop())
        return result

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
        print(self.symbol_table)
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

    #TODO: agregar codigo para declaraciones en letit
    def visitLetIn(self, ctx: YAPLParser.LetInContext):
        self.symbol_table.push(SymbolTable(self.errors, 2))
        ids = [i.getText() for i in ctx.OBJECTID()]
        types = [i.getText() for i in ctx.TYPEID()]
        ic = IC()
        temp = self.get_temp_var() # Declare temp variable for return value
        ic.add(Quadruple("0", op="<-", result=temp))
        childrenNodes = []
        if len(ctx.expression()) > 1:
            childrenNodes = [self.visit(i) for i in ctx.expression()[:-1]]
        assign_exprs = []
        if len(childrenNodes) > 0:
            [assign_exprs.append(i) for i in childrenNodes]
        if len(assign_exprs) < len(ids):
            [assign_exprs.append(None) for i in range(len(ids)-len(assign_exprs))]

        for i,t,a in zip(ids, types, assign_exprs):
            size = self.get_size(t)
            self.update_bp(size)
            self.symbol_table.top().add_symbol(Symbol(i, t, self.get_size(t), self.bp))
            size, offset = self.get_var_size(i)
            if a != None:
                ic.add(Quadruple(a.addr, op="<-", result=offset))
            else:
                # TODO: Manage void value if its an Int or a String or a Bool
                ic.add(Quadruple("0", op="<-", result=offset))
        body = self.visit(ctx.expression()[-1])
        ic.concat(body.code)
        ic.add(Quadruple(body.addr, op="<-", result=temp))
        return ReturnNode(OBJECT, "let", ic, temp)

    def visitClassDefine(self, ctx: YAPLParser.ClassDefineContext): # Class definition
        self.class_def = ctx.TYPEID()[0].getText()
        self.symbol_table.clear()
        self.symbol_table.push(SymbolTable(self.errors, 0))
        ic = IC()
        label = self.get_new_label()+"_class_"+self.class_def
        code = Quadruple(label, op="defLabel")
        ic.add(code)
        for n in ctx.feature():
            return_val = self.visit(n)
            if return_val.code:
                ic.concat(return_val.code)
        # print(ic.get_table())

        return ReturnNode(OBJECT, "class", ic, None)

    def visitProperty(self, ctx: YAPLParser.PropertyContext): # Attributes of a class
        size = self.get_size(ctx.TYPEID().getText())
        self.update_bp(size)
        self.symbol_table.top().add_symbol(Symbol(ctx.OBJECTID().getText(), ctx.TYPEID().getText(), size, self.bp))
        ic = IC()
        size, offset = self.get_var_size(ctx.OBJECTID().getText())
        if ctx.expression():
            result = self.visit(ctx.expression())
            ic.concat(result.code)
            ic.add(Quadruple(result.addr, op="<-", result=offset))
        else:
            #TODO: Check type for init void value
            ic.add(Quadruple("0", op="<-", result=offset))
        return ReturnNode(ctx.TYPEID().getText(), ctx.OBJECTID().getText(), ic, offset)

    def visitParentheses(self, ctx: YAPLParser.ParenthesesContext):
        result = self.visit(ctx.expression())
        return ReturnNode(result.type, result.value, result.code, result.addr)

    def visitBlock(self, ctx: YAPLParser.BlockContext):
        ic = IC()
        temp = self.get_temp_var() # For return value
        ic.add(Quadruple("0", op="<-", result=temp))
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        [ic.concat(i.code) for i in childrenNodes]
        ic.add(Quadruple(childrenNodes[-1].addr, op="<-", result=temp))
        return ReturnNode(OBJECT, "block", ic, temp)
        #return self.visit(ctx.expression()[-1])

    def visitMethod(self, ctx: YAPLParser.MethodContext): # Function within a class
        t = self.get_temp_var()
        if self.symbol_table.top()._context == 0: # Means is the first method found in class
            self.symbol_table.push(SymbolTable(self.errors, 1))
        else:
            class_found = True
            while self.symbol_table.is_empty() or class_found:
                sym_table = self.symbol_table.pop()
                if sym_table._context == 0:
                    class_found = not class_found
                    self.symbol_table.push(sym_table)
                    self.symbol_table.push(SymbolTable(self.errors, 1))
            if self.symbol_table.is_empty():
                print("Fatal error in visitmethod function")
                self.symbol_table.push(SymbolTable(self.errors, 1))
    
        params = ctx.formal()
        funcname = ctx.OBJECTID()
        for i in params:
            size = self.get_size(ctx.TYPEID().getText())
            self.update_bp(size)
            self.symbol_table.top().add_symbol(Symbol(i.OBJECTID().getText(), i.TYPEID().getText(), size, self.bp))
            # print(self.symbol_table.top().get_table())
        label = funcname.getText()+"@"+self.class_def
        result = self.visit(ctx.expression())
        ic = IC()
        ic.add(Quadruple(label, op="defLabel"))
        ic.concat(result.code)
        ic.add(Quadruple(result.addr, op="<-", result=t))
        return ReturnNode(OBJECT, "func", ic, t)


    def visitAssignment(self, ctx: YAPLParser.AssignmentContext):
        name = ctx.OBJECTID().getText()
        # Check if exists in scope
        type_ = self.exists_local_global_scope(name)
        right_side = self.visit(ctx.expression())
        ic = IC()
        ic.concat(right_side.code)
        size, offset = self.get_var_size(name)
        code = Quadruple(arg1=right_side.addr, op="<-", result=offset)
        ic.add(code)
        # print(ic.get_table())
        return ReturnNode(type_, "<-", ic, str(offset))

    def visitId(self, ctx: YAPLParser.IdContext):
        value = ctx.OBJECTID().getText()
        result = self.exists_local_global_scope(value)
        if value == "self":
            ic = IC()
            t = self.get_temp_var()
            ic.add(Quadruple(self.class_def, op="this", result=t))
            return ReturnNode(self.class_def, self.class_def, ic, t)
        if result:
            size, offset = self.get_var_size(value)
            code = Quadruple()
            ic = IC()
            ic.add(code)
            return ReturnNode(result, value, ic, str(offset))


    def visitIf(self, ctx: YAPLParser.IfContext):
        temp = self.get_temp_var()
        ctx.true = self.get_new_label()+"_true"
        ctx.false = self.get_new_label()+"_false"
        ctx.next = self.get_new_label()+"_next"
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        ic = IC()
        ic.concat(childrenNodes[0].code)
        true_label = Quadruple(ctx.true, op="defLabel")
        ic.add(true_label)
        ic.concat(childrenNodes[1].code)
        ic.add(Quadruple(childrenNodes[1].addr, op="<-", result=temp))# return value
        s_next = Quadruple(ctx.next, op="goto")
        ic.add(s_next)
        false_label = Quadruple(ctx.false, op="defLabel")
        ic.add(false_label)
        ic.concat(childrenNodes[2].code)
        ic.add(Quadruple(childrenNodes[2].addr, op="<-", result=temp))
        ic.add(Quadruple(ctx.next, op="defLabel"))
        # print(ic.get_table())
        return ReturnNode(TYPE_BOOL, "if", ic, temp)


    def visitWhile(self, ctx: YAPLParser.WhileContext):
        temp = self.get_temp_var()
        start = self.get_new_label()+"_start"
        ctx.true = self.get_new_label()+"_true"
        ctx.next = self.get_new_label()+"_next"
        ctx.false = ctx.next
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        ic = IC()
        start_l = Quadruple(start, op="defLabel")
        ic.add(start_l)
        ic.concat(childrenNodes[0].code)
        ic.add(Quadruple(ctx.true, op="defLabel"))
        ic.concat(childrenNodes[1].code)
        ic.add(Quadruple(childrenNodes[1].addr, op="<-", result=temp))
        ic.add(Quadruple(start, op="goto"))
        ic.add(Quadruple(ctx.next, op="defLabel"))
        print(ic.get_table())
        return ReturnNode(OBJECT, "while", ic, temp)


    def visitAdd(self, ctx: YAPLParser.AddContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        t = self.get_temp_var()
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.concat(childrenNodes[1].code)
        code = Quadruple(childrenNodes[0].addr, childrenNodes[1].addr, t, "+")
        ic.add(code)
        return ReturnNode(childrenNodes[0].type, "+", ic, t)

    def visitMinus(self, ctx: YAPLParser.MinusContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        t = self.get_temp_var()
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.concat(childrenNodes[1].code)
        code = Quadruple(childrenNodes[0].addr, childrenNodes[1].addr, t, "-")
        ic.add(code)
        return ReturnNode(childrenNodes[0].type, "-", ic, t)


    def visitMultiply(self, ctx: YAPLParser.MultiplyContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        t = self.get_temp_var()
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.concat(childrenNodes[1].code)
        code = Quadruple(childrenNodes[0].addr, childrenNodes[1].addr, t, "*")
        ic.add(code)
        return ReturnNode(childrenNodes[0].type, "*", ic, t)

    def visitDivision(self, ctx: YAPLParser.DivisionContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        t = self.get_temp_var()
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.concat(childrenNodes[1].code)
        code = Quadruple(childrenNodes[0].addr, childrenNodes[1].addr, t, "/")
        ic.add(code)
        return ReturnNode(childrenNodes[0].type, "/", ic, t)

    def visitBoolNot(self, ctx: YAPLParser.BoolNotContext):
        expr = self.visit(ctx.expression())
        t = self.get_temp_var()
        code = Quadruple(expr.addr, result=t, op="not")
        ic = IC()
        ic.concat(expr.code)
        ic.add(code)
        return ReturnNode(expr.type, "not", ic, t)

    def visitNegative(self, ctx: YAPLParser.NegativeContext):
        expr = self.visit(ctx.expression())
        t = self.get_temp_var()
        ic = IC()
        ic.concat(expr.code)
        code = Quadruple(expr.addr, op="~", result=t)
        ic.add(code)
        return ReturnNode(expr.type, "~", ic, t)

    def visitEqual(self, ctx: YAPLParser.EqualContext):
        # Check if this expresion is not part of assignment
        ctx.true = self.get_new_label()+"_true"
        ctx.false = self.get_new_label()+"_false"
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.concat(childrenNodes[1].code)
        instr = "if" + "_" + childrenNodes[0].addr + "_" + "=" + "_" + childrenNodes[1].addr + "_" + "goto" + "_" + ctx.parentCtx.true
        code = Quadruple(instr, op="=")
        code2 = Quadruple(ctx.parentCtx.false, op="goto")
        ic.add(code)
        ic.add(code2)
        return ReturnNode(TYPE_BOOL, "=", ic, None)

    def visitMethodCall(self, ctx: YAPLParser.MethodCallContext):
        curr_class = self.class_def
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.add(Quadruple("params", op="load"))
        class_pointer = childrenNodes[0].type
        if ctx.TYPEID():
            class_pointer = ctx.TYPEID().getText()
        label = "{}@{}".format(ctx.OBJECTID().getText(), class_pointer)
        ic.add(Quadruple(label, op="jump"))
        temp = self.get_temp_var()
        ic.add(Quadruple("func_res", op="<-", result=temp))
        return ReturnNode(OBJECT, "funcall", ic, temp)
     

    def visitOwnMethodCall(self, ctx: YAPLParser.OwnMethodCallContext):
        name = ctx.OBJECTID().getText()
        method = self.types_table.check_method(name, self.class_def)
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        ic = IC()
        temp = self.get_temp_var()
        ic.add(Quadruple("params", op="load"))
        ic.add(Quadruple("{}@{}".format(name, self.class_def), op="jump"))
        ic.add(Quadruple("func_res", op="<-", result=temp))
        return ReturnNode(OBJECT, "ownfunc", ic, temp)

    def visitLessThan(self, ctx: YAPLParser.LessThanContext):
        ctx.true = self.get_new_label()+"_true"
        ctx.false = self.get_new_label()+"_false"
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.concat(childrenNodes[1].code)
        instr = "if" + "_" + childrenNodes[0].addr + "_" + "<" + "_" + childrenNodes[1].addr + "_" + "goto" + "_" + ctx.parentCtx.true
        code = Quadruple(instr, op="<")
        code2 = Quadruple(ctx.parentCtx.false, op="goto")
        ic.add(code)
        ic.add(code2)
        return ReturnNode(TYPE_BOOL, "<", ic, None)

    def visitLessEqual(self, ctx: YAPLParser.LessEqualContext):
        ctx.true = self.get_new_label()+"_true"
        ctx.false = self.get_new_label()+"_false"
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        ic = IC()
        ic.concat(childrenNodes[0].code)
        ic.concat(childrenNodes[1].code)
        instr = "if" + "_" + childrenNodes[0].addr + "_" + "<=" + "_" + childrenNodes[1].addr + "_" + "goto" + "_" + ctx.parentCtx.true
        code = Quadruple(instr, op="<=")
        code2 = Quadruple(ctx.parentCtx.false, op="goto")
        ic.add(code)
        ic.add(code2)
        return ReturnNode(TYPE_BOOL, "<=", ic, None)

    def visitIsvoid(self, ctx: YAPLParser.IsvoidContext):
        expr = self.visit(ctx.expression())
        t = self.get_temp_var()
        code = Quadruple(expr.addr, result=t, op="is_void")
        ic = IC()
        ic.concat(expr.code)
        ic.add(code)
        return ReturnNode(expr.type, "is_void", ic, t)

    def visitNew(self, ctx: YAPLParser.NewContext):
        temp = self.get_temp_var()
        ic = IC()
        instance = self.types_table.get_element(ctx.TYPEID().getText())
        ic.add(Quadruple(str(self.heap_offset)+"x"+str(instance.size), op="new", result=temp))
        ic.add(Quadruple("params", op="init"))
        self.heap_offset += instance.size
        return ReturnNode(ctx.TYPEID().getText(), "new", ic, temp)

    def visitInt(self, ctx: YAPLParser.IntContext):
        ic = IC()
        return ReturnNode(TYPE_INT, ctx.getText(), ic, ctx.getText())

    def visitString(self, ctx: YAPLParser.StringContext):
        ic = IC()
        return ReturnNode(TYPE_STRING, ctx.getText(), ic, ctx.getText())

    def visitTrue(self, ctx: YAPLParser.TrueContext):
        true_label = self.get_new_label()
        code = Quadruple(true_label, op="goto")
        ic = IC()
        ic.add(code)
        return ReturnNode(TYPE_BOOL, (true_label, ""), ic, ctx.getText())

    def visitFalse(self, ctx: YAPLParser.FalseContext):
        false_label = self.get_new_label()
        code = Quadruple(false_label, op="goto")
        ic = IC()
        ic.add(code)
        return ReturnNode(TYPE_BOOL, ("", false_label), ic, ctx.getText())



#**************************************
#            Init Visitor
#**************************************
class InitCustomVisitor(YAPLVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.errors = Errors()
        self.types_table = TypeTable(self.errors)
        self.offset = 5

    def visitClassDefine(self, ctx: YAPLParser.ClassDefineContext):
        self.offset += 1
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



#**************************************
# Type checking and semantic visitor
#**************************************
class CustomVisitor(YAPLVisitor):

    def __init__(self) -> None:
        super().__init__()
        self.errors = Errors()
        self.symbol_table = Stack()
        self.types_table = TypeTable(self.errors)
        self.class_def = None
        self.int_code = IC()
        self.bp = -1
        self.init_bp = 0
        self.temp_index = 0

    def get_temp_var(self):
        self.temp_index += 1
        return "t"+str(self.temp_index)

    def get_size(self, _type : str) -> int:
        if _type == TYPE_INT:
            return 4
        elif _type == TYPE_BOOL:
            return 2
        elif _type == TYPE_STRING:
            return 4
        else:
            return 6

    def update_bp(self, size:int) -> None:
        if self.bp == -1:
            self.bp = self.init_bp
            return
        self.bp += size
        return

    def visitProgram(self, ctx: YAPLParser.ProgramContext):
        return super().visitProgram(ctx)

    def get_var_size(self, name : str) -> tuple:
        temp_stack = Stack()
        class_found = False
        result = (0,0)
        while not class_found:
            # print("Searching for", name)
            t = self.symbol_table.pop()
            temp_stack.push(t)
            # print("Top sym t is", t._context)
            if self.symbol_table.is_empty():
                result = (0,0)
                class_found = True
            if t.exists(name):
                class_found = True
                result = t.get_symbol_size(name)
                # print("Found size of var, ", name, result)
        while not temp_stack.is_empty():
            self.symbol_table.push(temp_stack.pop())
        return result


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
            size = self.get_size(t)
            self.update_bp(size)
            self.symbol_table.top().add_symbol(Symbol(i, t, self.get_size(t), self.bp))
            # print(self.symbol_table.top().get_table())
        # print("This is last in expre child nodes in let", exprChildrenNodes[-1])

        return ReturnNode(self.visit(ctx.expression()[-1]))

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
        size = self.get_size(ctx.TYPEID().getText())
        self.update_bp(size)
        self.symbol_table.top().add_symbol(Symbol(ctx.OBJECTID().getText(), ctx.TYPEID().getText(), size, self.bp))
        # print(self.symbol_table.top().get_table())
        return ReturnNode(ctx.TYPEID().getText())

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
            #print("Adding", i.OBJECTID().getText(), i.TYPEID().getText())
            size = self.get_size(ctx.TYPEID().getText())
            # print("bp is ", self.bp)
            self.update_bp(size)
            self.symbol_table.top().add_symbol(Symbol(i.OBJECTID().getText(), i.TYPEID().getText(), size, self.bp))
            print(self.symbol_table.top().get_table())
        # tparams["type"] = ctx.TYPEID().getText()

        # self.symbol_table.top().add_symbol(Symbol(ctx.OBJECTID().getText(), ctx.TYPEID().getText()))
        _type = self.visit(ctx.expression()) # Type of return
        if ctx.TYPEID().getText() == TYPE_STRING and _type == TYPE_INT:
            self.errors.add_error(f"Erorr in function, type {ctx.TYPEID().getText()} expected but {_type} returned", ctx.start.line)
        if ctx.TYPEID().getText() == TYPE_INT and _type == TYPE_BOOL:
            self.errors.add_error(f"Erorr in function, type {ctx.TYPEID().getText()} expected but {_type} returned", ctx.start.line)
        if ctx.TYPEID().getText() == "SELF_TYPE":
            return ReturnNode(_type)
        if _type != ctx.TYPEID().getText():
            if self.types_table.has_parent(_type, ctx.TYPEID().getText()):
                return ReturnNode(ctx.TYPEID().getText())
            self.errors.add_error(f"Erorr in function, type {ctx.TYPEID().getText()} expected but {_type} returned", ctx.start.line)
        return ReturnNode(_type)


    def visitAssignment(self, ctx: YAPLParser.AssignmentContext):
        name = ctx.OBJECTID().getText()
        # Check if exists in scope
        type_ = self.exists_local_global_scope(name)
        right_side = self.visit(ctx.expression())

        if type_:
            if type_ == right_side:
                return ReturnNode(type_)
            elif type_ == TYPE_BOOL and right_side == TYPE_INT:
                return ReturnNode(type_)
            elif type_ == TYPE_INT and right_side == TYPE_BOOL:
                return ReturnNode(type_)
            if type_ != right_side:
                if type_ == TYPE_INT and right_side == TYPE_STRING:
                    self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side} can't found inhertiance relation", ctx.start.line)
                    return ReturnNode(ERROR)
                if type_ == TYPE_STRING and right_side == TYPE_INT:
                    self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side} can't found inhertiance relation", ctx.start.line)
                    return ReturnNode(ERROR)
                if self.types_table.has_parent(right_side, type_):
                    return ReturnNode(type_)
                else:
                    self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side} can't found inhertiance relation", ctx.start.line)
            else:
                self.errors.add_error(f"Error in assignment, missmatch types {type_} <-  {right_side}", ctx.start.line)

        else:
            self.errors.add_error(f"Error in assignment, no variable {name} in the scope", ctx.start.line)
            return ReturnNode(ERROR)

    def visitId(self, ctx: YAPLParser.IdContext):
        value = ctx.OBJECTID().getText()
        if value == "self":
            
            return ReturnNode(self.class_def, self.class_def)

        result = self.exists_local_global_scope(value)
        if result:
            return ReturnNode(result, value)
        else:
            self.errors.add_error(f"Invalid id, not defined in scope {value}", ctx.start.line)
            return ReturnNode(ERROR)
        # local_scope = self.symbol_table.pop()
        # if self.symbol_table.top().exists(value):
        #     _type = self.symbol_table.top().get_symbol_type(value)
        #     self.symbol_table.push(local_scope)
        #     return _type


    def visitIf(self, ctx: YAPLParser.IfContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_BOOL or childrenNodes[0] == TYPE_INT:
            if childrenNodes[1] == childrenNodes[2]:
                return ReturnNode(childrenNodes[1])
            else:
                return ReturnNode(OBJECT)
        else:
            self.errors.add_error(f"Invalid expression on if statement {childrenNodes[0]} found, expected Bool type", ctx.start.line)
            return ReturnNode(ERROR)

    def visitWhile(self, ctx: YAPLParser.WhileContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_BOOL:
            return ReturnNode(TYPE_BOOL)
        else:
            self.errors.add_error(f"Invalid expression on while statement, {childrenNodes[0]} found, expected Bool type", ctx.start.line)
            return ReturnNode(ERROR)

    def visitAdd(self, ctx: YAPLParser.AddContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            # Check wich type of nodes are (value-nodes, id-nodes)
            # Search on symbol table
            # arg1 = None
            # arg2 = None
            # print(childrenNodes[1])
            # if childrenNodes[0].value.isnumeric():
            #     arg1 = childrenNodes[0].value
            # else:
            #     size, offset = self.get_var_size(childrenNodes[0].value)
            #     arg1 = str(self.init_bp)+"x"+str(offset)
            # if childrenNodes[1].value.isnumeric():
            #     arg2 = childrenNodes[1].value
            # else:
            #     size, offset = self.get_var_size(childrenNodes[1].value)
            #     arg2 = str(self.init_bp)+"x"+str(offset)
            # temp = self.get_temp_var()
            # self.int_code.add_instruction(arg1,arg2,"+", temp)
            return ReturnNode(TYPE_INT)
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} + {childrenNodes[1]} types missmatch", ctx.start.line)
            return ReturnNode(ERROR)

    def visitMinus(self, ctx: YAPLParser.MinusContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            # # Check wich type of nodes are (value-nodes, id-nodes)
            # # Search on symbol table
            # arg1 = None
            # arg2 = None
            # print(childrenNodes[1].value)
            # if childrenNodes[0].value.isnumeric():
            #     arg1 = childrenNodes[0].value
            # else:
            #     size, offset = self.get_var_size(childrenNodes[0].value)
            #     arg1 = str(self.init_bp)+"x"+str(offset)
            # if childrenNodes[1].value.isnumeric():
            #     arg2 = childrenNodes[1].value
            # else:
            #     size, offset = self.get_var_size(childrenNodes[1].value)
            #     arg2 = str(self.init_bp)+"x"+str(offset)
            #     temp = self.get_temp_var()
            # self.int_code.add_instruction(arg1,arg2,"-", temp)
            return ReturnNode(TYPE_INT)
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} - {childrenNodes[1]} types missmatch", ctx.start.line)
            return ReturnNode(ERROR)

    def visitMultiply(self, ctx: YAPLParser.MultiplyContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            return ReturnNode(TYPE_INT)
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} * {childrenNodes[1]} types missmatch", ctx.start.line)
            return ReturnNode(ERROR)

    def visitDivision(self, ctx: YAPLParser.DivisionContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_INT and childrenNodes[1] == TYPE_INT:
            return ReturnNode(TYPE_INT)
        else:
            self.errors.add_error(f"Invalid expression {childrenNodes[0]} * {childrenNodes[1]} types missmatch", ctx.start.line)
            return ReturnNode(ERROR)

    def visitBoolNot(self, ctx: YAPLParser.BoolNotContext):
        expr = self.visit(ctx.expression())
        if type(expr) == list:
            childNode = [self.visit(i) for i in expr]
            if childNode[0] == TYPE_BOOL:
                return ReturnNode(TYPE_BOOL)
            else:
                self.errors.add_error(f"Invalid expression ~{childNode[0]} types missmatch", ctx.start.line)
        else:
            if expr == TYPE_BOOL:
                return ReturnNode(TYPE_BOOL)
            else:
                self.errors.add_error(f"Invalid expression ~{expr} types missmatch", ctx.start.line)
                return ReturnNode(ERROR)

    def visitNegative(self, ctx: YAPLParser.NegativeContext):
        expr = self.visit(ctx.expression())
        if type(expr) == list:
            childNode = [self.visit(i) for i in expr]
            if childNode[0] == TYPE_INT:
                return ReturnNode(TYPE_INT)
            else:
                self.errors.add_error(f"Invalid expression ~{childNode[0]} types missmatch", ctx.start.line)
        else:
            if expr == TYPE_INT:
                return ReturnNode(TYPE_INT)
                return TYPE_INT
            else:
                self.errors.add_error(f"Invalid expression ~{expr} types missmatch", ctx.start.line)
                return ReturnNode(ERROR)

    def visitEqual(self, ctx: YAPLParser.EqualContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == childrenNodes[1]:
            return ReturnNode(TYPE_BOOL)
        else:
            self.errors.add_error(f"Invalid comparition {childrenNodes[0]} = {childrenNodes[1]} types missmatch", ctx.start.line)
            return ReturnNode(ERROR)


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
                return ReturnNode(ERROR)
            elif m == "Error1":
                self.errors.add_error(f"No parent class named {curr_class} for {childrenNodes[0]}", ctx.start.line)
            else:
                # Check params
                if len(childrenNodes) < 2: #no params
                    return ReturnNode(m["type"])
                params = m["params"]
                if len(params) != len(childrenNodes[1:]):
                    self.errors.add_error(f"Error in method call, {len(params)} params needed but {len(childrenNodes[1:])} were given", ctx.start.line)
                    if m["type"] == "SELF_TYPE":
                        return ReturnNode(curr_class)
                    return m["type"]
                for p,g,i in zip(params.values(), childrenNodes[1:], range(len(params))):
                    if p != g:
                        self.errors.add_error(f"Params missmatch in method call {method}, {i+1}th param must be {p} but {g} was given", ctx.start.line)
                if m["type"] == "SELF_TYPE":
                        return ReturnNode(curr_class)
                return ReturnNode(m["type"])
                return m["type"]

        else:
            curr_class = childrenNodes[0]
            m = self.types_table.check_method(method, curr_class)
            if m != "Error":
                if len(childrenNodes) < 2: #no params
                    if m["type"] == "SELF_TYPE":
                        return ReturnNode(curr_class)
                    return ReturnNode(m["type"])
                    return m["type"]
                params = m["params"]
                if len(params) != len(childrenNodes[1:]):
                    self.errors.add_error(f"Error in method call, {len(params)} params needed but {len(childrenNodes[1:])} were given", ctx.start.line)
                    if m["type"] == "SELF_TYPE":
                        return ReturnNode(curr_class)
                    return ReturnNode(m["type"])
                for p,g,i in zip(params.values(), childrenNodes[1:], range(len(params))):
                    if p != g:
                        self.errors.add_error(f"Params missmatch in method call {method}, {i+1}th param must be {p} but {g} was given", ctx.start.line)
                if m["type"] == "SELF_TYPE":
                        return ReturnNode(curr_class)
                return m["type"]
            else:
                self.errors.add_error(f"No such method named {method} in class {curr_class} or parent classes", ctx.start.line)
                return ReturnNode(ERROR)

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
                    return ReturnNode(self.class_def)
                return ReturnNode(method["type"])
            if num_params == len(childrenNodes):
                for m_p,e_p,i in zip(params.values(), childrenNodes, range(num_params)):
                    if m_p != e_p:
                        self.errors.add_error(f"Error, in method call {name}, {i+1}th param missmatch, {m_p} expected but {e_p} was given", ctx.start.line)
            else:
                self.errors.add_error(f"Error in method call, {num_params} params needed but {len(childrenNodes)} were given", ctx.start.line)
            if method["type"] == "SELF_TYPE":
                return ReturnNode(self.class_def)
            return ReturnNode(method["type"])
        else:
            self.errors.add_error(f"No method named {name} defined", ctx.start.line)
            return ReturnNode(ERROR)

    def visitLessThan(self, ctx: YAPLParser.LessThanContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == childrenNodes[1]:
            return ReturnNode(TYPE_BOOL)
        else:
            self.errors.add_error(f"Invalid comparition {childrenNodes[0]} < {childrenNodes[1]} types missmatch", ctx.start.line)
            return ReturnNode(ERROR)


    def visitLessEqual(self, ctx: YAPLParser.LessEqualContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == childrenNodes[1]:
            return ReturnNode(TYPE_BOOL)
        else:
            self.errors.add_error(f"Invalid comparition {childrenNodes[0]} <= {childrenNodes[1]} types missmatch", ctx.start.line)
            return ReturnNode(ERROR)

    def visitInt(self, ctx: YAPLParser.IntContext):
        return ReturnNode(TYPE_INT, ctx.getText())

    def visitString(self, ctx: YAPLParser.StringContext):
        return ReturnNode(TYPE_STRING, ctx.getText())

    def visitTrue(self, ctx: YAPLParser.TrueContext):
        return ReturnNode(TYPE_BOOL)

    def visitFalse(self, ctx: YAPLParser.FalseContext):
        return ReturnNode(TYPE_BOOL)

    def visitNew(self, ctx: YAPLParser.NewContext):
        #Check if type exists
        type_ = ctx.TYPEID().getText()
        if self.types_table.exists(type_):
            return ReturnNode(type_)
        else:
            self.errors.add_error(f"Type not defined: {type_} in new expression", ctx.start.line)
            return ReturnNode(ERROR)


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

    # Visitor for generate type table
    first_visitor = InitCustomVisitor()
    first_visitor.visit(tree)

    # Visitor for semantic and type validation
    try:
        visitor = CustomVisitor()
        visitor.types_table = first_visitor.types_table
        output = visitor.visit(tree)
    except:
        print("Somenthing went wrong during type and semantic analysis")
        return 

    # Visitor for generate intermediate code
    
    ic_visitor = CodeGenerator()
    ic_visitor.types_table = visitor.types_table
    result = ic_visitor.visit(tree)

    if result == None:
        print("Somenthing went wrong during type and semantic analysis")
        return

    print(visitor.types_table.get_table())
    print("------Errors------")
    print(visitor.errors.get_errors())

    print("------Int. Code------")
    print(result.code.get_table())

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

    try:
        visitor = CustomVisitor()
        visitor.types_table = first_visitor.types_table
        output = visitor.visit(tree)
    except:
        print("Somenthing went wrong during type and semantic analysis")
        return { "comp_error" : "Something went wrong"}

    ic_visitor = CodeGenerator()
    ic_visitor.types_table = visitor.types_table
    result = ic_visitor.visit(tree)

    if result == None:
        print("Somenthing went wrong during type and semantic analysis")
        return {"comp_error" : "Somenthing went wrong during type and semantic analysis"}

    response = visitor.errors.dump()
    response["table"] = visitor.types_table.dump()
    response["ic"] = result.code.dump()
    print(result.code.get_table())
    
    return response
    # print(visitor.types_table.get_table())
    # print("------Errors------")
    # print(visitor.errors.get_errors())


    # os.system(f"{JAVA_COM} {ANTLR} org.antlr.v4.Tool {ANTLR_FLAGS} -o {OUT_DIR} ./{GRAMMAR_NAME}/{GRAMMAR_NAME}.g4")
    # os.system(f"cd {OUT_DIR}/{GRAMMAR_NAME}; javac ./*.java; {JAVA_COM} {ANTLR}:{CLASSPATH} {G_PKG} {GRAMMAR_NAME} {START_RULE} ../../input/{file_name} {GRUN_FLAGS}")
    # os.system(f"rm -r ./{OUT_DIR}")

