# Generated from LambdaCalculus.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

# This class defines a complete generic visitor for a parse tree produced by LambdaCalculusParser.

class LambdaCalculusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#parenExpression.
    def visitParenExpression(self, ctx:LambdaCalculusParser.ParenExpressionContext):
        return self.visitChildren(ctx)



del LambdaCalculusParser