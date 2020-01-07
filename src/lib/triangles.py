from abc import ABC, abstractmethod

from .binom import binomial_coefficient


class Triangle(ABC):
    def __init__(self, n):
        self.n = n
        self.triangle = self.get_triangle()

    @abstractmethod
    def build_element(self, i, j):
        pass

    @abstractmethod
    def repr_element(self, e):
        pass

    def __repr__(self):
        last_row_len = len(' '.join(self.repr_element(x) for x in self.triangle[self.n]))

        triangle_repr_rows = []
        for row in self.triangle:
            row_i = ' '.join(self.repr_element(x) for x in row)
            indent = ' ' * int((last_row_len - len(row_i)) / 2)
            triangle_repr_rows.append(indent + row_i + indent)

        return '\n'.join(triangle_repr_rows)

    def get_triangle(self):
        triangle = []
        for i in range(self.n + 1):
            triangle.append([self.build_element(i, j) for j in range(i + 1)])
        return triangle


class PascalTriangle(Triangle):
    def build_element(self, i, j):
        return binomial_coefficient(i, j)

    def repr_element(self, e):
        return str(e)


class SierpinskiTriangle(Triangle):
    def __init__(self, n, d):
        self.d = d
        super(SierpinskiTriangle, self).__init__(n)

    def build_element(self, i, j):
        return binomial_coefficient(i, j) % self.d

    def repr_element(self, e):
        return ' ' if e == 0 else '*'
