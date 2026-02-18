# test_my_math.py
import unittest
from my_math import add, multiply

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 10), 0)

if __name__ == "__main__":
    unittest.main()
