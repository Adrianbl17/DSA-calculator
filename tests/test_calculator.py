import unittest

from core.calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_valid_expressions(self):
        cases = [
            ("5+3", 8),
            ("10-4", 6),
            ("5*4", 20),
            ("20/4", 5),
            ("2+3*4", 14),
            ("(2+3)*4", 20),
            ("2*(3+(4*5))", 46),
            ("2.5+1.5", 4),
            ("-5+3", -2),
            ("10-3-2", 5),
            ("0", 0),
            ("8/4/2", 1),
            ("2*-3", -6),
            ("-(2+3)", -5),
            ("--2", 2),
            ("12+34", 46),
            ("  3  ", 3),
            ("1/2", 0.5),
        ]
        for expression, expected in cases:
            with self.subTest(expression=expression):
                self.assertAlmostEqual(calculate(expression), expected)

    def test_show_postfix_returns_result_and_tokens(self):
        result, postfix = calculate("2+3*4", show_postfix=True)
        self.assertEqual(result, 14)
        self.assertEqual(postfix, [2.0, 3.0, 4.0, "*", "+"])

    def test_invalid_expressions(self):
        expressions = [
            "5/0",
            "(2+3",
            "5+abc",
            "",
            "5+",
            "()",
            "2 3",
            "2(3)",
            "3..2",
            "2+*3",
            "2+3)",
            "1/(2-2)",
            "2**3",
        ]
        for expression in expressions:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    calculate(expression)


if __name__ == "__main__":
    unittest.main()
