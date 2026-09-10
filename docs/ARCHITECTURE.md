# Architecture

## Design goal

v2.0 separates the mathematical workflow from the execution engine so the project is not tied to IBM or any other quantum provider.

## Layers

### `quantum_crypto_lab.shor`
Coordinates Shor's algorithm:

1. classical pre-checks;
2. choose a base `a`;
3. request an order-finding measurement distribution from a backend;
4. use continued fractions to recover candidate `r`;
5. validate `a^r mod N = 1`;
6. derive factors with `gcd(a^(r/2) ± 1, N)`.

### `quantum_crypto_lab.backends`
Defines the backend contract. The included `NumpyStatevectorBackend` is vendor-neutral.

### NumPy quantum simulation
The backend constructs the ideal entangled state

`(1/sqrt(Q)) Σ_x |x>|a^x mod N>`

which is exactly the state obtained after Hadamards plus reversible modular exponentiation in the ideal Shor order-finding circuit. It then applies the inverse QFT to the counting register using the mathematically equivalent unitary discrete Fourier transform implemented through NumPy FFT operations.

### Classical validation backend
`ClassicalExactOrderBackend` exists only for CI and conceptual comparisons. It is explicitly labelled non-quantum and is never the default.

## Extensibility

A future backend only needs to implement `run_order_finding(...) -> OrderFindingResult`. This permits adapters for Qiskit Aer, Cirq, Braket, Azure Quantum, hardware providers or custom simulators without changing the Shor orchestration layer.
