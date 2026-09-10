from quantum_crypto_lab import ShorSimulator, build_toy_keypair, decrypt_int, encrypt_int
from quantum_crypto_lab.rsa_demo import recover_private_key_from_factors


def test_toy_rsa_crack_roundtrip():
    key = build_toy_keypair(5, 7, 5)
    message = 12
    ciphertext = encrypt_int(message, key.public_key)
    result = ShorSimulator().factor(key.n, shots=2048)
    assert result.factors == (5, 7)
    recovered_private = recover_private_key_from_factors(key.public_key, *result.factors)
    assert decrypt_int(ciphertext, recovered_private) == message
