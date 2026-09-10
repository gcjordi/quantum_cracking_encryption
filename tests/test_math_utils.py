from quantum_crypto_lab.math_utils import (
    multiplicative_order,
    nontrivial_factors_from_order,
    recover_order_from_measurement,
)


def test_known_orders():
    assert multiplicative_order(2, 15) == 4
    assert multiplicative_order(2, 21) == 6
    assert multiplicative_order(2, 35) == 12


def test_recover_order_from_qpe_peak():
    assert recover_order_from_measurement(128, 256, 2, 15) == 4


def test_factors_from_order():
    assert nontrivial_factors_from_order(2, 4, 15) == (3, 5)
    assert nontrivial_factors_from_order(2, 6, 21) == (3, 7)
