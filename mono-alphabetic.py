# Pavich sangwaree 6320502452
# A Mono-alphabetic Substitution Cipher
# key = "GOYDSIPELUAVCRJWXZNHBQFTMK"

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plainText, key):
    plainText = plainText.upper()
    ciphertext = ""
    for i in plainText:
        ciphertext += key[alpha.index(i)]
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plainText = ""
    for i in ciphertext:
        plainText += alpha[key.index(i)]
    return plainText


print("Welcome to A Mono-alphabetic Substitution Cipher")
type = input("Enter type (E/D):")
if(type != 'E' and type != 'e' and type != 'D' and type != 'd'):
    print(f"Invalid input")
    exit(1)
inputString = input("Enter string:")
key = input("Enter key string [A-Z]:")
if(type == 'E' or type == 'e'):
    output = encrypt(inputString, key)
else:
    output = decrypt(inputString, key)
print(f"String output is {output}")
