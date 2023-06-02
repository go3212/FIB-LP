
from antlr4 import InputStream
from antlr_files.LambdaCalculusVisitor import LambdaCalculusVisitor
from antlr_files.LambdaCalculusLexer import LambdaCalculusLexer
from antlr_files.LambdaCalculusListener import LambdaCalculusListener
from antlr_files.LambdaCalculusParser import LambdaCalculusParser
from custom_dataclasses.expression import Abstraction, Application, Expression, Variable
from antlr4 import CommonTokenStream

class MyVisitor(LambdaCalculusVisitor):
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        return Application(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        return Abstraction(Variable(ctx.VAR().getText()), self.visit(ctx.expression()))

    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        return Variable(ctx.getText())

    # Visit a parse tree produced by LambdaCalculusParser#parenExpression.
    def visitParenExpression(self, ctx:LambdaCalculusParser.ParenExpressionContext):
        return self.visitChildren(ctx)

def print_expression(expr: Expression):
    if isinstance(expr, Variable):
        return expr.name
    elif isinstance(expr, Abstraction):
        return f"(\\{print_expression(expr.variable)}.{print_expression(expr.body)})"
    elif isinstance(expr, Application):
        return f"({print_expression(expr.function)} {print_expression(expr.argument)})"

def process(input_str: str):
    # Convertir el string de entrada a un flujo de tokens
    input_stream = InputStream(input_str)
    lexer = LambdaCalculusLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Generar el AST con el parser
    parser = LambdaCalculusParser(token_stream)
    tree = parser.expression()

    print("{}".format(tree.toStringTree(recog=parser)))

    # Crear un visitante y usarlo para convertir el AST en un árbol semántico
    visitor = MyVisitor()
    semantic_tree = visitor.visit(tree)

    return semantic_tree