from permutation import permutation, convert_to_bin_array, convert_bin_array_to_dec

expansion_p_box_array = [
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

straight_p_box_array = [
    16, 7,  20, 21, 29, 12, 28, 17, 
    1,  15, 23, 26, 5,  18, 31, 10, 
    2,  8,  24, 14, 32, 27, 3,  9,
    19, 13, 30, 6,  22, 11, 4,  25
]

s_box_0 = [
    [14, 4,  13, 1,  2,  15, 11, 8,  3,  10, 6,  12, 5,  9,  0,  7 ],
    [0,  15, 7,  4,  14, 2,  13, 1,  10,  6, 12, 11, 9,  5,  3,  8 ], 
    [4,  1,  14, 8,  13, 6,  2,  11, 15, 12, 9,  7,  3,  10, 5,  0 ],
    [15, 12, 8,  2,  4,  9,  1,  7,  5,  11, 3,  14, 10, 0,  6,  13] 
]

s_box_1 = [
    [15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10],
    [3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5 ],
    [0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15],
    [13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9 ]
]

s_box_2 = [
    [10, 0,  9,  14, 6,  3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8 ],
    [13, 7,  0,  9,  3,  4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1 ],
    [13, 6,  4,  9,  8,  15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7 ],
    [1,  10, 13, 0,  6,  9,  8,  7,  4,  15, 14, 3,  11, 5,  2,  12]
]

s_box_3 = [
    [7,  13, 14, 3,  0,  6,  9,  10, 1,  2,  8,  5,  11, 12, 4,  15],
    [13, 8,  11, 5,  6,  15, 0,  3,  4,  7,  2,  12, 1,  10, 14, 9 ],
    [10, 6,  9,  0,  12, 11, 7,  13, 15, 1,  3,  14, 5,  2,  8,  4 ],
    [3,  15, 0,  6,  10, 1,  13, 8,  9,  4,  5,  11, 12, 7,  2,  14]
]

s_box_4 = [
    [2,  12, 4,  1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0,  14, 9 ],
    [14, 11, 2,  12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9,  8,  6 ],
    [4,  2,  1,  11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3,  0,  14],
    [11, 8,  12, 7,  1,  14, 2,  13, 6,  15, 0,  9,  10, 4,  5,  3 ]
]

s_box_5 = [
    [12, 1,  10, 15, 9,  2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11],
    [10, 15, 4,  2,  7,  12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8 ],
    [9,  14, 15, 5,  2,  8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6 ],
    [4,  3,  2, 12,  9,  5,  15, 10, 11, 14, 1,  7,  6,  0,  8,  13]
]

s_box_6 = [
    [4,  11, 2,  14, 15, 0,  8,  13, 3,  12, 9,  7,  5,  10, 6,  1 ],
    [13, 0,  11, 7,  4,  9,  1,  10, 14, 3,  5,  12, 2,  15, 8,  6 ],
    [1,  4,  11, 13, 12, 3,  7,  14, 10, 15, 6,  8,  0,  5,  9,  2 ],
    [6,  11, 13, 8,  1,  4,  10, 7,  9,  5,  0,  15, 14, 2,  3,  12]
]

s_box_7 = [
    [13, 2,  8,  4,  6,  15, 11, 1,  10, 9,  3,  14, 5,  0,  12, 7 ],
    [1,  15, 13, 8,  10, 3,  7,  4,  12, 5,  6,  11, 0,  14, 9,  2 ],
    [7,  11, 4,  1,  9,  12, 14, 2,  0,  6,  10, 13, 15, 3,  5,  8 ],
    [2,  1,  14, 7,  4,  10, 8,  13, 15, 12, 9,  0,  3,  5,  6,  11]
]

s_box_array = [s_box_0, s_box_1, s_box_2, s_box_3, s_box_4, s_box_5, s_box_6, s_box_7]

def expansion_p_box(input):
    if len(input) != 32:
        raise Exception("Wrong dimension")

    return permutation(input, expansion_p_box_array)
    
def xor_bit(bit, other):
    if bit == '0' and other == '0':
        return '0'
    if bit == '0' and other == '1':
        return '1'
    if bit == '1' and other == '0':
        return '1'
    if bit == '1' and other == '1':
        return '0'

def xor(input, other):
    if len(input) != len(other):
        raise Exception("Wrong dimension")
        
    result = [None] * len(input)
    for i in range(len(input)):
        result[i] = xor_bit(input[i], other[i])
    return result

def s_box(input, s_box_index):
    if len(input) != 6:
        raise Exception("Wrong dimension")

    row = convert_bin_array_to_dec([input[0], input[5]])
    col = convert_bin_array_to_dec(input[1:5])
    return convert_to_bin_array(s_box_array[s_box_index][row][col], 4)


def s_boxes(input):
    if len(input) != 48:
        raise Exception("Wrong dimension")
    result = []
    for i in range(8):
        result += s_box(input[6 * i : 6 * i + 6], i)
    return result
    

def straight_p_box(input):
    if len(input) != 32:
        raise Exception("Wrong dimension")
    return permutation(input, straight_p_box_array)

def feistel_cipher(input, key):
    if len(input) != 32:
        raise Exception("Wrong dimension")
    if len(key) != 48:
        raise Exception("Wrong key dimension")

    expansion_p_box_result = expansion_p_box(input)
    xor_result = xor(expansion_p_box_result, key)
    s_boxes_result = s_boxes(xor_result)
    straight_p_box_result = straight_p_box(s_boxes_result)
    return straight_p_box_result



def main():
    print(convert_to_bin_array('0x18ca18ad', 32))
    print(expansion_p_box(convert_to_bin_array('0x18ca18ad', 32)))

if __name__ == '__main__':
    main()