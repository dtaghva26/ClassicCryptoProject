from app.cipher_algorithms.cipher import Cipher
from pycipher import Vigenere
from app.cipher_algorithms.wrapper_cipher import PyCipherWrapper
class VigenereCipher(PyCipherWrapper):
    def __init__(self, key):
        super().__init__(Vigenere(key))