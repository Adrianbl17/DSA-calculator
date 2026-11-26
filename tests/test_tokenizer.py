import unittest

from core.tokenizer import tokenize


class TokenizerTests(unittest.TestCase):
    def test_tokenizes_numbers_and_operators(self):
        self.assertEqual(tokenize("12 + 3.5"), [12.0, "+", 3.5])

    def test_tokenizes_decimal_and_signed_expression(self):
        self.assertEqual(tokenize("-0.5 * (2.)"), ["-", 0.5, "*", "(", 2.0, ")"])

    def test_rejects_invalid_character(self):
        with self.assertRaisesRegex(ValueError, "Invalid character"):
            tokenize("2 + a")

    def test_rejects_empty_input(self):
        with self.assertRaisesRegex(ValueError, "Empty expression"):
            tokenize("   ")

    def test_rejects_invalid_decimal(self):
        with self.assertRaises(ValueError):
            tokenize("3..2")


if __name__ == "__main__":
    unittest.main()
