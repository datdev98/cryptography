from feistel_cipher import feistel_cipher, xor
from permutation import convert_bin_array_to_hex

def mixer(input, key):
    feistel_cipher_result = feistel_cipher(input[32:], key)
    input[:32] = xor(input[:32], feistel_cipher_result)

def swapper(input):
    input[:32], input[32:] = input[32:], input[:32]

def rounds(input, keys):
    if len(input) != 64 or len(keys[0]) != 48:
        raise Exception("Wrong dimension")
    
    for i in range(15):
        mixer(input, keys[i])
        swapper(input)
        print("Round", i + 1, ":", convert_bin_array_to_hex(input), convert_bin_array_to_hex(keys[i]))


    mixer(input, keys[15])
    print("Round 16:", convert_bin_array_to_hex(input), convert_bin_array_to_hex(keys[15]))

    return input