# Pavich sangwaree 6320502452
# Caesar Cipher
def encrypt(plainText, key):
    cipherText = ""
    for c in plainText:
        if(c.isupper()):
            cipherText += chr((ord(c) + key - ord('A')) % 26 + ord('A'))
        else:
            cipherText += chr((ord(c) + key - ord('a')) % 26 + ord('a'))

    return cipherText


def decrypt(ciphertext, key):
    plainText = ""
    for c in ciphertext:
        if(c.isupper()):
            plainText += chr((ord(c) - key - ord('A')) % 26 + ord('A'))
        else:
            plainText += chr((ord(c) - key - ord('a')) % 26 + ord('a'))

    return plainText


print("Welcome to the Caesar Cipher")
type = input("Enter type (E/D):")
if(type != 'E' and type != 'e' and type != 'D' and type != 'd'):
    print(f"Invalid input")
    exit(1)
inputString = input("Enter string:")
key = int(input("Enter key:"))
if(type == 'E' or type == 'e'):
    output = encrypt(inputString, key)
else:
    output = decrypt(inputString, key)
print(f"String output is {output}")
