# calculates x^y
def apply_fast_exponentiation(x, y):
    p = 1  # p holds the partial result.
    s = x  # s holds the current x^(2^i)
    r = y  # r is used to compute the binary expansion of y
    while r > 0:
        if r % 2 == 1:
            p *= s
        s *= s
        r = r // 2
    return p


if __name__ == '__main__':
    print(apply_fast_exponentiation(5, 9))
