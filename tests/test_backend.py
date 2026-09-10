import numpy as np

from quantum_crypto_lab.backends import NumpyStatevectorBackend


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
