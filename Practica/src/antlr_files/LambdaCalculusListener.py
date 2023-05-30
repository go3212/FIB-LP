# Generated from LambdaCalculus.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

# This class defines a complete listener for a parse tree produced by LambdaCalculusParser.
class LambdaCalculusListener(ParseTreeListener):

    # Enter a parse tree produced by LambdaCalculusParser#expression.
    def enterExpression(self, ctx:LambdaCalculusParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#expression.
    def exitExpression(self, ctx:LambdaCalculusParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#lambda.
    def enterLambda(self, ctx:LambdaCalculusParser.LambdaContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#lambda.
    def exitLambda(self, ctx:LambdaCalculusParser.LambdaContext):
        pass



del LambdaCalculusParser