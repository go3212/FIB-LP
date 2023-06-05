import uuid
from telegram import ForceReply, Update
from visitors.visitor import process, print_expression
import pydot
from evaluator.evaluator import *
from telegram.ext import Application as App, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Bienvenido al AChurch Bot!')

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('AChurch Bot desarrollado por Fernando Gómez Navia.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Aqui hi ha algunes instruccions...')

async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Aquí tens les macros actualment definides...')

async def process_expression(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Obtén la expressió del missatge entrant
    expression_str = update.message.text
    # Processa la expressió
    response_str = process(expression_str)  # Assumeix que teniu una funció process que es pot cridar
    await context.bot.send_message(chat_id=update.message.chat_id, text=print_expression(response_str))
    draw_tree(response_str, "tree.png")
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=open('tree.png', 'rb'))
    tree_copy = copy.deepcopy(response_str)
    # print(print_expression(tree))
    evaluator = Evaluator(200)
    # initial evaluation
    prev_expr = copy.deepcopy(tree_copy)
    expr, operator = evaluator.eval(tree_copy)

    # evaluation loop
    while operator != "None":
        str_prev_expr = print_expression(prev_expr)
        str_expr = print_expression(expr)
        if str_prev_expr == str_expr: 
            break
        text = f"{str_prev_expr} -> {operator} -> {str_expr}"
        await context.bot.send_message(chat_id=update.message.chat_id, text=text)
        draw_tree(expr, "tree.png")
        await context.bot.send_photo(chat_id=update.message.chat_id, photo=open('tree.png', 'rb'))
        prev_expr = copy.deepcopy(expr)
        expr, operator = evaluator.eval(expr)

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
        graph = pydot.Dot(graph_type='graph')

    if isinstance(node, Variable):
        var_node = pydot.Node(str(id(node)), label=node.name, shape='ellipse')
        graph.add_node(var_node)

    elif isinstance(node, Application):
        app_node = pydot.Node(str(id(node)), label='@', shape='rectangle')
        graph.add_node(app_node)
        if parent_node:
            graph.add_edge(pydot.Edge(parent_node, app_node))
        generate_graph(node.func, graph, app_node)
        generate_graph(node.arg, graph, app_node)

    elif isinstance(node, Abstraction):
        abs_node = pydot.Node(str(id(node)), label='λ', shape='diamond')
        graph.add_node(abs_node)
        if parent_node:
            graph.add_edge(pydot.Edge(parent_node, abs_node))
        var_node = pydot.Node(str(id(node.var)), label=node.var.name, shape='ellipse')
        graph.add_node(var_node)
        graph.add_edge(pydot.Edge(abs_node, var_node, style='dashed'))
        generate_graph(node.body, graph, abs_node)

    return graph


def draw_tree(tree, filename):
    graph = generate_graph(tree)
    graph.write(filename, format='png')

