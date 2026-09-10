from quantum_crypto_lab import factor_integer


def test_factor_small_composites_quantum_path():
    expected = {15: (3, 5), 21: (3, 7), 35: (5, 7)}
    for n, factors in expected.items():
        result = factor_integer(n, shots=2048, seed=7)
        assert result.success
        assert result.factors == factors
        assert any(a.route == "quantum-order-finding" for a in result.attempts)


def test_even_precheck():
    result = factor_integer(14)
    assert result.factors == (2, 7)


def test_two_is_prime_not_a_factorization():
    result = factor_integer(2)
    assert not result.success
    assert result.factors is None


def test_prime_reports_no_factorization():
    result = factor_integer(13)
    assert not result.success
    assert result.factors is None
