from app.cipher_algorithms.cipher import Cipher
class PyCipherWrapper(Cipher):
    def __init__(self, algorithm):
        super().__init__()
        self.algorithm = algorithm

    def encrypt(self, text):
        return self.algorithm.encipher(text)

    def decrypt(self, text):
        return self.algorithm.decipher(text)