from calculator import calculate


def main():
    print('===== DSA CALCULATOR =====')
    print('Operators: + - * / ( ) | Type exit to quit')

    while True:
        try:
            expression = input('\nEnter expression: ')
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            break

        if expression.strip().lower() == 'exit':
            print('Goodbye!')
            break

        try:
            result, postfix = calculate(expression, show_postfix=True)

            print('Postfix:', ' '.join(str(t) for t in postfix))
            print(f'Result: {result:.10g}')

        except ValueError as error:
            print('Error:', error)


if __name__ == '__main__':
    main()