import unittest
from calculator import calculate
from stack import Stack
from tokenizer import tokenize
from parser import infix_to_postfix


class CalculatorTests(unittest.TestCase):
    def test_valid_expressions(self):
        cases = [('5+3',8), ('10-4',6), ('5*4',20), ('20/4',5),
                 ('2+3*4',14), ('(2+3)*4',20), ('2*(3+(4*5))',46),
                 ('2.5+1.5',4), ('-5+3',-2), ('10-3-2',5), ('0',0),
                 ('8/4/2',1), ('2*-3',-6), ('-(2+3)',-5), ('--2',2),
                 ('12+34',46), ('  3  ',3), ('1/2',0.5)]
        for expression, expected in cases:
            with self.subTest(expression=expression):
                self.assertAlmostEqual(calculate(expression), expected)

    def test_invalid_expressions(self):
        for expression in ['5/0', '(2+3', '5+abc', '', '5+', '()', '2 3',
                           '2(3)', '3..2', '2+*3', '2+3)', '1/(2-2)', '2**3']:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    calculate(expression)

    def test_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertTrue(stack.is_empty())

    def test_tokenizer(self):
        self.assertEqual(tokenize('12 + 3.5'), [12.0, '+', 3.5])

    def test_conversion(self):
        self.assertEqual(infix_to_postfix(tokenize('2+3*4')), [2,3,4,'*','+'])
        self.assertEqual(infix_to_postfix(tokenize('(2+3)*4')), [2,3,'+',4,'*'])


if __name__ == '__main__':
    unittest.main()
