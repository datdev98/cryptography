from functools import reduce

def convert_to_bin_array(number, length):
    if isinstance(number, int):
        return list(bin(number)[2:].zfill(length))
    elif isinstance(number, str):
        if number[0:2] == '0x':
            dec = int(number, 16)
            return list(bin(dec)[2:].zfill(length))
        if number[0:2] == '0b':
            return list(number[2:].zfill(length))

def create_bin_str(bin_array):
    bin_str = '0b'
    bin_str += reduce(lambda x, y: x + y, bin_array)
    return bin_str

def convert_bin_array_to_hex(bin_array):
    bin_str = create_bin_str(bin_array)
    return hex(int(bin_str, 2))

def convert_bin_array_to_dec(bin_array):
    bin_str = create_bin_str(bin_array)
    return int(bin_str, 2)

def permutation(input, array):
    result = [None] * len(array)
    for i in range(len(array)):
        # result[array[i]-1] = input[i]
        result[i] = input[array[i] - 1]

    return result

def main():
    bin_array = convert_to_bin_array('0x0000008000000002', 64)
    initial_permutation = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9,  1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    
    final_permutation = [
        40, 8,  48, 16, 56, 24, 64, 32,
        39, 7,  47, 15, 55, 23, 63, 31,
        38, 6,  46, 14, 54, 22, 62, 30,
        37, 5,  45, 13, 53, 21, 61, 29,
        36, 4,  44, 12, 52, 20, 60, 28,
        35, 3,  43, 11, 51, 19, 59, 27,
        34, 2,  42, 10, 50, 18, 58, 26,
        33, 1,  41, 9,  49, 17, 57, 25
    ]
    output = permutation(convert_to_bin_array('0x123456abcd132536', 64), initial_permutation)
    print(convert_bin_array_to_hex(output))

if __name__ == '__main__':
    main()  
