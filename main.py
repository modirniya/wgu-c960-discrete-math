from affine_cipher import AffineCipherOperations


def calculate_multiplicative_inverses(items: list):
    print(
        f"The multiplicative inverse of {items[1][0]} mod {items[0][0]} is "
        f"({items[1][1]} mod {items[0][0]}) = {items[1][1] % items[0][0]}\n")

    print(
        f"The multiplicative inverse of {items[0][0]} mod {items[1][0]} is "
        f"({items[0][1]} mod {items[1][0]}) = {items[0][1] % items[1][0]}")

    pass


if __name__ == '__main__':
    res = AffineCipherOperations.compute_gcd_and_steps(53, 71)
    print(res)
    res_dict = AffineCipherOperations.perform_extended_euclidean(res)
    print(res_dict)
    calculate_multiplicative_inverses(list(res_dict.items()))

    print(-4 % 71)
