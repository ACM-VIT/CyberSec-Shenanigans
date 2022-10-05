def encrypt():
    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key value: "))
    print("Ciphertext is", getCiphertext(plaintext, key))

def decrypt():
    plaintext = input("Enter ciphertext: ")
    key = int(input("Enter key value: "))
    print("Plaintext is", getPlaintext(plaintext, key))

def getCiphertext(plaintext: str, key: int) -> str:
    key = key % 26
    return shift(plaintext, key)

def getPlaintext(ciphertext: str, key: int) -> str:
    key = 26 - key % 26 
    return shift(ciphertext, key)

def shift(text: str, shift_val: int) -> str:
    shifted_text = []
    for ch in text:
        if ch.isupper():
            shifted_text.append(chr((ord(ch) + shift_val - 65) % 26 + 65))
        elif ch.islower():
            shifted_text.append(chr((ord(ch) + shift_val - 97) % 26 + 97))
        else:
            shifted_text.append(ch)
    return ''.join(shifted_text)

if __name__ == "__main__":
    encrypt()
    decrypt()
    