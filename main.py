from doctest import ELLIPSIS_MARKER
import os
from antlr4 import *
from dist.YAPL.YAPLLexer import YAPLLexer
from dist.YAPL.YAPLParser import YAPLParser
from dist.YAPL.YAPLVisitor import YAPLVisitor
from classes.symbol_table import ClassTable, AttributeTable, FuncTable

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
        self.cTable = ClassTable()
        self.aTable = AttributeTable()
        self.fTable = FuncTable()
        self.current_scope = 0

    def visitClassDefine(self, ctx: YAPLParser.ClassDefineContext):
        self.current_scope += 1
        if ctx.INHERITS():
            self.cTable.add(ctx.TYPEID()[0].getText(), ctx.TYPEID()[1].getText())
        else:
            self.cTable.add(ctx.TYPEID()[0].getText(), None)
        return super().visitClassDefine(ctx)

    def visitProperty(self, ctx: YAPLParser.PropertyContext):
        belongs_to = ctx.parentCtx.TYPEID()[0].getText()
        self.aTable.add(ctx.OBJECTID().getText(), ctx.TYPEID().getText(), self.current_scope, belongs_to)
        return super().visitProperty(ctx)

    def visitMethod(self, ctx: YAPLParser.MethodContext):
        self.current_scope += 1 
        params = ctx.formal()
        tparams = []
        belongs_to = ctx.parentCtx.TYPEID()[0].getText()
        for i in params:
            tparams.append((i.OBJECTID().getText(), i.TYPEID().getText()))
        self.fTable.add(ctx.OBJECTID().getText(), tparams, self.current_scope, ctx.TYPEID().getText(), belongs_to)
        self.current_scope -= 1
        return super().visitMethod(ctx)
    

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

    
    print(visitor.aTable.get_table())
    print(visitor.fTable.get_table())
    print(visitor.cTable.get_table())
    # print(output)

    # os.system(f"{JAVA_COM} {ANTLR} org.antlr.v4.Tool {ANTLR_FLAGS} -o {OUT_DIR} ./{GRAMMAR_NAME}/{GRAMMAR_NAME}.g4")
    # os.system(f"cd {OUT_DIR}/{GRAMMAR_NAME}; javac ./*.java; {JAVA_COM} {ANTLR}:{CLASSPATH} {G_PKG} {GRAMMAR_NAME} {START_RULE} ../../input/{file_name} {GRUN_FLAGS}")
    # os.system(f"rm -r ./{OUT_DIR}")
    

