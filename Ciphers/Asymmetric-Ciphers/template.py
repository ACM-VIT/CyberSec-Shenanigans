'''
Wiki page - for reference and algo
RSA - https://en.wikipedia.org/wiki/RSA_(cryptosystem)
ElGamal - https://en.wikipedia.org/wiki/ElGamal_encryption
'''

def key_generation():
    pass

def key_exchange(sender, recipient):
    pass

class CipherName(object):
    def __init__(self) -> None:
        # self.blockSize
        # self.publicKey
        # self.privateKey
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