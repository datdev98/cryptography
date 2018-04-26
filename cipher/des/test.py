from des import encrypt_text, decrypt_text
from permutation import convert_bin_array_to_hex

input = 'Không có gì quý hơn độc lập tự do'
key = '0xaabb09182736ccdd'

print("Encrypt:")
cipher_text = encrypt_text(input, key)
print(cipher_text)

print()
print("Decrypt:")
plain_text = decrypt_text(cipher_text, key)
print(plain_text)
