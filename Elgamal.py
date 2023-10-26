# Pavich sangwaree 6320502452
# ElGamal Cryptosystem
# import random


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def isCoprime(x, y):
    return gcd(x, y) == 1


def encrypt(plainText, p, g, y, k):
    plainText = plainText.upper()
    pCode = ord(plainText)-ord('A')
    c1 = pow(g, k, p)
    c2 = (pCode*pow(y, k)) % p
    return c1, c2


def decrypt(c1, c2, private):
    de = (c2 * pow(c1, -private, p)) % p
    return chr(de + ord('A'))


print("Welcome to ElGamal Cryptosystem!")
p = int(input("Enter prime p: "))
g = int(input(f"Enter co-prime g [1,{p-1}[: "))
while(not isCoprime(g, p)):
    print(f"Sorry! {g} is not co-prime of {p}.")
    g = int(input(f"Enter co-prime g [1,{p-1}[: "))
x = int(input(f"Enter private key x ]1,{p-1}[: "))
y = pow(g, x, p)
print(f"Enter plublic key y is {y}")
type = input("Enter the progress type E/D: ")
if(type != 'E' and type != 'e' and type != 'D' and type != 'd'):
    print(f"Invalid input")
    exit(1)
if(type == 'E' or type == 'e'):
    plainText = input("Enter the plaintext: ")
    # k = random.randint(0, 100)
    k = 10
    # y = 7
    print(f"The random number k is {k}")
    c1, c2 = encrypt(plainText, p, g, y, k)
    print(f"The ciphertext 1 is {c1}")
    print(f"The ciphertext 1 is {c2}")
else:
    c1 = int(input("Enter the ciphertext 1: "))
    c2 = int(input("Enter the ciphertext 2: "))
    plainText = decrypt(c1, c2, x)
    print(f"The ciphertext is {plainText}")
