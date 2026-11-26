# DSA Calculator

A simple Python calculator using a custom stack, the Shunting Yard algorithm and postfix evaluation.

## Features

- Addition, subtraction, multiplication and division
- Parentheses and operator precedence
- Negative and decimal numbers
- Input validation and error handling
- Graphical interface (GUI)
- Command-line interface (CLI)

## How to run

- GUI: `python main.py`
- CLI: `python main.py --cli`

## How to test

`python -m unittest discover -s tests -v`

## How it works

1. Convert the input into tokens.
2. Convert infix to postfix using a stack.
3. Evaluate postfix using another stack.
4. Display the result.

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)

Where n is the length of the input expression.