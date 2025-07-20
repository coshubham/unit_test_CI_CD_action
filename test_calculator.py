import pytest
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subs(self):
        self.assertEqual(self.calc.subs(10, 3), 7)

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 4), 5.0)

if __name__ == "__main__":
    unittest.main()
