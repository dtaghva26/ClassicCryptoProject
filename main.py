from enum import Enum
from app.cipher_algorithms.caesar_cipher import CaesarCipher
from app.cipher_algorithms.vigenere_cipher import VigenereCipher
from app.cipher_algorithms.autokey_cipher import AutoKeyCipher
from app.pipeline.Pipeline import Pipeline
from app.utils.trace_utils import print_trace


class Mode(Enum):
    SILENT = "silent"
    VERBOSE = "verbose"


def run_system(system, text: str, mode: Mode):
    if mode == Mode.VERBOSE and hasattr(system, "trace_encrypt"):
        encrypt_trace = system.trace_encrypt(text)
        encrypted = encrypt_trace[-1][1]

        decrypt_trace = system.trace_decrypt(encrypted)
        decrypted = decrypt_trace[-1][1]

        return encrypted, decrypted, encrypt_trace, decrypt_trace

    encrypted = system.encrypt(text)
    decrypted = system.decrypt(encrypted)

    return encrypted, decrypted, None, None


def evaluate(original: str, decrypted: str) -> bool:
    return original == decrypted


def print_report(name: str, original: str, encrypted: str, decrypted: str, passed: bool):
    print(f"\n=== {name} ===")
    print(f"Plaintext : {original}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")
    print("✅ PASS" if passed else "❌ FAIL")


def test(system, name: str, text: str, mode: Mode = Mode.SILENT):
    encrypted, decrypted, enc_trace, dec_trace = run_system(system, text, mode)

    passed = evaluate(text, decrypted)
    print_report(name, text, encrypted, decrypted, passed)

    if mode == Mode.VERBOSE and enc_trace and dec_trace:
        print_trace("TRACE ENCRYPT", enc_trace)
        print_trace("TRACE DECRYPT", dec_trace)


if __name__ == "__main__":
    text = "HELLOWORLD"

    pipeline = Pipeline(
        "Caesar + Vigenere",
        [
            CaesarCipher(3),
            VigenereCipher("KEY"),
        ],
    )

    systems = [
        ("Caesar", CaesarCipher(3), Mode.SILENT),
        ("Vigenere", VigenereCipher("KEY"), Mode.SILENT),
        ("Autokey", AutoKeyCipher("KEY"), Mode.SILENT),
        ("Pipeline", pipeline, Mode.VERBOSE),
    ]

    for name, system, mode in systems:
        test(system, name, text, mode)