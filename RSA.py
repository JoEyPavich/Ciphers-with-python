import random

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def isprime(x):
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            return False
    return True


def generate():
    p = random.randint(0, 100)
    q = random.randint(0, 100)
    while(isprime(p) == False):
        p = random.randint(0, 100)
    while(isprime(q) == False and q != p):
        q = random.randint(0, 100)
    return p, q


def generatePublicKey(t):
    e = random.randint(0, t-1)
    while(isprime(e) == False):
        e = random.randint(0, t-1)
    return e


def generatePrivateKey(e, t):
    d = 1
    while((d*e) % t != 1):
        d += 1
    return d


def encrypt(plainText, public, n):
    plainText = plainText.upper()
    cipher = []
    for c in plainText:
        cipher.append(pow(ord(c), public) % n)
    return cipher


def decrypt(cipher, private, n):
    plainText = ""
    for c in cipher:
        plainText += chr(pow(c, private) % n)
    return plainText


# p,q = generate()
p, q = 59, 37
n = p*q
t = (p-1)*(q-1)
# e = generatePublicKey(t)
e = 1723
# d = generatePrivateKey(e,t)
d = 1699
print(f"P = {p}, Q = {q}")
print(f"n = p*q = {n}")
print(f"t = (p-1)*(q-1) = {t}")
print(f"Public key = {e}")
print(f"Private key = {d}")
plainText = "TEST"
cipherText = encrypt(plainText, e, n)
decrypted = decrypt(cipherText, d, n)
print(f"encrypt of {plainText} is {cipherText}")
print(f"decrypt of {cipherText} is {decrypted}")
