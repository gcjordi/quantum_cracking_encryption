# Contributing

Contributions that improve correctness, portability, documentation, tests or educational clarity are welcome.

## Design principles

Please preserve these project boundaries:

1. Keep the core provider-neutral. Provider-specific integrations must be optional adapters.
2. Never present a classical shortcut as a quantum result.
3. Keep cryptographically relevant claims clearly separated from tiny educational simulations.
4. Add or update tests for mathematical and behavioral changes.
5. Do not present the toy RSA module as production cryptography.
6. Do not commit credentials, API keys, private keys, secrets or sensitive data.

## Development setup

Use Python 3.10 or newer.

```bash
python -m pip install -e '.[dev]'
pytest
ruff check quantum_crypto_lab tests
```

For the optional Gradio UI:

```bash
python -m pip install -e '.[ui]'
python app.py
```

## Pull requests

Keep changes focused, explain the motivation, and include tests when behavior changes. For notebook changes, avoid committing temporary checkpoints and unnecessary execution artifacts.

If a change introduces a claim about Shor's algorithm, RSA resource requirements, post-quantum standards, or another time-sensitive technical fact, include a primary or authoritative source where practical.

All pull requests should pass the repository CI, CodeQL checks where applicable, and dependency review.

## Issues and security

Use the issue forms for bugs and feature requests. For vulnerabilities or sensitive findings, follow `SECURITY.md` instead of opening a public issue.

By contributing, you agree that your contribution is distributed under the repository's GPL-3.0 license.
