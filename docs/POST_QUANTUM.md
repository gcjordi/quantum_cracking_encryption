# Post-Quantum Cryptography Context

Shor's algorithm is strategically important because sufficiently capable fault-tolerant quantum computers threaten RSA, finite-field Diffie-Hellman and elliptic-curve discrete-logarithm systems.

NIST's first finalized post-quantum standards were published in 2024:

| Standard | Algorithm | Main role |
|---|---|---|
| FIPS 203 | ML-KEM | Key encapsulation / shared-secret establishment |
| FIPS 204 | ML-DSA | Digital signatures |
| FIPS 205 | SLH-DSA | Stateless hash-based digital signatures |

This repository treats post-quantum migration as the defensive counterpart of the Shor demonstration. It does not implement production PQC primitives itself; production deployments should use maintained, reviewed implementations that conform to the relevant standards.

## Migration mindset

A practical migration program normally starts by inventorying where vulnerable public-key cryptography is used, identifying data that must remain confidential for many years, designing crypto-agility, testing PQC/hybrid paths and planning staged replacement.

The risk commonly described as **harvest now, decrypt later** means long-lived confidential traffic may matter before a cryptographically relevant quantum computer exists.
