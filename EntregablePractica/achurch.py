from __future__ import annotations
from LambdaCalculusLexer import *
from LambdaCalculusListener import *
from LambdaCalculusVisitor import *
from LambdaCalculusParser import *
from types import NoneType
from typing import Dict
from antlr4 import InputStream
from antlr4 import CommonTokenStream, tree
from collections import deque
from typing import Set, Tuple
from dataclasses import dataclass
import copy
from uuid import uuid4
from telegram import Update
import pydot
from telegram.ext import Application as App, CommandHandler, ContextTypes, MessageHandler, filters

# Expression


@dataclass
class Variable:
    name: str


@dataclass
class Application:
    func: Expression
    arg: Expression


@dataclass
class Abstraction:
    var: Variable
    body: Expression


Expression = Abstraction | Application | Variable

# Visitor
macros = {}

# Visitor para generar el árbol semántico...


class MyVisitor(LambdaCalculusVisitor):
    def __init__(self, macros):
        self.macros = macros

    def visitApplication(self, ctx: LambdaCalculusParser.ApplicationContext):
        return Application(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitAbstraction(self, ctx: LambdaCalculusParser.AbstractionContext):
        vars = [Variable(var.getText()) for var in ctx.VAR()]

        body = self.visit(ctx.expression())
        for var in reversed(vars):
            body = Abstraction(var, body)

        return body

    def visitVariable(self, ctx: LambdaCalculusParser.VariableContext):
        return Variable(ctx.getText())

    def visitParenExpression(self, ctx: LambdaCalculusParser.ParenExpressionContext):
        return self.visit(ctx.expression())

    def visitMacroVar(self, ctx: LambdaCalculusParser.MacroVarContext):
        return self.macros[ctx.getText()]

    def visitMacroDefinition(self, ctx: LambdaCalculusParser.MacroDefinitionContext):
        macroVar = ctx.MACRO_VAR()
        if macroVar is None:
            macroVar = ctx.INFIX_MACRO_VAR()
        self.macros[macroVar.getText()] = self.visit(ctx.expression())
        return self.macros[macroVar.getText()]

    def visitInfixMacro(self, ctx: LambdaCalculusParser.InfixMacroContext):
        return Application(Application(self.macros[ctx.INFIX_MACRO_VAR().getText()], self.visit(ctx.expression(0))), self.visit(ctx.expression(1)))

# Function que convierte una expresión a un string, se llama print_expression porque originalmente la imprimia por pantalla, actualmente solo genera el string...


def print_expression(expr: Expression):
    if isinstance(expr, Variable):
        return expr.name
    elif isinstance(expr, Abstraction):
        return f"(λ{print_expression(expr.var)}.{print_expression(expr.body)})"
    elif isinstance(expr, Application):
        return f"({print_expression(expr.func)}{print_expression(expr.arg)})"

# De un string que representa una expresión devuelve el árbol semántico.


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

# Devuelve las macros definidas en el sistema.


def GetMacros() -> dict:
    return macros

#  Evaluator, sirve para evaluar expresiones.


class Evaluator:
    def __init__(self, max_reductions: int):
        self.max_reductions = max_reductions

    # Evalua una expresión, solo evalua un paso o ninguno. La tupla que devuelve tiene como primer parámetro la expresión
    # y como segudo parámetro "α" (alfa conversión), "β" (beta reduccion) o "None" si se puede hacer nada.
    def eval(self, term: Expression) -> Tuple[Expression, str]:
        return self.singleEval(term)

    # Evalua si una expresión contiene una variable.
    def occurs_in(self, expr: Expression, var: Variable) -> bool:
        if isinstance(expr, Variable):
            return expr == var
        elif isinstance(expr, Application):
            return self.occurs_in(expr.func, var) or self.occurs_in(expr.arg, var)
        elif isinstance(expr, Abstraction):
            return expr.var != var and self.occurs_in(expr.body, var)

    # Devuelve todas las varaibles que estan en una expresión
    def get_variables(self, expression: Expression) -> set:
        if isinstance(expression, Variable):
            return {expression.name}
        elif isinstance(expression, Application):
            return Evaluator.get_variables(expression.func) | Evaluator.get_variables(expression.arg)
        elif isinstance(expression, Abstraction):
            return {expression.var.name} | Evaluator.get_variables(expression.body)
        else:
            return set()

    #  Devuelve todos los nombres usados en una expresión.
    def get_used_names(self, expr: Expression) -> Set[str]:
        if isinstance(expr, Variable):
            return {expr.name}
        elif isinstance(expr, Application):
            return self.get_used_names(expr.func) | self.get_used_names(expr.arg)
        elif isinstance(expr, Abstraction):
            return {expr.var.name} | self.get_used_names(expr.body)
        else:
            return set()

    # Genera un nuevo nombre para una variable compatible con los que ya existen.
    def new_name(self, abstraction: Abstraction) -> str:
        used_names = self.get_used_names(abstraction)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char not in used_names:
                return char
        raise Exception("All variable names from a-z are already used!")

    #  Realiza una evaluación de un solo paso.
    def singleEval(self, term: Expression, r=0) -> Tuple[Expression, str]:
        if r > self.max_reductions:
            return term, "None"
        if isinstance(term, Variable):
            return term, "None"
        elif isinstance(term, Application):
            if isinstance(term.func, Abstraction):
                # Check if α-conversion is needed
                if isinstance(term.func.body, Abstraction) and self.alpha_conversion_needed(term.func.body, term.func.var, term.arg):
                    # α-conversion
                    converted_abstraction = self.alpha_convert(term.func)
                    return Application(converted_abstraction, term.arg), "α"
                else:
                    # β-reduction
                    replaced_term = self.substitute(
                        term.func.body, term.func.var, term.arg)
                    return replaced_term, "β"
            reduced_func, func_op = self.singleEval(term.func, r + 1)
            if (func_op != "None"):
                return Application(reduced_func, term.arg), func_op
            reduced_arg, arg_op = self.singleEval(term.arg, r + 1)
            if (arg_op != "None"):
                return Application(term.func, reduced_arg), arg_op
            else:
                return Application(reduced_func, reduced_arg), "None"
        elif isinstance(term, Abstraction):
            expr, operation = self.singleEval(term.body, r + 1)
            return Abstraction(term.var, expr), operation

    # Devuelve si la Abstracción necesita una alpha conversión para poder realizar una beta reduccion.
    def alpha_conversion_needed(self, body: Abstraction, var: Variable, val: Expression) -> bool:
        var_in_body = self.occurs_in(body.body, var) and body.var != var
        body_var_in_val = self.occurs_in(val, body.var)
        return var_in_body and body_var_in_val

    # Realiza una substitución de una expresión por una variable.
    def substitute(self, body: Expression, var: Variable, val: Expression) -> Expression:
        if isinstance(body, Variable):
            if body == var:
                return val
            else:
                return body
        elif isinstance(body, Application):
            return Application(self.substitute(body.func, var, val), self.substitute(body.arg, var, val))
        elif isinstance(body, Abstraction):
            if body.var == var:
                return body
            else:
                return Abstraction(body.var, self.substitute(body.body, var, val))

    # Realiza una alfa conversión.
    def alpha_convert(self, abstraction: Abstraction) -> Abstraction:
        new_var = Variable(self.new_name(abstraction))
        # Perform alpha conversion
        if isinstance(abstraction.body, Abstraction):
            abstraction = self.replace_variable(
                abstraction, abstraction.body.var.name, new_var.name)
        return abstraction

    # Permite renombrar variables de una expresión
    def replace_variable(self, expression: Expression, old_var_name: str, new_var_name: str) -> Expression:
        if isinstance(expression, Variable):
            if expression.name == old_var_name:
                return Variable(new_var_name)
            else:
                return expression
        elif isinstance(expression, Application):
            return Application(
                self.replace_variable(
                    expression.func, old_var_name, new_var_name),
                self.replace_variable(expression.arg, old_var_name, new_var_name))
        elif isinstance(expression, Abstraction):
            return Abstraction(
                Variable(
                    new_var_name) if expression.var.name == old_var_name else expression.var,
                self.replace_variable(expression.body, old_var_name, new_var_name))
        else:
            return expression

# TELEGRAM BOT


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f'AChurchBot!\nWelcome {user_name}!')


async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('AChurchBot!\n@ Fernando Gómez Navia, 2023')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('/start\n/author\n/help\n/macros\nλ-Calculus expression!')


async def macros_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    macros = GetMacros()
    if len(macros) == 0:
        macro_message = "There are no defined macros!"
    else:
        macro_message = '\n'.join(
            f'{k}≡{print_expression(v)}' for k, v in macros.items())
    await context.bot.send_message(chat_id=update.message.chat_id, text=macro_message)

# Procesa una expresión. Se podria simplificar bastante este código.


async def process_expression(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    expression_str = update.message.text
    response_str = process(expression_str)
    await context.bot.send_message(chat_id=update.message.chat_id, text=print_expression(response_str))
    draw_tree(response_str, "tree.png")
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=open('tree.png', 'rb'))
    tree_copy = copy.deepcopy(response_str)
    evaluator = Evaluator(200)
    prev_expr = copy.deepcopy(tree_copy)
    expr, operator = evaluator.eval(tree_copy)
    if operator != "None":
        count = 1
    else:
        count = 0

    while operator != "None":
        str_prev_expr = print_expression(prev_expr)
        str_expr = print_expression(expr)
        if str_prev_expr == str_expr:
            break
        text = f"{str_prev_expr} -> {operator} -> {str_expr}"
        await context.bot.send_message(chat_id=update.message.chat_id, text=text)

        prev_expr = copy.deepcopy(expr)
        expr, operator = evaluator.eval(expr)
        if operator != "None":
            count += 1

    if count == 0:
        await context.bot.send_message(chat_id=update.message.chat_id, text="The expression is irreducible!")
    else:
        await context.bot.send_message(chat_id=update.message.chat_id, text=print_expression(expr))
        draw_tree(expr, "tree.png")
        await context.bot.send_photo(chat_id=update.message.chat_id, photo=open('tree.png', 'rb'))


def telegram_bot(token: str) -> None:
    application = App.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("author", author))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("macros", macros_command))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, process_expression))

    application.run_polling()


def generate_graph(node, graph=None, parent_node=None):
    if graph is None:
        graph = pydot.Dot(graph_type='digraph')

    if isinstance(node, Variable):
        var_node = pydot.Node(str(uuid4()), label=node.name, shape='ellipse')
        graph.add_node(var_node)
        if parent_node:
            graph.add_edge(pydot.Edge(parent_node, var_node))

    elif isinstance(node, Application):
        app_node = pydot.Node(str(uuid4()), label='@', shape='rectangle')
        graph.add_node(app_node)
        if parent_node:
            graph.add_edge(pydot.Edge(parent_node, app_node))
        generate_graph(node.func, graph, app_node)
        generate_graph(node.arg, graph, app_node)

    elif isinstance(node, Abstraction):
        abs_node = pydot.Node(
            str(uuid4()), label=f'λ{node.var.name}', shape='diamond')
        graph.add_node(abs_node)
        if parent_node:
            graph.add_edge(pydot.Edge(parent_node, abs_node))
        generate_graph(node.body, graph, abs_node)
        mark_bound_variables(graph, abs_node, node.var.name, abs_node)

    return graph


def mark_bound_variables(graph, abs_node, var_name, current):
    for edge in graph.get_edges():
        if edge.get_source() == current.get_name():
            target_node = graph.get_node(edge.get_destination())[0]
            if target_node.get_label() == var_name:
                graph.add_edge(pydot.Edge(
                    target_node, abs_node, style='dashed'))
            elif target_node.get_shape() == 'rectangle' or target_node.get_shape() == 'diamond':
                mark_bound_variables(graph, abs_node, var_name, target_node)


def draw_tree(tree, filename):
    graph = generate_graph(tree)
    graph.write(filename, format='png')


def main():
    telegram_bot("5865283700:AAGhUlfWX8xjb29SlY1qw8B-UIgnpFOnJ7A")


if __name__ == '__main__':
    main()
