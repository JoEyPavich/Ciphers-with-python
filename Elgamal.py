import random

p = 17
g = 6
x = 5
y = pow(g, x, p)

k = random.randint(10, 100)

print(f"Let p = {p}")
print(f"Select g = {g}")
print(f"private key = {x}")
print(f"public key = ({p},{g},{y})")


def encrypt(plainText, p, g, y):
    plainText = plainText.upper()
    ciphertext = []
    for c in plainText:
        P = ord(c)-ord('A')
        c1 = pow(g, k, p)
        c2 = (P*pow(y, k)) % p
        pair = [c1, c2]
        print(f"C1 is {c1} and C2 is {c2}")
        ciphertext.append(pair)
    return ciphertext


def decrypt(ciphertext, private):
    plainText = ""
    for c in ciphertext:
        de = c[1] * pow(c[0], -private, p) % p
        plainText += chr(de+ord('A'))
    return plainText

# Plaintext is P ∈ [0, p[ note!

plainText = "HELLO"
cipherText = encrypt(plainText, p, g, y)
decrypted = decrypt(cipherText, x)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}")
