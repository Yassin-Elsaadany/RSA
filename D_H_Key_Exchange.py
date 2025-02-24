#!/usr/bin/env python3
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

# Generate Diffie-Hellman parameters (2048 bits)
parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

# Generate private key and public key for Party A
private_key_a = parameters.generate_private_key()
public_key_a = private_key_a.public_key()

# Generate private key and public key for Party B
private_key_b = parameters.generate_private_key()
public_key_b = private_key_b.public_key()

# Compute the shared secret for Party A using Party B's public key
shared_secret_a = private_key_a.exchange(public_key_b)

# Compute the shared secret for Party B using Party A's public key
shared_secret_b = private_key_b.exchange(public_key_a)

# Ensure both parties have the same shared secret
assert shared_secret_a == shared_secret_b
print("Shared secret computed successfully.")

# Derive a symmetric key from the shared secret using PBKDF2
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
symmetric_key = kdf.derive(shared_secret_a)

# Print the shared symmetric key
print("Shared symmetric key:", symmetric_key.hex())
