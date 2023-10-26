# Pavich sangwaree 6320502452
# A One-time Pad
# secret_key = "00101 01100 10101"


def binToDec(bin):
    result = 0
    j = 0
    for i in reversed(range(0, len(bin))):
        result += int(bin[i]) * pow(2, j)
        j += 1
    return result


def encryptAndDecrypt(plainText, key):
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


print("Welcome to A One-time Pad")
type = input("Enter type (E/D):")
if(type != 'E' and type != 'e' and type != 'D' and type != 'd'):
    print(f"Invalid input")
    exit(1)
inputString = input("Enter string:")
key = input("Enter key string (n bits):")
checkKey = key.replace(" ", "")
if (not checkKey.isdigit() or len(checkKey) != len(inputString) * 5):
    print("Key must be a binary string with n of data size.")
    exit(1)
output = encryptAndDecrypt(inputString, key)
print(f"String output is {output}")
