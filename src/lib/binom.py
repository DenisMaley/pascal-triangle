from math import factorial as fac


def binomial_coef(n, k):
    try:
        coef = fac(n) // fac(k) // fac(n - k)
    except ValueError:
        coef = 0
    return coef
