import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_two_plus_three_equals_five(self):
        self.assertEquals(5, self.calculator.add(2, 3))

    def test_three_subtract_two_equals_one(self):
        self.assertEquals(1, self.calculator.subtract(3, 2))

    def test_two_subtract_three_equals_one(self):
        self.assertEquals(-1, self.calculator.subtract(2, 3))

if __name__ == "__main__":
    unittest.main()
