#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import os

def generate_keys(public_key_file, private_key_file):
    # Generate RSA key pair (2048 bits)
    key = RSA.generate(2048)

    # Export the public key
    with open(public_key_file, 'wb') as pub_file:
        pub_file.write(key.publickey().export_key())

    # Export the private key (private key should be stored securely, not shared)
    with open(private_key_file, 'wb') as priv_file:
        priv_file.write(key.export_key())



# Generate keys for sender and receiver
generate_keys("sender_public.key", "sender_private.key")
generate_keys("receiver_public.key", "receiver_private.key")
