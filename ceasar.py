def encrypt(plainText, key):
    cipherText = ""
    for c in plainText:
        if(c.isupper()):
            cipherText += chr((ord(c) + key - ord('A'))%26 + ord('A'))
        else:
            cipherText += chr((ord(c) + key - ord('a'))%26 + ord('a'))
            
    return cipherText

def decrypt(ciphertext, key):
    plainText = ""
    for c in ciphertext:
        if(c.isupper()):
            plainText += chr((ord(c) - key - ord('A'))%26 + ord('A'))
        else:
            plainText += chr((ord(c) - key - ord('a'))%26 + ord('a'))
            
    return plainText


plainText = "Hello"
key = 5
cipherText = encrypt(plainText, key)
decrypted = decrypt(cipherText,key)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}") 
