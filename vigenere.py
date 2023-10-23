# Vigenère Cipher
secret_key = "SESAME"


def encrypt(plainText, key):
    ciphertext = ""
    len_key = len(key)
    i = 0
    for c in plainText:
        c = c.upper()
        x = ord(key[i]) - ord('A')
        ciphertext += chr((ord(c) + ord(key[i]) - 2*ord('A')) % 26 + ord('A'))
        i = (i+1) % len_key
    return ciphertext


def decrypt(ciphertext, key):
    plainText = ""
    len_key = len(key)
    i = 0
    for c in ciphertext:
        c = c.upper()
        x = ord(key[i]) - ord('A')
        plainText += chr( ( ord(c) - ord(key[i]) - 2*ord('A') ) % 26 + ord('A') )
        i = (i+1)%len_key
    return plainText

plainText = "THISISATESTMESSAGE"
cipherText = encrypt(plainText, secret_key)
decrypted = decrypt(cipherText, secret_key)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}")
