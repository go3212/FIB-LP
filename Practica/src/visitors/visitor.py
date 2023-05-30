
from contextlib import AbstractContextManager
from wsgiref.types import InputStream
from antlr_files.LambdaCalculusLexer import LambdaCalculusLexer
from antlr_files.LambdaCalculusListener import LambdaCalculusListener
from antlr_files.LambdaCalculusParser import LambdaCalculusParser
from custom_dataclasses.expression import Application, Variable



class MyVisitor(LambdaCalculusListener):
    def visitVariable(self, ctx):
        return Variable(ctx.getText())

    def visitApplication(self, ctx):
        return Application(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitLambda(self, ctx):
        return AbstractContextManager(Variable(ctx.VARIABLE().getText()), self.visit(ctx.expression()))

def process(input_str):
    lexer = LambdaCalculusLexer(InputStream(input_str))
    parser = LambdaCalculusParser(CommonTokenStream(lexer))
    tree = parser.expression()
    visitor = MyVisitor()
    return visitor.visit(tree)
