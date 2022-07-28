# Generated from YAPL/YAPL.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#klass.
    def enterKlass(self, ctx:YAPLParser.KlassContext):
        pass

    # Exit a parse tree produced by YAPLParser#klass.
    def exitKlass(self, ctx:YAPLParser.KlassContext):
        pass


    # Enter a parse tree produced by YAPLParser#method.
    def enterMethod(self, ctx:YAPLParser.MethodContext):
        pass

    # Exit a parse tree produced by YAPLParser#method.
    def exitMethod(self, ctx:YAPLParser.MethodContext):
        pass


    # Enter a parse tree produced by YAPLParser#attr.
    def enterAttr(self, ctx:YAPLParser.AttrContext):
        pass

    # Exit a parse tree produced by YAPLParser#attr.
    def exitAttr(self, ctx:YAPLParser.AttrContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#let_formal.
    def enterLet_formal(self, ctx:YAPLParser.Let_formalContext):
        pass

    # Exit a parse tree produced by YAPLParser#let_formal.
    def exitLet_formal(self, ctx:YAPLParser.Let_formalContext):
        pass


    # Enter a parse tree produced by YAPLParser#minus.
    def enterMinus(self, ctx:YAPLParser.MinusContext):
        pass

    # Exit a parse tree produced by YAPLParser#minus.
    def exitMinus(self, ctx:YAPLParser.MinusContext):
        pass


    # Enter a parse tree produced by YAPLParser#dispatch.
    def enterDispatch(self, ctx:YAPLParser.DispatchContext):
        pass

    # Exit a parse tree produced by YAPLParser#dispatch.
    def exitDispatch(self, ctx:YAPLParser.DispatchContext):
        pass


    # Enter a parse tree produced by YAPLParser#str_const.
    def enterStr_const(self, ctx:YAPLParser.Str_constContext):
        pass

    # Exit a parse tree produced by YAPLParser#str_const.
    def exitStr_const(self, ctx:YAPLParser.Str_constContext):
        pass


    # Enter a parse tree produced by YAPLParser#mul.
    def enterMul(self, ctx:YAPLParser.MulContext):
        pass

    # Exit a parse tree produced by YAPLParser#mul.
    def exitMul(self, ctx:YAPLParser.MulContext):
        pass


    # Enter a parse tree produced by YAPLParser#isvoid.
    def enterIsvoid(self, ctx:YAPLParser.IsvoidContext):
        pass

    # Exit a parse tree produced by YAPLParser#isvoid.
    def exitIsvoid(self, ctx:YAPLParser.IsvoidContext):
        pass


    # Enter a parse tree produced by YAPLParser#selfdispatch.
    def enterSelfdispatch(self, ctx:YAPLParser.SelfdispatchContext):
        pass

    # Exit a parse tree produced by YAPLParser#selfdispatch.
    def exitSelfdispatch(self, ctx:YAPLParser.SelfdispatchContext):
        pass


    # Enter a parse tree produced by YAPLParser#while.
    def enterWhile(self, ctx:YAPLParser.WhileContext):
        pass

    # Exit a parse tree produced by YAPLParser#while.
    def exitWhile(self, ctx:YAPLParser.WhileContext):
        pass


    # Enter a parse tree produced by YAPLParser#div.
    def enterDiv(self, ctx:YAPLParser.DivContext):
        pass

    # Exit a parse tree produced by YAPLParser#div.
    def exitDiv(self, ctx:YAPLParser.DivContext):
        pass


    # Enter a parse tree produced by YAPLParser#neg.
    def enterNeg(self, ctx:YAPLParser.NegContext):
        pass

    # Exit a parse tree produced by YAPLParser#neg.
    def exitNeg(self, ctx:YAPLParser.NegContext):
        pass


    # Enter a parse tree produced by YAPLParser#paren.
    def enterParen(self, ctx:YAPLParser.ParenContext):
        pass

    # Exit a parse tree produced by YAPLParser#paren.
    def exitParen(self, ctx:YAPLParser.ParenContext):
        pass


    # Enter a parse tree produced by YAPLParser#not.
    def enterNot(self, ctx:YAPLParser.NotContext):
        pass

    # Exit a parse tree produced by YAPLParser#not.
    def exitNot(self, ctx:YAPLParser.NotContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessThan.
    def enterLessThan(self, ctx:YAPLParser.LessThanContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessThan.
    def exitLessThan(self, ctx:YAPLParser.LessThanContext):
        pass


    # Enter a parse tree produced by YAPLParser#let.
    def enterLet(self, ctx:YAPLParser.LetContext):
        pass

    # Exit a parse tree produced by YAPLParser#let.
    def exitLet(self, ctx:YAPLParser.LetContext):
        pass


    # Enter a parse tree produced by YAPLParser#block.
    def enterBlock(self, ctx:YAPLParser.BlockContext):
        pass

    # Exit a parse tree produced by YAPLParser#block.
    def exitBlock(self, ctx:YAPLParser.BlockContext):
        pass


    # Enter a parse tree produced by YAPLParser#id.
    def enterId(self, ctx:YAPLParser.IdContext):
        pass

    # Exit a parse tree produced by YAPLParser#id.
    def exitId(self, ctx:YAPLParser.IdContext):
        pass


    # Enter a parse tree produced by YAPLParser#if.
    def enterIf(self, ctx:YAPLParser.IfContext):
        pass

    # Exit a parse tree produced by YAPLParser#if.
    def exitIf(self, ctx:YAPLParser.IfContext):
        pass


    # Enter a parse tree produced by YAPLParser#case.
    def enterCase(self, ctx:YAPLParser.CaseContext):
        pass

    # Exit a parse tree produced by YAPLParser#case.
    def exitCase(self, ctx:YAPLParser.CaseContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessThanOrEqualTo.
    def enterLessThanOrEqualTo(self, ctx:YAPLParser.LessThanOrEqualToContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessThanOrEqualTo.
    def exitLessThanOrEqualTo(self, ctx:YAPLParser.LessThanOrEqualToContext):
        pass


    # Enter a parse tree produced by YAPLParser#add.
    def enterAdd(self, ctx:YAPLParser.AddContext):
        pass

    # Exit a parse tree produced by YAPLParser#add.
    def exitAdd(self, ctx:YAPLParser.AddContext):
        pass


    # Enter a parse tree produced by YAPLParser#new.
    def enterNew(self, ctx:YAPLParser.NewContext):
        pass

    # Exit a parse tree produced by YAPLParser#new.
    def exitNew(self, ctx:YAPLParser.NewContext):
        pass


    # Enter a parse tree produced by YAPLParser#bool_true.
    def enterBool_true(self, ctx:YAPLParser.Bool_trueContext):
        pass

    # Exit a parse tree produced by YAPLParser#bool_true.
    def exitBool_true(self, ctx:YAPLParser.Bool_trueContext):
        pass


    # Enter a parse tree produced by YAPLParser#eq.
    def enterEq(self, ctx:YAPLParser.EqContext):
        pass

    # Exit a parse tree produced by YAPLParser#eq.
    def exitEq(self, ctx:YAPLParser.EqContext):
        pass


    # Enter a parse tree produced by YAPLParser#int_const.
    def enterInt_const(self, ctx:YAPLParser.Int_constContext):
        pass

    # Exit a parse tree produced by YAPLParser#int_const.
    def exitInt_const(self, ctx:YAPLParser.Int_constContext):
        pass


    # Enter a parse tree produced by YAPLParser#bool_false.
    def enterBool_false(self, ctx:YAPLParser.Bool_falseContext):
        pass

    # Exit a parse tree produced by YAPLParser#bool_false.
    def exitBool_false(self, ctx:YAPLParser.Bool_falseContext):
        pass


    # Enter a parse tree produced by YAPLParser#assign.
    def enterAssign(self, ctx:YAPLParser.AssignContext):
        pass

    # Exit a parse tree produced by YAPLParser#assign.
    def exitAssign(self, ctx:YAPLParser.AssignContext):
        pass


