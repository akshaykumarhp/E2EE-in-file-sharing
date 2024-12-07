# **End-to-End Encryption (E2EE) File Sharing**

This project demonstrates how to implement **End-to-End Encryption (E2EE)** for secure file sharing. It uses **RSA** for key exchange and **AES** for file encryption. The process also includes file integrity verification and AI-based risk detection.

---

## **Features**
- **RSA Key Exchange**: Encrypts the AES symmetric key securely for sharing.
- **AES File Encryption**: Encrypts file content efficiently with a symmetric key.
- **File Integrity Check**: Ensures the decrypted file matches the original.
- **AI-Based Risk Detection**: Evaluates the risk of suspicious user activity.

---

## **Requirements**
1. Python 3.7 or higher.
2. Libraries:
   - `pycryptodome` (for AES encryption).

---

## **Setup Instructions**
Follow these steps to set up and run the project.

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/e2ee-file-sharing.git
cd e2ee-file-sharing
```

### 2. **Install Dependencies**
Run the following command to install the required Python library:
```bash
pip install pycryptodome
```

### 3. **Prepare a Sample File**
- Place the file you want to encrypt in the `data/` folder.
- The file must be named `sample.txt`.

Example `sample.txt`:
```
This is a sample text file for testing End-to-End Encryption.
```

### 4. **Run the Program**
Execute the program using:
```bash
python main.py
```

---

## **How It Works**
The project follows these steps to demonstrate E2EE:

1. **RSA Key Generation**:
   - Generates a public-private key pair.
   - Public key is used for encrypting the AES symmetric key.
   - Private key is used for decrypting the AES symmetric key.

2. **AES File Encryption**:
   - Encrypts the content of `sample.txt` using AES encryption.
   - A symmetric key is dynamically generated for the encryption.

3. **Symmetric Key Encryption**:
   - The symmetric key is encrypted using RSA and shared securely with the recipient.

4. **File and Key Sharing**:
   - Simulates the sharing of the encrypted file and symmetric key over a network.

5. **Decryption**:
   - The recipient decrypts the symmetric key using their private RSA key.
   - The file is then decrypted using the symmetric key.

6. **File Integrity Check**:
   - Verifies that the decrypted file matches the original using SHA-256 hash comparison.

7. **AI-Based Risk Detection**:
   - Simulates user behavior (e.g., failed decryption attempts, unusual access times).
   - Evaluates the risk of suspicious activity.