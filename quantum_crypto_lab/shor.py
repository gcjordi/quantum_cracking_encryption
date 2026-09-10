"""Educational Shor factorization workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from math import gcd, isqrt
from typing import Iterable

from .backends import NumpyStatevectorBackend, OrderFindingBackend, OrderFindingResult
from .math_utils import (
    is_prime,
    nontrivial_factors_from_order,
    recover_order_from_measurement,
)


@dataclass(frozen=True)
class Attempt:
    base: int
    route: str
    order: int | None = None
    factors: tuple[int, int] | None = None
    measurement: int | None = None
    note: str = ""


@dataclass(frozen=True)
class FactorizationResult:
    n: int
    factors: tuple[int, int] | None
    success: bool
    backend_name: str
    attempts: tuple[Attempt, ...] = field(default_factory=tuple)


class ShorSimulator:
    """Coordinate Shor's classical preprocessing/postprocessing and backend."""

    def __init__(self, backend: OrderFindingBackend | None = None) -> None:
        self.backend = backend or NumpyStatevectorBackend()

    @staticmethod
    def _default_bases(n: int) -> Iterable[int]:
        preferred = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
        yielded: set[int] = set()
        for a in preferred:
            if 1 < a < n:
                yielded.add(a)
                yield a
        for a in range(2, min(n, 64)):
            if a not in yielded:
                yield a

    @staticmethod
    def _ranked_measurements(result: OrderFindingResult) -> list[int]:
        return [
            k for k, _count in sorted(
                result.counts.items(), key=lambda item: (-item[1], item[0])
            )
            if k != 0
        ]

    def factor(
        self,
        n: int,
        *,
        shots: int = 4096,
        seed: int | None = 7,
        max_bases: int = 12,
        counting_qubits: int | None = None,
        prefer_quantum_path: bool = True,
    ) -> FactorizationResult:
        if n < 2:
            raise ValueError("n must be >= 2")
        if n % 2 == 0:
            return FactorizationResult(n, (2, n // 2), True, self.backend.name, (
                Attempt(2, "classical-precheck", factors=(2, n // 2), note="n is even"),
            ))
        if is_prime(n):
            return FactorizationResult(n, None, False, self.backend.name, (
                Attempt(0, "classical-precheck", note="n is prime"),
            ))
        root = isqrt(n)
        if root * root == n:
            return FactorizationResult(n, (root, root), True, self.backend.name, (
                Attempt(root, "classical-precheck", factors=(root, root), note="perfect square"),
            ))

        attempts: list[Attempt] = []
        used = 0
        for a in self._default_bases(n):
            if used >= max_bases:
                break
            used += 1
            g = gcd(a, n)
            if g != 1:
                factors = tuple(sorted((g, n // g)))
                attempts.append(Attempt(a, "gcd-shortcut", factors=factors))
                if prefer_quantum_path:
                    continue
                return FactorizationResult(n, factors, True, self.backend.name, tuple(attempts))

            measurement_result = self.backend.run_order_finding(
                a,
                n,
                counting_qubits=counting_qubits,
                shots=shots,
                seed=None if seed is None else seed + used,
            )
            seen_orders: set[int] = set()
            for k in self._ranked_measurements(measurement_result):
                r = recover_order_from_measurement(k, measurement_result.q, a, n)
                if r is None or r in seen_orders:
                    continue
                seen_orders.add(r)
                factors = nontrivial_factors_from_order(a, r, n)
                attempts.append(
                    Attempt(a, "quantum-order-finding", order=r, factors=factors, measurement=k)
                )
                if factors is not None:
                    return FactorizationResult(n, factors, True, self.backend.name, tuple(attempts))
            if not seen_orders:
                attempts.append(
                    Attempt(a, "quantum-order-finding", note="no valid order recovered")
                )

        for attempt in attempts:
            if attempt.route == "gcd-shortcut" and attempt.factors:
                return FactorizationResult(n, attempt.factors, True, self.backend.name, tuple(attempts))
        return FactorizationResult(n, None, False, self.backend.name, tuple(attempts))


def factor_integer(n: int, **kwargs: object) -> FactorizationResult:
    """Convenience wrapper using the portable NumPy backend."""
    return ShorSimulator().factor(n, **kwargs)
