from app.cipher_algorithms.wrapper_cipher import PyCipherWrapper
from pycipher import Autokey

class AutoKeyCipher(PyCipherWrapper):
    def __init__(self, key):
        super().__init__(Autokey(key))
        self.is_stateful = True