import sys
from antlr4 import *
from dist.YAPL import YAPLLexer
from dist.YAPL import YAPLParser
from dist.YAPL import YAPLVisitor

#antlr4 -Dlanguage=Python3 YAPL/YAPL.g4 -visitor -o dist

if __name__ == "__main__":

    dir_file = input("Ingrese el directorio en donde se encuentra el programa YAPL >>")
    data = InputStream(dir_file)

