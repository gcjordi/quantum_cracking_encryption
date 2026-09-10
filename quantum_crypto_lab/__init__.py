"""Quantum Cryptography Lab v2.0.

Educational, provider-neutral simulations of Shor order finding, toy RSA,
and the migration context for post-quantum cryptography.
"""

from .shor import FactorizationResult, ShorSimulator, factor_integer
from .rsa_demo import ToyRSAKeyPair, build_toy_keypair, encrypt_int, decrypt_int
from .pqc import PQC_STANDARDS, quantum_threat_for_primitive

__all__ = [
    "FactorizationResult",
    "ShorSimulator",
    "factor_integer",
    "ToyRSAKeyPair",
    "build_toy_keypair",
    "encrypt_int",
    "decrypt_int",
    "PQC_STANDARDS",
    "quantum_threat_for_primitive",
]

__version__ = "2.0.0"
