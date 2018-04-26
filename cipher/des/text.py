from permutation import convert_to_bin_array, convert_bin_array_to_dec

def convert_text_to_bin_array(text):
    result = []
    byte_str = text.encode('utf-8')

    for b in byte_str:
        result.extend(convert_to_bin_array(b, 8))

    return result

def convert_bin_array_to_text(bin_array):
    if len(bin_array) % 8 != 0:
        raise Exception("Bin array length must chia het cho 8")
    byte_array = []
    for i in range(len(bin_array) // 8):
        byte = convert_bin_array_to_dec(bin_array[8*i:i*8 + 8])
        byte_array.append(byte)
    return bytes(byte_array).decode('utf-8')

def convert_bin_array_to_block(bin_array, block_size):
    adder = (block_size - len(bin_array) % block_size) % block_size
    result = []
    result.append(['0'] * adder)
    for bit in bin_array:
        if len(result[len(result) - 1]) == block_size:
            result.append([])
        result[len(result) - 1].extend([bit])

    return result

def convert_block_to_bin_array(block):
    result = []
    for row in block:
        for cell in row:
            result.append(cell)
    return result

def main():
    bin_array = convert_text_to_bin_array("Không có gì quý hơn độc lập tự do")
    block = convert_bin_array_to_block(bin_array, 64)
    bin_array = convert_block_to_bin_array(block)
    text = convert_bin_array_to_text(bin_array)
    print(text)

if __name__ == '__main__':
    main()