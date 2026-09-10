"""Backend contract for provider-neutral order-finding simulations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class OrderFindingResult:
    a: int
    n: int
    counting_qubits: int
    shots: int
    counts: dict[int, int]
    probabilities: tuple[float, ...]
    backend_name: str

    @property
    def q(self) -> int:
        return 1 << self.counting_qubits


class OrderFindingBackend(Protocol):
    name: str

    def run_order_finding(
        self,
        a: int,
        n: int,
        *,
        counting_qubits: int | None = None,
        shots: int = 4096,
        seed: int | None = 7,
    ) -> OrderFindingResult:
        raise NotImplementedError
