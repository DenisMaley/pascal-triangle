import unittest

from src.solutions.divisibility import not_div_count


class TestDivisibility(unittest.TestCase):
    tests = [
        {'n': 5, 'p': 5, 'expected_result': 17},
        {'n': 5, 'p': 7, 'expected_result': 21},
        {'n': 1, 'p': 13, 'expected_result': 3},
        {'n': 99, 'p': 7, 'expected_result': 2361},
        {'n': 999999999, 'p': 7, 'expected_result': 2129970655314432},
        {'n': 879799878, 'p': 17, 'expected_result': 6026990181372288},
        {'n': 879799878, 'p': 19, 'expected_result': 8480245105257600},
        {'n': 751825095, 'p': 7, 'expected_result': 1268068459033362},
        {'n': 530891642, 'p': 19, 'expected_result': 3152614956962304},
        {'n': 713352683, 'p': 7, 'expected_result': 1136714903932416},
        {'n': 633083772, 'p': 17, 'expected_result': 3132363934499307},
    ]

    def test_not_div_count(self):
        for test in self.tests:
            self.assertEqual(test['expected_result'], not_div_count(test['n'], test['p']))


if __name__ == '__main__':
    unittest.main()
