# A Permutation Cipher
import random
secret_key = "24135"


def encrypt(plainText, key):
    plainText = plainText.replace(" ", "")
    plainText = plainText.upper()
    ciphertext = ""
    len_key = len(key)
    len_text = len(plainText)
    while(len_text % len_key != 0):
        plainText += chr(random.randint(0, 26)+ord('A'))
        len_text = len(plainText)
    for i in range(0, len_text, len_key):
        subPlainText = plainText[i:i+len_key]
        subCipher = ""
        for j in range(1, len_key+1):
            index = key.index(str(j))
            subCipher += subPlainText[index]
        ciphertext += subCipher

    return ciphertext


def decrypt(ciphertext, key):
    plainText = ""
    len_key = len(key)
    len_text = len(ciphertext)
    for i in range(0, len_text, len_key):
        subCipher = ciphertext[i:i+len_key]
        subPlainText = ""
        for j in range(0, len_key):
            index = int(key[j]) - 1
            subPlainText += subCipher[index]
        plainText += subPlainText
    return plainText


plainText = "Once upon a time there was a little girl called snow white"
cipherText = encrypt(plainText, secret_key)
decrypted = decrypt(cipherText, secret_key)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}")
# ONCE UPON A TIME THERE WAS A LITTLE GIRL CALLED SNOWWHITE QEC