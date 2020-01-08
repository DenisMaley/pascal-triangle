import unittest

from src import Controller
from src.lib.triangles import PascalTriangle, SierpinskiTriangle


class TestController(unittest.TestCase):
    n = 10
    d = 7

    def test_get_pascal_triangle(self):
        triangle = Controller.get_pascal_triangle(self.n)
        self.assertIsInstance(triangle, PascalTriangle)
        self.assertEqual(self.n, len(triangle.triangle))

    def test_get_sierpinski_triangle(self):
        triangle = Controller.get_sierpinski_triangle(self.n, self.d)
        self.assertIsInstance(triangle, SierpinskiTriangle)
        self.assertEqual(self.n, len(triangle.triangle))

    def test_get_not_divisible(self):
        tests = [
            {'n': 100, 'p': 7, 'expected_result': 2361},
            {'n': 1000000000, 'p': 7, 'expected_result': 2129970655314432},
            {'n': 879799879, 'p': 17, 'expected_result': 6026990181372288},
            {'n': 879799879, 'p': 19, 'expected_result': 8480245105257600},
            {'n': 751825096, 'p': 7, 'expected_result': 1268068459033362},
        ]

        for test in tests:
            self.assertEqual(test['expected_result'], Controller.get_not_divisible(test['n'], test['p']))
