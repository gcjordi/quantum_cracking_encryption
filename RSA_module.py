"""Compatibility notice for Quantum Cryptography Lab v2.0.

The original 2021 RSA_module.py was intentionally replaced. Use
quantum_crypto_lab.rsa_demo for the safe, clearly labelled educational API.
"""

from quantum_crypto_lab.rsa_demo import (  # noqa: F401
    ToyRSAKeyPair,
    build_toy_keypair,
    decrypt_int,
    encrypt_int,
    recover_private_key_from_factors,
)
