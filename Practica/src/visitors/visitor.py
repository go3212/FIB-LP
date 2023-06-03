
from antlr4 import InputStream
from antlr_files.LambdaCalculusVisitor import LambdaCalculusVisitor
from antlr_files.LambdaCalculusLexer import LambdaCalculusLexer
from antlr_files.LambdaCalculusListener import LambdaCalculusListener
from antlr_files.LambdaCalculusParser import LambdaCalculusParser
from custom_dataclasses.expression import Abstraction, Application, Expression, Macro, Variable
from antlr4 import CommonTokenStream, tree

macros = {}


class MyVisitor(LambdaCalculusVisitor):
    def __init__(self, macros):
        self.macros = macros

    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        return Application(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        # Create a list of Variable instances from the abstraction context.
        vars = [Variable(var.getText()) for var in ctx.VAR()]
        
        # Create a nested abstraction for each variable
        body = self.visit(ctx.expression())
        for var in reversed(vars):
            body = Abstraction(var, body)
            
        return body

    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        return Variable(ctx.getText())

    # Visit a parse tree produced by LambdaCalculusParser#parenExpression.
    def visitParenExpression(self, ctx:LambdaCalculusParser.ParenExpressionContext):
        return self.visit(ctx.expression())

    # Rest of your visitor methods...
    def visitMacroVar(self, ctx:LambdaCalculusParser.MacroVarContext):
        # This assumes you have a dictionary somewhere mapping macro names to their definitions.
        # You would need to replace "macros" with your actual macro dictionary.
        return self.macros[ctx.getText()]

    def visitMacroDefinition(self, ctx:LambdaCalculusParser.MacroDefinitionContext):
        # Again, replace "macros" with your actual macro dictionary.
        self.macros[ctx.MACRO_VAR().getText()] = self.visit(ctx.expression())
        return self.macros[ctx.MACRO_VAR().getText()]

    def visitInfixMacro(self, ctx:LambdaCalculusParser.InfixMacroContext):
        # Treat the infix macro as an application of the macro to the two arguments.
        return Application(Application(Macro(ctx.MACRO_VAR().getText()), self.visit(ctx.expression(0))), self.visit(ctx.expression(1)))
    
def print_expression(expr: Expression):
    if isinstance(expr, Variable):
        return expr.name
    elif isinstance(expr, Abstraction):
        return f"(λ{print_expression(expr.var)}.{print_expression(expr.body)})"
    elif isinstance(expr, Application):
        return f"({print_expression(expr.func)}{print_expression(expr.arg)})"

def process(input_str: str):
    # Convertir el string de entrada a un flujo de tokens
    input_stream = InputStream(input_str)
    lexer = LambdaCalculusLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Generar el AST con el parser
    parser = LambdaCalculusParser(token_stream)
    tree = parser.expression()
    # print(tree.toStringTree(recog=parser))
    # Crear un visitante y usarlo para convertir el AST en un árbol semántico
    visitor = MyVisitor(macros)
    semantic_tree = visitor.visit(tree)

    return semantic_tree