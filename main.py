import unittest


class Calculator:
    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.plus(4, 7), 11)
        self.assertEqual(self.calc.plus(-1, 1), 0)
        self.assertEqual(self.calc.plus(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.minus(10, 5), 5)
        self.assertEqual(self.calc.minus(-1, 1), -2)
        self.assertEqual(self.calc.minus(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)


if __name__ == '__main__':
    unittest.main()
