import multiplicative_cipher
import additive_cipher

def encrypt(plain_text, key1, key2):
    T = multiplicative_cipher.encrypt(plain_text, key1).lower()
    C = additive_cipher.encrypt(T, key2)
    return C

def decrypt(ciper_text, key1, key2):
    T = additive_cipher.decrypt(ciper_text, key2).upper()
    P = multiplicative_cipher.decrypt(T, key1)
    return P

def main():
    plain_text = input("Enter text: ")
    key1 = int(input("Enter key 1: "))
    key2 = int(input("Enter key 2: "))


    result = encrypt(plain_text, key1, key2)
    print('Encrypted text:', result)
    print('Redecrypt:', decrypt(result, key1, key2))

if __name__ == '__main__':
    main()