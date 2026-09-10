"""Portable NumPy statevector backend for Shor order finding.

This backend is independent of IBM Cloud and of any quantum vendor SDK. It
simulates the ideal mathematical state produced by modular exponentiation and
then applies the inverse QFT numerically with an FFT. It is intended for small
educational composites, not cryptographically sized RSA moduli.
"""

from __future__ import annotations

from math import ceil, gcd, log2, sqrt

import numpy as np

from .base import OrderFindingResult


class NumpyStatevectorBackend:
    name = "numpy-statevector"

    def __init__(self, *, max_state_amplitudes: int = 8_500_000) -> None:
        self.max_state_amplitudes = int(max_state_amplitudes)

    @staticmethod
    def _register_sizes(n: int, counting_qubits: int | None) -> tuple[int, int, int, int]:
        work_qubits = max(1, ceil(log2(n)))
        t = counting_qubits if counting_qubits is not None else 2 * work_qubits
        if t < 2:
            raise ValueError("counting_qubits must be >= 2")
        q = 1 << t
        work_dim = 1 << work_qubits
        return work_qubits, t, q, work_dim

    def exact_probabilities(
        self, a: int, n: int, *, counting_qubits: int | None = None
    ) -> np.ndarray:
        if n < 3 or n % 2 == 0:
            raise ValueError("order finding expects an odd n >= 3")
        if not 1 < a < n:
            raise ValueError("a must satisfy 1 < a < n")
        if gcd(a, n) != 1:
            raise ValueError("quantum order finding requires gcd(a, n) == 1")

        _work_qubits, _t, q, work_dim = self._register_sizes(n, counting_qubits)
        amplitudes = q * work_dim
        if amplitudes > self.max_state_amplitudes:
            raise MemoryError(
                f"Simulation requires {amplitudes:,} complex amplitudes. "
                "Use a smaller n/counting register or a different backend."
            )

        # After Hadamards on the counting register and reversible modular
        # exponentiation: (1/sqrt(Q)) sum_x |x>|a^x mod N>.
        state = np.zeros((q, work_dim), dtype=np.complex128)
        amp = 1.0 / sqrt(q)
        value = 1
        for x in range(q):
            state[x, value] = amp
            value = (value * a) % n

        # Inverse QFT on the counting register. numpy.fft.fft implements the
        # exp(-2*pi*i*x*k/Q) convention; the additional 1/sqrt(Q) makes it
        # unitary. Measurement probabilities marginalize over the work reg.
        transformed = np.fft.fft(state, axis=0) / sqrt(q)
        probs = np.sum(np.abs(transformed) ** 2, axis=1).real
        probs /= probs.sum()
        return probs

    def run_order_finding(
        self,
        a: int,
        n: int,
        *,
        counting_qubits: int | None = None,
        shots: int = 4096,
        seed: int | None = 7,
    ) -> OrderFindingResult:
        if shots <= 0:
            raise ValueError("shots must be positive")
        probs = self.exact_probabilities(a, n, counting_qubits=counting_qubits)
        t = round(log2(len(probs)))
        rng = np.random.default_rng(seed)
        sampled = rng.multinomial(shots, probs)
        counts = {int(k): int(v) for k, v in enumerate(sampled) if v}
        return OrderFindingResult(
            a=a,
            n=n,
            counting_qubits=t,
            shots=shots,
            counts=counts,
            probabilities=tuple(float(x) for x in probs),
            backend_name=self.name,
        )
