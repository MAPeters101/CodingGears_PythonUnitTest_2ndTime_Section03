import unittest
import lesson009_calculator


class TestCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = lesson009_calculator.calc_add(10,20)
        self.assertEqual(result, 30)


