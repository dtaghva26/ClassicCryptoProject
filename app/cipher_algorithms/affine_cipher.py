from app.cipher_algorithms.cipher import Cipher
from pycipher import Affine
class AffineCipher(Cipher):
    def __init__(self, key):
        self.algorithm = Affine(key)
    def encrypt(self, text):
        return self.algorithm.encipher(text)
    def decrypt(self, text):
        return self.algorithm.decipher(text)