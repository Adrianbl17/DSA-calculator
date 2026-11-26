from stack import Stack

PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, 'u-': 3, 'u+': 3}


def is_number(token):
    return isinstance(token, (int, float))


def handle_closing_parenthesis(operators, output):
    while operators.peek() != '(':
        output.append(operators.pop())

    operators.pop()


def handle_unary_operator(token, operators):
    operators.push('u' + token)


def handle_operator(token, operators, output):
    while (not operators.is_empty()
           and operators.peek() != '('
           and PRECEDENCE[operators.peek()] >= PRECEDENCE[token]):

        output.append(operators.pop())

    operators.push(token)


def empty_stack(operators, output):
    while not operators.is_empty():
        output.append(operators.pop())


def infix_to_postfix(tokens):
    output = []
    operators = Stack()
    expect_operand = True

    for token in tokens:

        if is_number(token):
            output.append(token)
            expect_operand = False

        elif token == '(':
            operators.push(token)
            expect_operand = True

        elif token == ')':
            handle_closing_parenthesis(operators, output)
            expect_operand = False

        elif expect_operand and token in ('+', '-'):
            handle_unary_operator(token, operators)

        else:
            handle_operator(token, operators, output)
            expect_operand = True

    empty_stack(operators, output)

    return output