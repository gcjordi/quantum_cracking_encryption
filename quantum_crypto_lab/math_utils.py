"""Classical number-theory helpers used around Shor's quantum subroutine."""

from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = isqrt(n)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True


def multiplicative_order(a: int, n: int) -> int:
    """Return the smallest r > 0 such that a**r = 1 (mod n).

    This is classical and is intentionally used only for validation/tests or
    the explicit classical backend, never to fake a quantum measurement.
    """
    if n <= 1 or gcd(a, n) != 1:
        raise ValueError("multiplicative order requires n > 1 and gcd(a, n) == 1")
    x = 1
    for r in range(1, n + 1):
        x = (x * a) % n
        if x == 1:
            return r
    raise ArithmeticError("order not found; inputs may be invalid")


def recover_order_from_measurement(k: int, q: int, a: int, n: int) -> int | None:
    """Recover a candidate order from a QPE measurement k / q.

    Continued fractions produce a denominator that can be a divisor of the
    true order. Small multiples are therefore checked and the smallest valid
    order candidate is returned.
    """
    if k <= 0 or q <= 0:
        return None
    denominator = Fraction(k, q).limit_denominator(n).denominator
    for multiple in range(1, n // denominator + 1):
        r = denominator * multiple
        if pow(a, r, n) == 1:
            return r
    return None


def nontrivial_factors_from_order(a: int, r: int, n: int) -> tuple[int, int] | None:
    """Classical post-processing step of Shor's algorithm."""
    if r <= 0 or r % 2:
        return None
    x = pow(a, r // 2, n)
    if x in (1, n - 1):
        return None
    p = gcd(x - 1, n)
    q = gcd(x + 1, n)
    if 1 < p < n and 1 < q < n and p * q == n:
        return tuple(sorted((p, q)))
    return None
