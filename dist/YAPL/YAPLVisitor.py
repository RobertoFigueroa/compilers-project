# Generated from YAPL/YAPL.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#klass.
    def visitKlass(self, ctx:YAPLParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#attr.
    def visitAttr(self, ctx:YAPLParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#let_formal.
    def visitLet_formal(self, ctx:YAPLParser.Let_formalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#minus.
    def visitMinus(self, ctx:YAPLParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#dispatch.
    def visitDispatch(self, ctx:YAPLParser.DispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#str_const.
    def visitStr_const(self, ctx:YAPLParser.Str_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#mul.
    def visitMul(self, ctx:YAPLParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#isvoid.
    def visitIsvoid(self, ctx:YAPLParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#selfdispatch.
    def visitSelfdispatch(self, ctx:YAPLParser.SelfdispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#div.
    def visitDiv(self, ctx:YAPLParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#neg.
    def visitNeg(self, ctx:YAPLParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#paren.
    def visitParen(self, ctx:YAPLParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThan.
    def visitLessThan(self, ctx:YAPLParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#let.
    def visitLet(self, ctx:YAPLParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#block.
    def visitBlock(self, ctx:YAPLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#if.
    def visitIf(self, ctx:YAPLParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#case.
    def visitCase(self, ctx:YAPLParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThanOrEqualTo.
    def visitLessThanOrEqualTo(self, ctx:YAPLParser.LessThanOrEqualToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#new.
    def visitNew(self, ctx:YAPLParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#bool_true.
    def visitBool_true(self, ctx:YAPLParser.Bool_trueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#eq.
    def visitEq(self, ctx:YAPLParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#int_const.
    def visitInt_const(self, ctx:YAPLParser.Int_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#bool_false.
    def visitBool_false(self, ctx:YAPLParser.Bool_falseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#assign.
    def visitAssign(self, ctx:YAPLParser.AssignContext):
        return self.visitChildren(ctx)



del YAPLParser