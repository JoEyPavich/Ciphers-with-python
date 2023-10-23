# A Polyalphabetic Substitution Cipher
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ["tmkgoydsipeluavcrjwxznhbqgTMKGOYDSIPELUAVCRJWXZNHBQG", "dcbahgfemlkjizyxwvutsrqponDCBAHGFEMLKJIZYXWVUTSRQPON"]


def encrypt(plainText, key):
    ciphertext = ""
    len_key = len(key)
    i = 0
    for c in plainText:
        ciphertext += key[i][alpha.index(c)]
        i = (i+1) % len_key
    return ciphertext


def decrypt(ciphertext, key):
    plainText = ""
    len_key = len(key)
    i = 0
    for c in ciphertext:
        plainText += alpha[key[i].index(c)]
        i = (i+1) % len_key
    return plainText


plainText = "Hello"
cipherText = encrypt(plainText, key)
decrypted = decrypt(cipherText, key)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}")
