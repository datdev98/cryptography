from permutation import permutation

parity_drop_array = [
    57, 49, 41, 33, 25, 17, 9,  1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7,  62, 54, 46, 38,
    30, 22, 14, 6,  61, 53, 45, 37,
    29, 21, 13, 5,  28, 20, 12, 4
]

bit_shifts_array = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

key_compression_array = [
    14, 17, 11, 24, 1,  5,  3,  28,
    15, 6,  21, 10, 23, 19, 12, 4,
    26, 8,  16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

def parity_drop(input):
    if len(input) != 64:
        raise Exception("Wrong dimension")
    return permutation(input, parity_drop_array)

def shift_left(input, bit_shifts):
    for i in range(bit_shifts):
        input.append(input.pop(0))

def compression_p_box(input):
    return permutation(input, key_compression_array)

    
def round_key_generator(input):
    cipher_key = parity_drop(input)
    cipher_key_lert = cipher_key[:28]
    cipher_key_right = cipher_key[28:]
    keys = []
    for i in range(16):
        shift_left(cipher_key_lert, bit_shifts_array[i])
        shift_left(cipher_key_right, bit_shifts_array[i])
        keys.append(compression_p_box(cipher_key_lert + cipher_key_right))
    return keys