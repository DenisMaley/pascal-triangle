from .lib import PascalTriangle


class Controller:
    def __init__(self, n):
        self.n = n

    def get_triangle(self):
        return PascalTriangle(self.n).get_triangle()
