# Pavich sangwaree 6320502452
# Vigenère Cipher
# secret_key = "SESAME"


def encrypt(plainText, key):
    ciphertext = ""
    len_key = len(key)
    i = 0
    for c in plainText:
        aCode = ord('A') if c.isupper() else ord('a')
        pCode = ord(c) - aCode
        kCode = ord(key[i]) - \
            ord('A') if key[i].isupper() else ord(key[i]) - ord('a')
        ciphertext += chr((pCode + kCode) % 26 + aCode)
        i = (i+1) % len_key
    return ciphertext


def decrypt(ciphertext, key):
    plainText = ""
    len_key = len(key)
    i = 0
    for c in ciphertext:
        aCode = ord('A') if c.isupper() else ord('a')
        pCode = ord(c) - aCode
        kCode = ord(key[i]) - \
            ord('A') if key[i].isupper() else ord(key[i]) - ord('a')
        plainText += chr((pCode - kCode) % 26 + aCode)
        i = (i+1) % len_key
    return plainText


print("Welcome to the Vigenère Cipher")
type = input("Enter type (E/D):")
if(type != 'E' and type != 'e' and type != 'D' and type != 'd'):
    print(f"Invalid input")
    exit(1)
inputString = input("Enter string:")
key = input("Enter key string:")
if(type == 'E' or type == 'e'):
    output = encrypt(inputString, key)
else:
    output = decrypt(inputString, key)
print(f"String output is {output}")
