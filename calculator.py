from tokenizer import tokenize
from parser import infix_to_postfix
from evaluator import evaluate_postfix


def calculate(expression, show_postfix=False):
    tokens = tokenize(expression)
    postfix = infix_to_postfix(tokens)
    result = evaluate_postfix(postfix)

    if show_postfix:
        return result, postfix

    return result