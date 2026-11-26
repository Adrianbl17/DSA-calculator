# DSA Calculator

A simple Python calculator using stacks and the Shunting Yard algorithm.

## Features

- Addition, subtraction, multiplication and division
- Parentheses and operator precedence
- Negative and decimal numbers
- Input validation and error handling

## How to run

python main.py

## How to test

python -m unittest -v

## How it works

1. Convert the input into tokens.
2. Convert infix to postfix using a stack.
3. Evaluate postfix using another stack.
4. Display the result.

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)