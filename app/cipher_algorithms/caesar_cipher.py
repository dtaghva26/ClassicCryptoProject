from pycipher import Caesar
from app.cipher_algorithms.wrapper_cipher import PyCipherWrapper
class CaesarCipher(PyCipherWrapper):
    def __init__(self, key):
        super().__init__(Caesar(key))