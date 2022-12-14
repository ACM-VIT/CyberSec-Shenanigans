'''
Wiki page - for reference and algo
AES - https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
DES - https://en.wikipedia.org/wiki/Data_Encryption_Standard
blowfish - https://en.wikipedia.org/wiki/Blowfish_(cipher)
twofish - https://en.wikipedia.org/wiki/Twofish
'''

def key_generation():
    pass

def key_exchange(sender, recipient):
    pass

class CipherName(object):
    def __init__(self) -> None:
        # self.blockSize
        # self.key
        pass

    def encryption(plaintext, key):
        # return ciphertetxt
        pass

    def decryption(ciphertext, key):
        # return plaintext
        pass

    def pad(plaintext):
        # return padded_plaintext
        pass

    def unpad(plaintext):
        # return unpadded_plaintext
        pass

def hashing(file_path):
    pass

def signing(file_path):
    pass

def verify_hash(file_path, given_hash):
    pass

def verify_sign(file_path, given_sign):
    pass