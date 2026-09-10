"""Deterministic validation backend.

This backend is NOT quantum simulation. It exists for unit tests, CI and for
showing the boundary between Shor's classical and quantum components.
"""

from __future__ import annotations

from math import ceil, log2

from ..math_utils import multiplicative_order
from .base import OrderFindingResult


class ClassicalExactOrderBackend:
    name = "classical-exact-order (validation only)"

    def run_order_finding(
        self,
        a: int,
        n: int,
        *,
        counting_qubits: int | None = None,
        shots: int = 4096,
        seed: int | None = 7,
    ) -> OrderFindingResult:
        del seed
        if shots <= 0:
            raise ValueError("shots must be positive")
        t = counting_qubits or 2 * max(1, ceil(log2(n)))
        q = 1 << t
        r = multiplicative_order(a, n)
        # Ideal peaks near s/r, represented here deterministically. This is a
        # validation fixture, not a substitute for the NumPy quantum backend.
        peaks = sorted({round(s * q / r) % q for s in range(r)})
        base = shots // len(peaks)
        remainder = shots - base * len(peaks)
        counts = {
            k: base + (1 if index < remainder else 0)
            for index, k in enumerate(peaks)
            if base + (1 if index < remainder else 0) > 0
        }
        probs = [0.0] * q
        for k in peaks:
            probs[k] = 1.0 / len(peaks)
        return OrderFindingResult(a, n, t, shots, counts, tuple(probs), self.name)
