from tokenizer import tokenize
from parser import infix_to_postfix
from evaluator import evaluate_postfix


def calculate(expression):
    tokens = tokenize(expression)
    postfix = infix_to_postfix(tokens)
    
    return evaluate_postfix(postfix)