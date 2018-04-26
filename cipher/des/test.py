from des import encrypt_one_block, decrypt_one_block
from permutation import convert_bin_array_to_hex

input = '0x123456abcd132536'
key = '0xaabb09182736ccdd'

print("Encrypt:")
cipher_text = encrypt_one_block(input, key)

print()
cipher_text = convert_bin_array_to_hex(cipher_text)
print("Decrypt:")
plain_text = decrypt_one_block(cipher_text, key)
