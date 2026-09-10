# Theory: Shor order finding

For an odd composite `N`, choose `a` with `1 < a < N`.

If `gcd(a, N) != 1`, a factor has already been found classically. Otherwise Shor reduces factoring to finding the multiplicative order `r` such that:

`a^r = 1 (mod N)`.

The quantum subroutine creates a superposition over exponents, computes `a^x mod N` reversibly, and applies an inverse QFT to expose peaks related to rational values `s/r`.

A measurement `k` from a `Q = 2^t` counting register approximates:

`k / Q ≈ s / r`.

Continued fractions recover a candidate denominator. The candidate is validated before it is used.

When `r` is even and `a^(r/2) != -1 (mod N)`, non-trivial factors can be obtained from:

`gcd(a^(r/2) - 1, N)` and `gcd(a^(r/2) + 1, N)`.

## What the simulator does not do

It does not claim to represent fault-tolerant hardware cost, error correction, gate synthesis cost or cryptographically relevant RSA factorization. Statevector memory scales exponentially, so the included simulator deliberately targets small teaching examples.
