from .lib import PascalTriangle, SierpinskiTriangle
from .solutions import not_div_count


class Controller:

    def __init__(self):
        pass

    @staticmethod
    def get_pascal_triangle(n):
        return PascalTriangle(n)

    @staticmethod
    def get_sierpinski_triangle(n, d):
        return SierpinskiTriangle(n, d)

    @staticmethod
    def get_not_divisible(n, d):
        return not_div_count(n, d)
