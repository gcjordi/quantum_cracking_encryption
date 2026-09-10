"""Dated research context for cryptographically relevant quantum factoring."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RSA2048Estimate:
    year: int
    description: str
    physical_qubits: str
    runtime: str
    source: str


RSA2048_ESTIMATES = (
    RSA2048Estimate(
        2019,
        "Gidney & Ekerå fault-tolerant resource estimate",
        "about 20 million noisy physical qubits",
        "about 8 hours",
        "https://arxiv.org/abs/1905.09749",
    ),
    RSA2048Estimate(
        2025,
        "Gidney revised estimate using newer arithmetic and error-correction techniques",
        "less than 1 million noisy physical qubits",
        "less than one week",
        "https://arxiv.org/abs/2505.15917",
    ),
)


def rsa2048_research_context() -> tuple[RSA2048Estimate, ...]:
    """Return published estimates; these are scenarios, not forecasts."""
    return RSA2048_ESTIMATES
