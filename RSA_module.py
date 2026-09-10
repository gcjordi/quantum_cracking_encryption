"""Compatibility notice for Quantum Cryptography Lab v2.0.

The original 2021 RSA_module.py was intentionally replaced. Use
quantum_crypto_lab.rsa_demo for the safe, clearly labelled educational API.
"""

from quantum_crypto_lab import rsa_demo as _rsa_demo

ToyRSAKeyPair = _rsa_demo.ToyRSAKeyPair
build_toy_keypair = _rsa_demo.build_toy_keypair
decrypt_int = _rsa_demo.decrypt_int
encrypt_int = _rsa_demo.encrypt_int
recover_private_key_from_factors = _rsa_demo.recover_private_key_from_factors

__all__ = [
    "ToyRSAKeyPair",
    "build_toy_keypair",
    "decrypt_int",
    "encrypt_int",
    "recover_private_key_from_factors",
]
