# Generated from LambdaCalculus.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

# This class defines a complete listener for a parse tree produced by LambdaCalculusParser.
class LambdaCalculusListener(ParseTreeListener):

    # Enter a parse tree produced by LambdaCalculusParser#application.
    def enterApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#application.
    def exitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#abstraction.
    def enterAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#abstraction.
    def exitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#variable.
    def enterVariable(self, ctx:LambdaCalculusParser.VariableContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#variable.
    def exitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#parenExpression.
    def enterParenExpression(self, ctx:LambdaCalculusParser.ParenExpressionContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#parenExpression.
    def exitParenExpression(self, ctx:LambdaCalculusParser.ParenExpressionContext):
        pass



del LambdaCalculusParser