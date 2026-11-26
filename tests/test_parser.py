import unittest

from core.parser import infix_to_postfix
from core.tokenizer import tokenize


class ParserTests(unittest.TestCase):
    def test_operator_precedence(self):
        self.assertEqual(
            infix_to_postfix(tokenize("2+3*4")),
            [2.0, 3.0, 4.0, "*", "+"],
        )

    def test_parentheses_and_nested_parentheses(self):
        self.assertEqual(
            infix_to_postfix(tokenize("(2+3)*4")),
            [2.0, 3.0, "+", 4.0, "*"],
        )
        self.assertEqual(
            infix_to_postfix(tokenize("2*(3+(4*5))")),
            [2.0, 3.0, 4.0, 5.0, "*", "+", "*"],
        )

    def test_left_associativity(self):
        self.assertEqual(
            infix_to_postfix(tokenize("10-3-2")),
            [10.0, 3.0, "-", 2.0, "-"],
        )
        self.assertEqual(
            infix_to_postfix(tokenize("8/4/2")),
            [8.0, 4.0, "/", 2.0, "/"],
        )

    def test_unary_operators(self):
        self.assertEqual(
            infix_to_postfix(tokenize("-2*-3")),
            [2.0, "u-", 3.0, "u-", "*"],
        )

    def test_rejects_invalid_expression_structure(self):
        for expression in ("5+", "()", "2 3", "2(3)", "2+*3", "2+3)"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    infix_to_postfix(tokenize(expression))


if __name__ == "__main__":
    unittest.main()
