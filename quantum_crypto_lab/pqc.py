"""Small machine-readable map of the current NIST post-quantum standards."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PQCStandard:
    fips: str
    algorithm: str
    purpose: str
    standardized: str
    notes: str


PQC_STANDARDS: tuple[PQCStandard, ...] = (
    PQCStandard(
        "FIPS 203",
        "ML-KEM",
        "Key encapsulation / establishing shared secrets",
        "2024",
        "Primary NIST post-quantum KEM standard, derived from CRYSTALS-Kyber.",
    ),
    PQCStandard(
        "FIPS 204",
        "ML-DSA",
        "Digital signatures",
        "2024",
        "Primary NIST lattice-based signature standard, derived from CRYSTALS-Dilithium.",
    ),
    PQCStandard(
        "FIPS 205",
        "SLH-DSA",
        "Digital signatures",
        "2024",
        "Stateless hash-based signature standard, derived from SPHINCS+.",
    ),
)


def quantum_threat_for_primitive(name: str) -> str:
    normalized = name.strip().lower().replace("_", "-")
    if normalized in {"rsa", "dh", "diffie-hellman", "ecdh", "ecdsa", "ecc"}:
        return "High: a cryptographically relevant quantum computer running Shor threatens this primitive."
    if normalized in {"aes", "sha-2", "sha2", "sha-3", "sha3"}:
        return "Reduced security margin: Grover-style search changes symmetric/hash security assumptions, not in the same way as Shor."
    if normalized in {"ml-kem", "ml-dsa", "slh-dsa"}:
        return "Designed for post-quantum security under the assumptions used by the corresponding standard."
    return "Unknown primitive: assess its underlying hard problem and current cryptanalytic evidence."
