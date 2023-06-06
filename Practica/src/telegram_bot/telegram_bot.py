import copy
from uuid import uuid4
from telegram import Update
from visitors.visitor import GetMacros, process, print_expression
import pydot
from evaluator.evaluator import *
from telegram.ext import Application as App, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name 
    await update.message.reply_text(f'AChurchBot!\nWelcome {user_name}!')

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('AChurchBot!\n@ Fernando Gómez Navia, 2023')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('/start\n/author\n/help\n/macros\nλ-Calculus expression!')

async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    macros = GetMacros()
    if len(macros) == 0:
        macro_message = "There are no defined macros!"
    else:
        macro_message = '\n'.join(f'{k}≡{print_expression(v)}' for k, v in macros.items())
    await context.bot.send_message(chat_id=update.message.chat_id, text=macro_message)

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
    else: count = 0

    while operator != "None":
        str_prev_expr = print_expression(prev_expr)
        str_expr = print_expression(expr)
        if str_prev_expr == str_expr: 
            break
        text = f"{str_prev_expr} -> {operator} -> {str_expr}"
        await context.bot.send_message(chat_id=update.message.chat_id, text=text)

        prev_expr = copy.deepcopy(expr)
        expr, operator = evaluator.eval(expr)
        if operator != "None": count += 1
    
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
    application.add_handler(CommandHandler("macros", macros))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_expression))

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
        abs_node = pydot.Node(str(uuid4()), label=f'λ{node.var.name}', shape='diamond')
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
                graph.add_edge(pydot.Edge(target_node, abs_node, style='dashed'))
            elif target_node.get_shape() == 'rectangle' or target_node.get_shape() == 'diamond':
                mark_bound_variables(graph, abs_node, var_name, target_node)

def draw_tree(tree, filename):
    graph = generate_graph(tree)
    graph.write(filename, format='png')