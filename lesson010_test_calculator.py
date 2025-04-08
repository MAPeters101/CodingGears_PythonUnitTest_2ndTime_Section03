import unittest
from lesson010_calculator import Calculator


class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        calc1 = Calculator(10, 30)
        result = calc1.calc_add()
        self.assertEqual(result, 40)