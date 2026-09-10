"""Tiny RSA implementation for education only.

This module intentionally operates on integer messages and tiny key sizes so
that the modulus can be factored by the included Shor simulator. It must never
be used as production cryptography.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .math_utils import is_prime


@dataclass(frozen=True)
class ToyRSAKeyPair:
    p: int
    q: int
    n: int
    phi: int
    e: int
    d: int

    @property
    def public_key(self) -> tuple[int, int]:
        return self.e, self.n

    @property
    def private_key(self) -> tuple[int, int]:
        return self.d, self.n


def build_toy_keypair(p: int = 5, q: int = 7, e: int = 5) -> ToyRSAKeyPair:
    if p == q or not is_prime(p) or not is_prime(q):
        raise ValueError("p and q must be distinct primes")
    n = p * q
    phi = (p - 1) * (q - 1)
    if not 1 < e < phi or gcd(e, phi) != 1:
        raise ValueError("e must satisfy 1 < e < phi and gcd(e, phi) == 1")
    d = pow(e, -1, phi)
    return ToyRSAKeyPair(p, q, n, phi, e, d)


def encrypt_int(message: int, public_key: tuple[int, int]) -> int:
    e, n = public_key
    if not 0 <= message < n:
        raise ValueError(f"message must be an integer in [0, {n})")
    return pow(message, e, n)


def decrypt_int(ciphertext: int, private_key: tuple[int, int]) -> int:
    d, n = private_key
    if not 0 <= ciphertext < n:
        raise ValueError(f"ciphertext must be an integer in [0, {n})")
    return pow(ciphertext, d, n)


def recover_private_key_from_factors(
    public_key: tuple[int, int], p: int, q: int
) -> tuple[int, int]:
    e, n = public_key
    if p * q != n:
        raise ValueError("p and q do not factor the public modulus")
    phi = (p - 1) * (q - 1)
    return pow(e, -1, phi), n
