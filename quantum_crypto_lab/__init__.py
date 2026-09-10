"""Quantum Cryptography Lab v2.0.

Educational, provider-neutral simulations of Shor order finding, toy RSA,
and the migration context for post-quantum cryptography.
"""

from .pqc import PQC_STANDARDS, quantum_threat_for_primitive
from .rsa_demo import ToyRSAKeyPair, build_toy_keypair, decrypt_int, encrypt_int
from .shor import FactorizationResult, ShorSimulator, factor_integer

__all__ = [
    "PQC_STANDARDS",
    "FactorizationResult",
    "ShorSimulator",
    "ToyRSAKeyPair",
    "build_toy_keypair",
    "decrypt_int",
    "encrypt_int",
    "factor_integer",
    "quantum_threat_for_primitive",
]

__version__ = "2.0.0"
