from .binom_coef import binomial_coef


class PascalTriangle:
    def __init__(self, n):
        self.n = n

    def get_triangle(self):
        triangle = []
        for i in range(self.n + 1):
            triangle.append([binomial_coef(i, j) for j in range(i + 1)])
        return triangle
