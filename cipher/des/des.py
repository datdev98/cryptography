from permutation import permutation, convert_to_bin_array, convert_bin_array_to_hex
from rounds import rounds
from key_generation import round_key_generator

initial_permutation_array = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

final_permutation_array = [
    40, 8,  48, 16, 56, 24, 64, 32,
    39, 7,  47, 15, 55, 23, 63, 31,
    38, 6,  46, 14, 54, 22, 62, 30,
    37, 5,  45, 13, 53, 21, 61, 29,
    36, 4,  44, 12, 52, 20, 60, 28,
    35, 3,  43, 11, 51, 19, 59, 27,
    34, 2,  42, 10, 50, 18, 58, 26,
    33, 1,  41, 9,  49, 17, 57, 25
]

def initial_permutation(input):
    return permutation(input, initial_permutation_array)

def final_permutation(input):
    return permutation(input, final_permutation_array)

def encrypt_one_block(plain_text, key):
    print("Plain text:", plain_text)
    initial_permutation_result = initial_permutation(convert_to_bin_array(plain_text, 64))
    print("After initial permutation:", convert_bin_array_to_hex(initial_permutation_result))

    keys = round_key_generator(convert_to_bin_array(key, 64))
    rounds_result = rounds(initial_permutation_result, keys)
    print("After 16 rounds:", convert_bin_array_to_hex(rounds_result))

    cipher_text = final_permutation(rounds_result)
    print("After final permutation:", convert_bin_array_to_hex(cipher_text))

    return cipher_text
    


def decrypt_one_block(cipher_text, key):
    print("Cipher text:", cipher_text)
    initial_permutation_result = initial_permutation(convert_to_bin_array(cipher_text, 64))
    print("After initial permutation:", convert_bin_array_to_hex(initial_permutation_result))

    keys = round_key_generator(convert_to_bin_array(key, 64))
    keys.reverse()
    rounds_result = rounds(initial_permutation_result, keys)
    print("After 16 rounds:", convert_bin_array_to_hex(rounds_result))

    plain_text = final_permutation(rounds_result)
    print("After final permutation:", convert_bin_array_to_hex(plain_text))

    return plain_text
