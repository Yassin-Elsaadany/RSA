#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_file(input_file, output_file, public_key_file):
    try:
        # Load receiver's public key
        with open(public_key_file, 'rb') as pub_file:
            public_key = RSA.import_key(pub_file.read())

        cipher = PKCS1_OAEP.new(public_key)

        # Read input file (plaintext.txt)
        try:
            with open(input_file, 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' was not found.")
            return

        # Encrypt the data
        encrypted_data = cipher.encrypt(data)

        # Write encrypted data to output file
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)

        print(f"File '{input_file}' encrypted successfully. Output saved to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Encrypt the data using the receiver's public key
encrypt_file("plaintext.txt", "encrypted_data.txt", "receiver_public.key")
