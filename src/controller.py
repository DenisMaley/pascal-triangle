from .lib import PascalTriangle, SierpinskiTriangle


class Controller:

    @staticmethod
    def get_pascal_triangle(n):
        return PascalTriangle(n)

    @staticmethod
    def get_sierpinski_triangle(n, d):
        return SierpinskiTriangle(n, d)
