# Pavich sangwaree 6320502452
# RSA

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def isCoprime(x, y):
    return gcd(x, y) == 1


def generatePrivateKey(e, t):
    d = 1
    while((d*e) % t != 1):
        d += 1
    return d


def encrypt(plainText, public, n):
    plainText = plainText.upper()
    cipher = ""
    for c in plainText:
        cipher += str(pow(ord(c) - ord('A'), public) % n)
        cipher += "-"
    return cipher[:-1]


def decrypt(cipher, private, n):
    plainText = ""
    cipher = cipher.split('-')
    for c in cipher:
        plainText += chr((pow(int(c), private) % n) + ord('A'))
    return plainText


print("Welcome to RSA!")
p = int(input("Enter prime p:"))
q = int(input("Enter prime q:"))
n = p*q
t = (p-1)*(q-1)
print(f"The value of n is {p}x{q}= {n}")
e = int(input(f"Enter co-prime e ]1,{t}[:"))
while(not isCoprime(e, t)):
    print(f"Sorry! {e} is not co-prime of ({p}-1)({q}-1)={t}.")
    e = int(input(f"Enter co-prime e ]1,{t}[:"))
d = generatePrivateKey(e, t)
type = input("Enter the progress type E/D:")
if(type != 'E' and type != 'e' and type != 'D' and type != 'd'):
    print(f"Invalid input")
    exit(1)
if(type == 'E' or type == 'e'):
    plainText = input("Enter the plaintext:")
    ciphertext = encrypt(plainText, e, n)
    print(f"The ciphertext is {ciphertext}")
else:
    ciphertext = input("Enter the ciphertext:")
    plainText = decrypt(ciphertext, d, n)
    print(f"The private key d is {d}")
    print(f"The ciphertext is {plainText}")
