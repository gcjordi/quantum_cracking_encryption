import numpy as np

from quantum_crypto_lab.backends import ClassicalExactOrderBackend, NumpyStatevectorBackend


def test_probabilities_normalized():
    backend = NumpyStatevectorBackend()
    probs = backend.exact_probabilities(2, 15)
    assert np.isclose(probs.sum(), 1.0)
    assert len(probs) == 256


def test_n15_has_expected_qft_peaks():
    backend = NumpyStatevectorBackend()
    probs = backend.exact_probabilities(2, 15)
    for k in (0, 64, 128, 192):
        assert np.isclose(probs[k], 0.25)


def test_classical_backend_excludes_zero_count_measurements():
    backend = ClassicalExactOrderBackend()
    result = backend.run_order_finding(2, 15, shots=1)
    assert sum(result.counts.values()) == 1
    assert all(count > 0 for count in result.counts.values())
