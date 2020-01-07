from src.lib import dec_to_base, decode


# For the theory and terminology check the document:

# D function
def not_div_count(n, p):
    if n == 0:
        return 1
    i = 0
    base_repr = dec_to_base(n, p)

    while n >= p ** (i + 1):
        i += 1

    # a_i - leading weight converted back to integer
    head = decode(base_repr[0])
    # a_(i-1)...a_0 - tailing weights in decimal system
    tail = n - head * p ** i

    return t(head) * t(p) ** i + (head + 1) * not_div_count(tail, p)


def t(k):
    return int(k * (k + 1) / 2)
