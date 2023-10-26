# Pavich sangwaree 6320502452
# A Polyalphabetic Substitution Cipher
# key = ["TMKGOYDSIPELUAVCRJWXZNHBQG", "DCBAHGFEMLKJIZYXWVUTSRQPON"]

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plainText, key):
    plainText = plainText.upper()
    ciphertext = ""
    len_key = len(key)
    i = 0
    for c in plainText:
        ciphertext += key[i][alpha.index(c)]
        i = (i+1) % len_key
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plainText = ""
    len_key = len(key)
    i = 0
    for c in ciphertext:
        plainText += alpha[key[i].index(c)]
        i = (i+1) % len_key
    return plainText


print("Welcome to A Polyalphabetic Substitution Cipher")
type = input("Enter type (E/D):")
if(type != 'E' and type != 'e' and type != 'D' and type != 'd'):
    print(f"Invalid input")
    exit(1)
inputString = input("Enter string:")
n = int(input("Enter a number of keys:"))
keys = []
for i in range(0, n):
    key = input(f"Enter {i+1}-key string:")
    keys.append(key)
if(type == 'E' or type == 'e'):
    output = encrypt(inputString, keys)
else:
    output = decrypt(inputString, keys)
print(f"String output is {output}")
