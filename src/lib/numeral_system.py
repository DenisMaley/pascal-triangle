ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"


def dec_to_base(dec=0, base=2):
    if dec < base:
        return encode(dec)
    else:
        return dec_to_base(dec // base, base) + encode(dec % base)


def encode(n):
    try:
        return ALPHABET[n]
    except IndexError:
        raise Exception("cannot encode: %s" % n)


def base_to_dec(s, base=2, pow=0):
    if s == "":
        return 0
    else:
        return decode(s[-1]) * (base ** pow) + base_to_dec(s[0:-1], base, pow + 1)


def decode(s):
    try:
        return ALPHABET.index(s)
    except ValueError:
        raise Exception("cannot decode: %s" % s)
