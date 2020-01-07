from math import factorial as fac


# https://en.wikipedia.org/wiki/Binomial_coefficient#Binomial_coefficient_in_programming_languages
# Naive implementation
# from math import factorial
# coef = factorial(n) // factorial(k) // factorial(n - k)
# is very slow and are useless for calculating factorials of very high numbers
def binomial_coefficient(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c
