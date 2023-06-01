# input: Positive integers x and y
# output: x^y
def apply_fast_exponentiation(x, y):
    p = 1  # p holds the partial result
    s = x  # s holds the current x^(2^i)
    r = y  # r is used to compute the binary expansion of y
    while r > 0:
        if r % 2 == 1:
            p *= s
        s *= s
        r //= 2
    return p


# input: Positive integers x, y, and n
# output: x^y mod n
def apply_modular_exponentiation(x, y, n):
    p = 1  # p holds the partial result
    s = x  # s holds the current x^(2^i)
    r = y  # r is used to compute the binary expansion of y
    while r > 0:
        if r % 2 == 1:
            p = (p * s) % n
        s = (s * s) % n
        r //= 2
    return p


if __name__ == '__main__':
    print(apply_fast_exponentiation(5, 9))
    print(apply_modular_exponentiation(5, 68, 7))
