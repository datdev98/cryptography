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
    output = permutation(convert_to_bin_array('0x123456abcd132536', 64), initial_permutation)
    print(convert_bin_array_to_hex(output))

if __name__ == '__main__':
    main()  
