from math import frexp, ldexp

def float_to_int_exp(n: float)->(int, int):
    return int(ldexp(frexp(n)[0], 53)), frexp(n)[1] - 53

