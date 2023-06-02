
from evaluator.evaluator import Evaluator
from visitors.visitor import process, print_expression

def main():
    while True:
        try:
            input_str = input('AChurch> ')
            if input_str == 'quit':
                break

            # Genera el AST
            tree = process(input_str)
            # print(print_expression(tree))
            evaluator = Evaluator(400)
            evaluated_tree = evaluator.eval(tree)
            # Imprime el AST
            print(print_expression(evaluated_tree))

        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
