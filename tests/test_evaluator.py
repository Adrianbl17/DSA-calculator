import unittest

from core.evaluator import evaluate_postfix


class EvaluatorTests(unittest.TestCase):
    def test_evaluates_binary_and_unary_operators(self):
        self.assertEqual(evaluate_postfix([2, 3, 4, "*", "+"]), 14)
        self.assertEqual(evaluate_postfix([5, "u-", 3, "+"]), -2)
        self.assertEqual(evaluate_postfix([2, "u-", "u-"]), 2)

    def test_rejects_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Division by zero"):
            evaluate_postfix([1, 0, "/"])

    def test_rejects_insufficient_operands(self):
        with self.assertRaisesRegex(ValueError, "Missing operands"):
            evaluate_postfix([1, "+"])

    def test_rejects_extra_operands(self):
        with self.assertRaisesRegex(ValueError, "Invalid expression"):
            evaluate_postfix([1, 2])


if __name__ == "__main__":
    unittest.main()
