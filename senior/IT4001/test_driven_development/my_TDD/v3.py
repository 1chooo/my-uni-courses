import unittest

class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("輸入必須是數字")
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("輸入必須是數字")
        return a - b

    def multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("輸入必須是數字")
        return a * b

    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("輸入必須是數字")
        if b == 0:
            raise ValueError("除數不能為零")
        return a / b

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

        result = self.calculator.add(-5, 7)
        self.assertEqual(result, 2)

        result = self.calculator.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3)

        with self.assertRaises(TypeError):
            self.calculator.add(2, "3")

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

        result = self.calculator.subtract(3, 5)
        self.assertEqual(result, -2)

        result = self.calculator.subtract(0.6, 0.1)
        self.assertAlmostEqual(result, 0.5)

        with self.assertRaises(TypeError):
            self.calculator.subtract(5, "3")

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

        result = self.calculator.multiply(-4, 5)
        self.assertEqual(result, -20)

        result = self.calculator.multiply(0.1, 0.3)
        self.assertAlmostEqual(result, 0.03)

        with self.assertRaises(TypeError):
            self.calculator.multiply(2, "3")

    def test_divide(self):
        result = self.calculator.divide(6, 2)
        self.assertEqual(result, 3)

        result = self.calculator.divide(10, 4)
        self.assertAlmostEqual(result, 2.5)

        result = self.calculator.divide(-9, 3)
        self.assertEqual(result, -3)

        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)

        with self.assertRaises(TypeError):
            self.calculator.divide(6, "2")

if __name__ == '__main__':
    unittest.main()