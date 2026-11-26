from core.stack import Stack
from utils.helpers import is_number


def apply_operator(left, right, operator):
    if operator == "+":
        return left + right

    if operator == "-":
        return left - right

    if operator == "*":
        return left * right

    if operator == "/":
        if right == 0:
            raise ValueError("Division by zero")

        return left / right

    raise ValueError("Unknown operator")


def handle_unary_operator(token, operands):
    if operands.is_empty():
        raise ValueError("Missing operand")

    value = operands.pop()

    if token == "u-":
        operands.push(-value)
    else:
        operands.push(value)


def handle_binary_operator(token, operands):
    if operands.size() < 2:
        raise ValueError("Missing operands")

    right = operands.pop()
    left = operands.pop()
    result = apply_operator(left, right, token)
    operands.push(result)


def evaluate_postfix(tokens):
    operands = Stack()

    for token in tokens:
        if is_number(token):
            operands.push(token)
        elif token in ("u-", "u+"):
            handle_unary_operator(token, operands)
        else:
            handle_binary_operator(token, operands)

    if operands.size() != 1:
        raise ValueError("Invalid expression")

    return operands.pop()
