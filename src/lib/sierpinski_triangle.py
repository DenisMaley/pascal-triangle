from .binom_coef import binomial_coef


class SierpinskiTriangle:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def get_triangle(self):
        triangle = []
        for i in range(self.n + 1):
            triangle.append([min(binomial_coef(i, j) % self.d, 1) for j in range(i + 1)])
        return triangle
