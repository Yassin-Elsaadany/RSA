# How to Run the RSA Encryption System

## 1. Setup
- Ensure you have **Python** installed on your system.
- Install the required cryptographic libraries (if needed) by running:

  ```bash
  pip install pycryptodome
  ```

## 2. Setting Up Virtual Environment (venv)
- It is recommended to use a virtual environment for dependency management.
- Create a virtual environment by running:

  ```bash
  python -m venv venv
  ```
- Activate the virtual environment:
  - On **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - On **Mac/Linux**:
    ```bash
    source venv/bin/activate
    ```

- Install the required dependencies within the virtual environment:
  ```bash
  pip install pycryptodome
  ```

## 3. Key Generation
- Run the **Key_Generation.py** script to generate RSA key pairs:

  ```bash
  python Key_Generation.py
  ```

- This will create:
  - `sender_private.key` & `sender_public.key`
  - `receiver_private.key` & `receiver_public.key`

## 4. Encryption Process
- Place your plaintext file in the directory (e.g., `plaintext.txt`).
- Encrypt the file using **RSA_Encryption.py**:

  ```bash
  python RSA_Encryption.py
  ```

- The script will generate `encrypted_data.txt`, containing the encrypted content.

## 5. Decryption Process
- To decrypt the encrypted file, run:

  ```bash
  python RSA_Decryption.py
  ```

- This will generate `decrypted_data.txt` containing the original plaintext.

## 6. Optional: Key Exchange
- If you are using **Diffie-Hellman Key Exchange**, you can run:

  ```bash
  python D_H_Key_Exchange.py
  ```

- This helps securely exchange encryption keys between sender and receiver.

---

