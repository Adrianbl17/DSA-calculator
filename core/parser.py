from core.stack import Stack
from utils.helpers import is_number

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "u-": 3, "u+": 3}


def handle_closing_parenthesis(operators, output):
    while not operators.is_empty() and operators.peek() != "(":
        output.append(operators.pop())

    if operators.is_empty():
        raise ValueError("Unmatched closing parenthesis")

    operators.pop()


def handle_unary_operator(token, operators):
    operators.push("u" + token)


def handle_operator(token, operators, output):
    # Pop operators of equal or higher precedence for left associativity.
    while (
        not operators.is_empty()
        and operators.peek() != "("
        and PRECEDENCE[operators.peek()] >= PRECEDENCE[token]
    ):
        output.append(operators.pop())

    operators.push(token)


def empty_stack(operators, output):
    while not operators.is_empty():
        token = operators.pop()

        if token == "(":
            raise ValueError("Unmatched opening parenthesis")

        output.append(token)


def infix_to_postfix(tokens):
    output = []
    operators = Stack()
    expect_operand = True

    for token in tokens:
        if is_number(token):
            if not expect_operand:
                raise ValueError("Missing operator")

            output.append(token)
            expect_operand = False

        elif token == "(":
            if not expect_operand:
                raise ValueError("Missing operator before parenthesis")

            operators.push(token)
            expect_operand = True

        elif token == ")":
            if expect_operand:
                raise ValueError("Missing operand")

            handle_closing_parenthesis(operators, output)
            expect_operand = False

        elif expect_operand and token in ("+", "-"):
            handle_unary_operator(token, operators)

        elif token in ("+", "-", "*", "/"):
            if expect_operand:
                raise ValueError("Missing operand")

            handle_operator(token, operators, output)
            expect_operand = True

        else:
            raise ValueError("Unknown token")

    if expect_operand:
        raise ValueError("Missing operand")

    empty_stack(operators, output)
    return output
