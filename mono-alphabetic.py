# A Mono-alphabetic Substitution Cipher
alpha = "abcdefghijklmnopqrstuvwxyz"
key = "goydsipeluavcrjwxznhbqftmk"


def encrypt(plainText, key):
    ciphertext = ""
    for i in plainText:
        ciphertext += key[alpha.index(i)]
    return ciphertext


def decrypt(ciphertext, key):
    plainText = ""
    for i in ciphertext:
        plainText += alpha[key.index(i)]
    return plainText

plainText = "hello"
cipherText = encrypt(plainText, key)
decrypted = decrypt(cipherText, key)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}")
