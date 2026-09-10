# Quantum Cryptography Lab v2.0

[![CI](https://github.com/gcjordi/quantum_cracking_encryption/actions/workflows/tests.yml/badge.svg)](https://github.com/gcjordi/quantum_cracking_encryption/actions/workflows/tests.yml)
[![CodeQL](https://github.com/gcjordi/quantum_cracking_encryption/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/gcjordi/quantum_cracking_encryption/actions/workflows/codeql-analysis.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gcjordi/quantum_cracking_encryption/blob/master/Colab_Quickstart.ipynb)

A provider-neutral educational laboratory for understanding **Shor's algorithm, RSA risk and the transition to post-quantum cryptography**.

I originally created this repository as an experiment around RSA factorization and Shor's algorithm. In v2.0 I rebuilt the project to make the scientific boundary clearer, remove the old IBM Quantum dependency, modernize the codebase, and connect the demonstration to the current post-quantum cryptography landscape.

> **Important:** this repository is an educational simulator. It does not break real-world RSA keys and it is not production cryptographic software.

## What v2.0 does

- Simulates the quantum **order-finding** core of Shor's algorithm for small composite integers.
- Models the state after reversible modular exponentiation: `|x>|a^x mod N>`.
- Applies the **inverse Quantum Fourier Transform** numerically using a unitary FFT-equivalent operation.
- Recovers the period with **continued fractions** and performs Shor's classical post-processing.
- Demonstrates how recovering the factors of a toy RSA modulus allows reconstruction of its private key.
- Includes machine-readable information about NIST's post-quantum standards: **ML-KEM, ML-DSA and SLH-DSA**.
- Includes dated research context for published RSA-2048 quantum resource estimates.

## Provider-neutral by design

The core implementation does **not** require IBM Quantum, IBM Cloud, an API key, a quantum account, Qiskit, Cirq, AWS Braket, Azure Quantum or any other provider.

The default backend is a small **NumPy statevector simulator** designed specifically for the educational order-finding experiment. The same notebooks can therefore run in:

- Google Colab
- JupyterLab / Jupyter Notebook
- AWS EC2, SageMaker or other Python notebook environments
- Azure, GCP or local Python environments
- GitHub Codespaces

The backend API is separated from Shor's classical orchestration, so additional engines can be added later without rewriting the rest of the project.

## Quick start

### Google Colab

Use the **Open In Colab** badge above or open `Colab_Quickstart.ipynb` and run the cells. The bootstrap cell installs the repository package automatically from GitHub when needed.

### Existing checkout / notebook environment

```python
from quantum_crypto_lab import factor_integer

result = factor_integer(15)
print(result.factors)
# (3, 5)
```

Try other deliberately small educational examples:

```python
for n in (15, 21, 35):
    result = factor_integer(n)
    print(n, result.factors, result.backend_name)
```

## Toy RSA demonstration

```python
from quantum_crypto_lab import ShorSimulator, build_toy_keypair, decrypt_int, encrypt_int
from quantum_crypto_lab.rsa_demo import recover_private_key_from_factors

key = build_toy_keypair(p=5, q=7, e=5)
message = 12
ciphertext = encrypt_int(message, key.public_key)

factored = ShorSimulator().factor(key.n)
p, q = factored.factors
recovered_private = recover_private_key_from_factors(key.public_key, p, q)
recovered_message = decrypt_int(ciphertext, recovered_private)

print(message, ciphertext, recovered_message)
```

## Notebooks

- `Colab_Quickstart.ipynb` — easiest portable entry point.
- `Breaking_RSA.ipynb` — end-to-end toy RSA → Shor → recovered private key demonstration.
- `Factorizer_Quantum_Simulator.ipynb` — factor 15, 21 and 35 and inspect order-finding measurements.
- `notebooks/01_shor_order_finding.ipynb` — deeper look at QPE/QFT measurement peaks.
- `notebooks/02_rsa_quantum_risk.ipynb` — what the toy experiment does and does not imply for real RSA.
- `notebooks/03_post_quantum_transition.ipynb` — NIST PQC standards and migration context.

## Scientific scope

The simulator is intentionally limited to small integers. A statevector simulator has exponential memory requirements and cannot scale to cryptographically relevant RSA sizes. This is a feature of the educational boundary, not a claim that RSA-2048 can be attacked on a laptop.

The included RSA-2048 resource figures are **published research estimates**, not predictions of when a cryptographically relevant quantum computer will exist.

## Why the old implementation was replaced

The original notebooks used Qiskit 0.14-era APIs and an order-finding function whose measured quantum result was not actually used to derive the returned period. v2.0 replaces that mechanism rather than cosmetically refactoring it.

The new flow is:

`choose a` → `gcd pre-check` → `quantum order-finding simulation` → `QFT measurement` → `continued fractions` → `period r` → `gcd(a^(r/2) ± 1, N)` → `factors`

## Post-quantum context

Shor's algorithm threatens public-key schemes based on integer factorization and discrete logarithms, including RSA and traditional elliptic-curve public-key cryptography, once sufficiently capable fault-tolerant quantum computers exist.

NIST standardized its first post-quantum cryptography standards in 2024:

- FIPS 203 — ML-KEM
- FIPS 204 — ML-DSA
- FIPS 205 — SLH-DSA

See `docs/POST_QUANTUM.md` for the migration-oriented view.

## Repository health and security

The repository is maintained with:

- CI across Python **3.10–3.14**.
- Ruff static linting.
- GitHub CodeQL with the `security-and-quality` query suite.
- Dependency Review on pull requests.
- Dependabot version updates for Python dependencies and GitHub Actions.
- Structured bug and feature request forms.

This project only demonstrates factorization of deliberately tiny, generated educational moduli. Do not use it to target systems, keys or data you do not own or have explicit permission to test. See `SECURITY.md` for responsible disclosure.

## Project structure

```text
quantum_crypto_lab/        reusable Python package
  backends/                provider-neutral backend contract + NumPy simulator
notebooks/                 extended educational notebooks
tests/                     automated tests
docs/                      architecture, theory, PQC and research context
Breaking_RSA.ipynb         updated compatibility notebook
Factorizer_Quantum_Simulator.ipynb
Colab_Quickstart.ipynb
app.py                     optional Gradio educational UI
```

## Development

Core development installation:

```bash
python -m pip install -e '.[dev]'
pytest
ruff check quantum_crypto_lab tests
```

Optional browser UI:

```bash
python -m pip install -e '.[ui]'
python app.py
```

## Contributing

Contributions are welcome when they preserve the project's provider-neutral and educational scope. See `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and the issue/PR templates before contributing.

## License

GPL-3.0, preserving the repository's existing license.

## Author

Developed and maintained by **Jordi Garcia Castillón (gcjordi)**.
