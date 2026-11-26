import unittest

from core.stack import Stack


class StackTests(unittest.TestCase):
    def test_stack_operations(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertTrue(stack.is_empty())

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            Stack().pop()

    def test_peek_empty_stack(self):
        with self.assertRaises(IndexError):
            Stack().peek()


if __name__ == "__main__":
    unittest.main()
