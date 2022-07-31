import os
from antlr4 import *
from dist.YAPL.YAPLLexer import YAPLLexer
from dist.YAPL.YAPLParser import YAPLParser
from dist.YAPL.YAPLVisitor import YAPLVisitor

#antlr4 -Dlanguage=Python3 YAPL/YAPL.g4 -visitor -o dist

if __name__ == "__main__":

    dir_file = input("Ingrese el directorio en donde se encuentra el programa YAPL >>")
    # TODO: Check if file exists
    _file = open(dir_file)
    str_file = _file.read()
    _file.close()
    data = InputStream(str_file)
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    parser = YAPLParser(stream)
    tree = parser.program()
    
    visitor = YAPLVisitor()
    output = visitor.visit(tree)
    
    print(output)

    # os.system("make compile")
    # os.system("make run")
    # os.system("make clean")
    

    

