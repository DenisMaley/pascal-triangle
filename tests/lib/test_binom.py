import unittest

from src.lib.binom import binomial_coefficient


class TestBinom(unittest.TestCase):
    tests = [
        {'n': 1, 'k': -1, 'expected_coef': 0},
        {'n': 1, 'k': 4, 'expected_coef': 0},
        {'n': 1, 'k': 1, 'expected_coef': 1},
        {'n': 4, 'k': 3, 'expected_coef': 4},
        {'n': 10, 'k': 3, 'expected_coef': 120},
        {'n': 15, 'k': 5, 'expected_coef': 3003},
        {'n': 23, 'k': 10, 'expected_coef': 1144066},
        {'n': 50, 'k': 25, 'expected_coef': 126410606437752},
    ]

    def test_binomial_coefficient(self):
        for test in self.tests:
            self.assertEqual(test['expected_coef'], binomial_coefficient(test['n'], test['k']))


if __name__ == '__main__':
    unittest.main()
