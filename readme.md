# Classic Crypto Project

A small educational Python project that demonstrates classic substitution ciphers and cipher composition.

> ⚠️ **Security notice:** These algorithms are historically important for learning but are **not secure** for modern cryptographic use.

## Features

- Implementations of classic ciphers using `pycipher` wrappers:
  - Caesar
  - Vigenère
  - Autokey
  - Affine
- A `Pipeline` abstraction to chain multiple ciphers (encrypt in order, decrypt in reverse).
- Optional verbose tracing for pipeline step-by-step transformations.
- Lightweight CLI-style execution via `main.py`.

## Tech Stack

- Python 3.10+
- [`pycipher`](https://pypi.org/project/pycipher/)
- `pytest` (dependency present for adding/running tests)

## Repository Structure

```text
.
├── app/
│   ├── cipher_algorithms/
│   │   ├── cipher.py
│   │   ├── wrapper_cipher.py
│   │   ├── caesar_cipher.py
│   │   ├── vigenere_cipher.py
│   │   ├── autokey_cipher.py
│   │   └── affine_cipher.py
│   ├── pipeline/
│   │   └── Pipeline.py
│   └── utils/
│       └── trace_utils.py
├── main.py
├── requirements.txt
└── readme.md
```

## Getting Started

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd ClassicCryptoProject
```

### 2) Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows PowerShell
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the project

```bash
python main.py
```

## Example Output Behavior

`main.py` runs:

1. Caesar cipher test
2. Vigenère cipher test
3. Autokey cipher test
4. A composed pipeline (`Caesar(3) -> Vigenere("KEY")`)

For each, it prints:

- plaintext
- encrypted text
- decrypted text
- pass/fail round-trip check

Pipeline mode also prints verbose encryption/decryption traces.

## Usage Patterns

### Run a single cipher in code

```python
from app.cipher_algorithms.caesar_cipher import CaesarCipher

cipher = CaesarCipher(3)
ciphertext = cipher.encrypt("HELLOWORLD")
plaintext = cipher.decrypt(ciphertext)
```

### Build a custom pipeline

```python
from app.pipeline.Pipeline import Pipeline
from app.cipher_algorithms.caesar_cipher import CaesarCipher
from app.cipher_algorithms.vigenere_cipher import VigenereCipher

pipeline = Pipeline(
    "Demo Pipeline",
    [CaesarCipher(3), VigenereCipher("KEY")],
)

ciphertext = pipeline.encrypt("HELLOWORLD")
plaintext = pipeline.decrypt(ciphertext)
trace = pipeline.trace_encrypt("HELLOWORLD")
```

## Engineering Notes

- `Pipeline` validates that each step exposes `encrypt()` and `decrypt()`.
- Decryption order in `Pipeline` is automatically reversed.
- `AutoKeyCipher` is marked stateful (`is_stateful = True`) for extensibility.

## Limitations / Assumptions

- Inputs are expected to be compatible with `pycipher` behavior (typically uppercase alphabetic text).
- No CLI argument parsing yet (execution is currently driven by `main.py`).
- Automated tests are not yet implemented in this repository.

## Testing

When tests are added, run:

```bash
pytest -q
```

## Roadmap (Suggested)

- Add proper unit tests for each cipher and pipeline edge cases.
- Add linting/formatting (`ruff`, `black`) and CI workflow.
- Add a real CLI (`argparse`/`typer`) for user-provided text, keys, and mode.
- Add error handling for invalid keys and unsupported characters.
- Add benchmarking and docs for educational comparisons.

## Contributing

1. Fork the repo
2. Create a feature branch
3. Make changes with tests/docs
4. Open a pull request

## License

No license file is currently present. Add a `LICENSE` file if you plan to distribute this project publicly.
