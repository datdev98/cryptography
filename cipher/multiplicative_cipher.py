import integer

plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text, key):
    text = ''
    for ch in plain_text:
        text += cipher[(plain.index(ch) * key) % 26]
    return text

def decrypt(cipher_text, key):
    text = ''
    nghich_dao = integer.nghich_dao(key, 26)
    if nghich_dao == 0:
        print("Khong the tim nghic dao")
        return
    for ch in cipher_text:
        text += plain[(cipher.index(ch) * nghich_dao) % 26]
    return text

def main():
    plain_text = input("Enter text: ")
    key = int(input("Enter key: "))


    result = encrypt(plain_text, key)
    print('Encrypted text:', result)
    print('Redecrypt:', decrypt(result, key))

if __name__ == '__main__':
    main()