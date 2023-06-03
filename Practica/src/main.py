
import copy
from evaluator.evaluator import Evaluator
from telegram_bot.telegram_bot import *
from visitors.visitor import process, print_expression

def main():
    # telegram_bot("5865283700:AAGhUlfWX8xjb29SlY1qw8B-UIgnpFOnJ7A")
    while True:
        try:
            input_str = input('AChurch> ')
            if input_str == 'quit':
                break

            # Genera el AST
            tree = process(input_str)
            tree_copy = copy.deepcopy(tree)
            # print(print_expression(tree))
            evaluator = Evaluator(400)
            evaluated_tree = evaluator.eval(tree_copy)


            print("Result:")
            print(print_expression(evaluated_tree))

        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
