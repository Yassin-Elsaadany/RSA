#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_file(input_file, output_file, private_key_file):
    # Load receiver's private key
    with open(private_key_file, 'rb') as priv_file:
        private_key = RSA.import_key(priv_file.read())

    cipher = PKCS1_OAEP.new(private_key)

    # Read the encrypted data
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write decrypted data to output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Decrypt the encrypted data using the receiver's private key
decrypt_file("encrypted_data.txt", "decrypted_data.txt", "receiver_private.key")
