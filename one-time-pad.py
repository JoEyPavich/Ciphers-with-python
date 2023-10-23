# A One time pad
secret_key = "00101 01100 10101"


def binToDec(bin):
    result = 0
    j = 0
    for i in reversed(range(0, len(bin))):
        result += int(bin[i]) * pow(2, j)
        j += 1
    return result


def encrypt(plainText, key):
    plainText = plainText.upper()
    ciphertext = ""
    key = key.split(' ')
    i = 0
    len_key = len(key)
    for c in plainText:
        intKey = binToDec(key[i])
        intC = ord(c) - ord('A')
        xor = intC ^ intKey
        ciphertext += chr(xor + ord('A'))
        i = (i+1) % len_key
    return ciphertext

plainText = 'ANT'
cipherText = encrypt(plainText, secret_key)
decrypted = encrypt(cipherText, secret_key)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}")
