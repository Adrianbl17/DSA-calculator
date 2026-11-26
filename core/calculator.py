from core.evaluator import evaluate_postfix
from core.parser import infix_to_postfix
from core.tokenizer import tokenize


def calculate(expression, show_postfix=False):
    tokens = tokenize(expression)
    postfix = infix_to_postfix(tokens)
    result = evaluate_postfix(postfix)

    if show_postfix:
        return result, postfix

    return result
