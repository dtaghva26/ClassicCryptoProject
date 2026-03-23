from typing import List, Tuple
from app.cipher_algorithms.cipher import Cipher


class Pipeline:
    def __init__(self, name: str, steps: List[Cipher]):
        if not steps:
            raise ValueError("Pipeline must contain at least one step.")

        for step in steps:
            if not hasattr(step, "encrypt") or not hasattr(step, "decrypt"):
                raise TypeError("All steps must implement encrypt() and decrypt()")

        self.name = name
        self.steps = steps

    def encrypt(self, text: str) -> str:
        result = text
        for cipher in self.steps:
            result = cipher.encrypt(result)
        return result

    def decrypt(self, text: str) -> str:
        result = text
        for cipher in reversed(self.steps):
            result = cipher.decrypt(result)
        return result

    def trace_encrypt(self, text: str) -> List[Tuple[str, str]]:
        """
        Returns a step-by-step trace of encryption.
        Each entry: (step_name, result)
        """
        result = text
        history = [("start", result)]

        for cipher in self.steps:
            result = cipher.encrypt(result)
            history.append((type(cipher).__name__, result))

        return history

    def trace_decrypt(self, text: str) -> List[Tuple[str, str]]:
        """
        Returns a step-by-step trace of decryption.
        Each entry: (step_name, result)
        """
        result = text
        history = [("start", result)]

        for cipher in reversed(self.steps):
            result = cipher.decrypt(result)
            history.append((type(cipher).__name__, result))

        return history

    def __repr__(self) -> str:
        step_names = " -> ".join(type(s).__name__ for s in self.steps)
        return f"<Pipeline {self.name}: {step_names}>"
    