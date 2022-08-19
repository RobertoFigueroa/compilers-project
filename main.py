from ctypes.wintypes import BOOL
from inspect import ismemberdescriptor
from pickle import TRUE
from xml.dom.minidom import TypeInfo
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

class CustomVisitor(YAPLVisitor):

    def __init__(self) -> None:
        super().__init__()
        self.errors = Errors()
        self.symbol_table = Stack()
        self.types_table = TypeTable(self.errors)
        self.class_def = None

    def exists_local_global_scope(self, name : str) -> any:
        local = self.symbol_table.pop()
        if local.exists(name): # Check in local scope
            symb = local.get_symbol_type(name)
            self.symbol_table.push(local)
            return symb
        if self.symbol_table.top().exists(name): # Check in global scope
            
            self.symbol_table.push(local)
            return 0
        return None

    def visitLetIn(self, ctx: YAPLParser.LetInContext):
        self.symbol_table.push(SymbolTable(self.errors, 2))
        print("This is stack\n", self.symbol_table.get_stack(), "in let")
        return super().visitLetIn(ctx)

    def visitClassDefine(self, ctx: YAPLParser.ClassDefineContext): # Class definition
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
        print("This is stack\n", self.symbol_table.get_stack(), "in", ctx.TYPEID()[0].getText())
        self.class_def = ctx.TYPEID()[0].getText()
        if ctx.INHERITS():
            _type = TypeElement(ctx.TYPEID()[0].getText(), ctx.TYPEID()[1].getText())
            self.types_table.add_type(_type)
        else:
            _type = TypeElement(ctx.TYPEID()[0].getText())
            self.types_table.add_type(_type)
        return super().visitClassDefine(ctx)    

    def visitProperty(self, ctx: YAPLParser.PropertyContext): # Attributes of a class
        belongs_to = ctx.parentCtx.TYPEID()[0].getText()
        self.types_table.update_attributes(ctx.OBJECTID().getText(), ctx.TYPEID().getText(), belongs_to)
        self.symbol_table.top().add_symbol(Symbol(ctx.OBJECTID().getText(), ctx.TYPEID().getText()))
        return super().visitProperty(ctx)

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
        print("This is stack\n", self.symbol_table.get_stack(), "in", ctx.OBJECTID().getText())
        params = ctx.formal()
        tparams = {}
        belongs_to = ctx.parentCtx.TYPEID()[0].getText()
        for i in params:
            tparams[i.OBJECTID().getText()] = i.TYPEID().getText() 
        # tparams["type"] = ctx.TYPEID().getText()
        self.types_table.update_methods(ctx.OBJECTID().getText(), ctx.TYPEID().getText(), tparams, belongs_to)
        return super().visitMethod(ctx)



    
    
    def visitAssignment(self, ctx: YAPLParser.AssignmentContext):
        # print("This is assignment", ctx.OBJECTID().getText(), ctx.ASSIGNMENT().getText(), ctx.expression())
        return super().visitAssignment(ctx)
    
    # def visitId(self, ctx: YAPLParser.IdContext):
    #     # Check if exists in local context
    #     value = ctx.OBJECTID().getText()
    #     if self.symbol_table.top().exists(value): 
    #         return self.symbol_table.top().get_symbol_type(value)
    #     else:
    #         # Check in global context
    #         local_scope = self.symbol_table.pop()
    #         if self.symbol_table.top().exists(value):
    #             self.symbol_table.push(local_scope)
    #             return self.symbol_table.top().get_symbol_type(value)
    #         else:
    #             self.symbol_table.push(local_scope)
    #             self.errors.add_error(f"Variable {value} not defined in this scope", ctx.start.line)
    #             return ERROR

    def visitIf(self, ctx: YAPLParser.IfContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        if childrenNodes[0] == TYPE_BOOL:
            return TYPE_BOOL
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
        childNode = [self.visit(i) for i in ctx.expression()]
        if childNode[0] == TYPE_BOOL:
            return TYPE_BOOL
        else:
            self.errors.add_error(f"Invalid expression ~{childNode[0]} types missmatch", ctx.start.line)
            return ERROR

    def visitNegative(self, ctx: YAPLParser.NegativeContext):
        childNode = [self.visit(i) for i in ctx.expression()]
        if childNode[0] == TYPE_INT:
            return TYPE_INT
        else:
            self.errors.add_error(f"Invalid expression ~{childNode[0]} types missmatch", ctx.start.line)
            return ERROR

    def visitEqual(self, ctx: YAPLParser.EqualContext):
        childrenNodes = [self.visit(i) for i in ctx.expression()]
        # print("This are children on equal statement", childrenNodes)
        if childrenNodes[0] == childrenNodes[1]:
            return TYPE_BOOL
        else:
            self.errors.add_error(f"Invalid comparition {childrenNodes[0]} = {childrenNodes[1]} types missmatch", ctx.start.line)
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
        return super().visitNew(ctx)
    

if __name__ == "__main__":

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

    visitor = CustomVisitor()
    output = visitor.visit(tree)

    print(visitor.types_table.get_table())

    print(visitor.errors.get_errors())

    print("This is stack\n", visitor.symbol_table.get_stack())

    # os.system(f"{JAVA_COM} {ANTLR} org.antlr.v4.Tool {ANTLR_FLAGS} -o {OUT_DIR} ./{GRAMMAR_NAME}/{GRAMMAR_NAME}.g4")
    # os.system(f"cd {OUT_DIR}/{GRAMMAR_NAME}; javac ./*.java; {JAVA_COM} {ANTLR}:{CLASSPATH} {G_PKG} {GRAMMAR_NAME} {START_RULE} ../../input/{file_name} {GRUN_FLAGS}")
    # os.system(f"rm -r ./{OUT_DIR}")
    

