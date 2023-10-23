def encrypt(text, key):
    result = ""
    for i in text:
        if(i.isupper()):
            result += chr((ord(i) + key - ord('A'))%26 + ord('A'))
        else:
            result += chr((ord(i) + key - ord('a'))%26 + ord('a'))
            
    return result

def decrypt(text, key):
    result = ""
    for i in text:
        if(i.isupper()):
            result += chr((ord(i) - key - ord('A'))%26 + ord('A'))
        else:
            result += chr((ord(i) - key - ord('a'))%26 + ord('a'))
            
    return result


text = "Hello"
key = 5
en = encrypt(text, key)
de = decrypt(en,key)
print(f"encrypt of {text} is {en}")
print(f"decrypt of {en} is {de}") 
