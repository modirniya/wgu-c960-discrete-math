# Number of letters in English alphabet
ENG_LETTERS = 26


# Function to convert a character to its corresponding number, 'A' or 'a' => 0, 'B' or 'b' => 1, etc.
def char_to_num(char):
    char = char.upper()
    return ord(char) - ord('A')


# Function to convert a number to its corresponding character, 0 => 'A', 1 => 'B', etc.
def num_to_char(num):
    return chr(num + ord('A'))


# Function to encrypt a character using affine cipher
def encrypt(char, key):
    char_num = char_to_num(char)
    encrypted_num = (key[0] * char_num + key[1]) % ENG_LETTERS
    return num_to_char(encrypted_num)


class AffineCipherOperations:
    @staticmethod
    def compute_gcd_and_steps(a, b):
        if b > a:
            a, b = b, a
        gcd_steps = []
        while a % b != 0:
            old_a = a
            a = b
            b = old_a % b
            gcd_steps.append((old_a, (a, old_a // a), b))
        gcd = gcd_steps[-1][2]
        if gcd != 1:
            raise ValueError(f"The first element of the key must be coprime with {ENG_LETTERS}.")
        return gcd_steps

    @staticmethod
    def perform_extended_euclidean(gcd_steps):
        extended_steps_dict = {}
        final_step = None
        for current_step in gcd_steps:
            key = current_step[2]
            final_step = ((current_step[0], 1), (current_step[1][0], current_step[1][1] * -1))
            extended_steps_dict[key] = final_step
        result_dict = {}
        AffineCipherOperations.perform_recursive_operation(final_step, extended_steps_dict, result_dict)
        return result_dict

    @staticmethod
    def perform_recursive_operation(items_list, substitutions_dict, results_dict, multiplier=1):
        for item in items_list:
            item_key = item[0]
            if item_key in substitutions_dict:
                AffineCipherOperations.perform_recursive_operation(substitutions_dict[item_key], substitutions_dict,
                                                                   results_dict, item[1] * multiplier)
            else:
                if item_key in results_dict:
                    results_dict[item_key] += item[1] * multiplier
                else:
                    results_dict[item_key] = item[1] * multiplier


# Function to decrypt a character using affine cipher
def decrypt(char, key):
    encrypted_char_num = char_to_num(char)
    gcd_steps = AffineCipherOperations.compute_gcd_and_steps(key[0], ENG_LETTERS)
    inverse_dict = AffineCipherOperations.perform_extended_euclidean(gcd_steps)
    decrypted_char_num = (inverse_dict[key[0]] % ENG_LETTERS) * (encrypted_char_num - key[1]) % ENG_LETTERS
    return num_to_char(decrypted_char_num)


if __name__ == '__main__':
    init_char = 'B'
    print(f"initial character -> {init_char}")
    encryption_key = (1255, 224)
    print(f"encryption key in use -> {encryption_key}")
    encrypted_char = encrypt(init_char, encryption_key)
    print(f"encrypted character -> {encrypted_char}")
    decrypted_char = decrypt(encrypted_char, encryption_key)
    print(f"decrypted character -> {decrypted_char}")
