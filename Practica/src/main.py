
import copy
from evaluator.evaluator import Evaluator
from telegram_bot.telegram_bot import *
from visitors.visitor import process, print_expression

def main():
    telegram_bot("5865283700:AAGhUlfWX8xjb29SlY1qw8B-UIgnpFOnJ7A")
    while True:
        try:
            input_str = input('AChurch> ')
            if input_str == 'quit':
                break

            # Genera el AST
            tree = process(input_str)
            tree_copy = copy.deepcopy(tree)
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
                print(f"{str_prev_expr} -> {operator} -> {str_expr}")
                prev_expr = copy.deepcopy(expr)
                expr, operator = evaluator.eval(expr)


            print("Result:")
            print(print_expression(expr))

        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
