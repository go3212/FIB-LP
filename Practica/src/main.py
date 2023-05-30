
from visitors.visitor import process

def main():
    while True:
        try:
            input_str = input('AChurch> ')
            if input_str == 'quit':
                break

            # Genera el AST
            tree = process(input_str)
            # Imprime el AST
            print(tree)

        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
