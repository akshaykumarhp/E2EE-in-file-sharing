import time
from encryption.rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt
from encryption.aes import aes_encrypt, aes_decrypt
from encryption.integrity import calculate_hash, verify_hash
from ai.risk_detection import predict_risk
import os

def measure_throughput(file_size, time_taken):
    throughput = (file_size / (1024 * 1024)) / time_taken  # Convert bytes to MB
    return throughput

def main():
    print("### Starting End-to-End Encryption (E2EE) Demo with Performance Metrics ###\n")

    metrics = {}  # Dictionary to store metrics

    # Step 1: RSA Key Generation
    print("Step 1: Generating RSA Keys...")
    start_time = time.time()
    public_key, private_key = generate_rsa_keys()
    metrics['rsa_keygen_time'] = time.time() - start_time
    print(f"RSA Key Generation Time: {metrics['rsa_keygen_time']:.4f} seconds")
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}\n")

    # Step 2: AES File Encryption
    print("Step 2: Encrypting the file using AES...")
    symmetric_key = os.urandom(16)  # Dynamically generate a 16-byte (128-bit) key
    print(f"Generated Symmetric Key (AES): {symmetric_key.hex()} (in hexadecimal format)\n")

    start_time = time.time()
    aes_encrypt("data/sample.txt", symmetric_key)
    metrics['aes_encrypt_time'] = time.time() - start_time

    file_size = os.path.getsize("data/sample.txt")  # Get file size in bytes
    metrics['encryption_throughput'] = measure_throughput(file_size, metrics['aes_encrypt_time'])
    print(f"File successfully encrypted and saved as 'data/encrypted_file.bin'.")
    print(f"AES Encryption Time: {metrics['aes_encrypt_time']:.4f} seconds")
    print(f"AES Encryption Throughput: {metrics['encryption_throughput']:.2f} MB/s\n")

    # Step 3: Encrypting the AES Symmetric Key using RSA
    print("Step 3: Encrypting the AES Symmetric Key using RSA...")
    start_time = time.time()
    encrypted_key = rsa_encrypt(symmetric_key, public_key)
    metrics['rsa_encrypt_time'] = time.time() - start_time
    print(f"Encrypted Symmetric Key (RSA): {encrypted_key}")
    print(f"RSA Encryption Time: {metrics['rsa_encrypt_time']:.4f} seconds\n")

    # Step 4: Sharing the encrypted file and symmetric key...
    print("Step 4: Sharing the encrypted file and symmetric key...")
    print("- Encrypted File: 'data/encrypted_file.bin'")
    print("- Encrypted Symmetric Key: (shared securely with the recipient)\n")

    # Step 5: Decrypting the Symmetric Key using RSA
    print("Step 5: Decrypting the Symmetric Key using RSA...")
    start_time = time.time()
    decrypted_symmetric_key = rsa_decrypt(encrypted_key, private_key)
    metrics['rsa_decrypt_time'] = time.time() - start_time
    print(f"Decrypted Symmetric Key (AES): {decrypted_symmetric_key.hex()} (in hexadecimal format)")
    print(f"RSA Decryption Time: {metrics['rsa_decrypt_time']:.4f} seconds\n")

    # Step 6: Decrypting the File with AES
    print("Step 6: Decrypting the file using AES...")
    start_time = time.time()
    aes_decrypt("data/encrypted_file.bin", decrypted_symmetric_key, "data/decrypted_sample.txt")
    metrics['aes_decrypt_time'] = time.time() - start_time

    metrics['decryption_throughput'] = measure_throughput(file_size, metrics['aes_decrypt_time'])
    print("File successfully decrypted and saved as 'data/decrypted_sample.txt'.")
    print(f"AES Decryption Time: {metrics['aes_decrypt_time']:.4f} seconds")
    print(f"AES Decryption Throughput: {metrics['decryption_throughput']:.2f} MB/s\n")

    # Step 7: File Integrity Verification
    print("Step 7: Verifying file integrity...")
    original_hash = calculate_hash("data/sample.txt")
    decrypted_hash = calculate_hash("data/decrypted_sample.txt")
    print(f"Original File Hash: {original_hash}")
    print(f"Decrypted File Hash: {decrypted_hash}")
    verify_hash(original_hash, decrypted_hash)
    print("Integrity check passed! The decrypted file matches the original.\n")

    # Step 8: Simulating AI-Based Risk Detection
    print("Step 8: Simulating AI-Based Risk Detection...")
    activity_data = {"failed_attempts": 3, "file_size_change": 0.0, "time": "2 AM"}
    risk_score = predict_risk(activity_data)
    metrics['risk_score'] = risk_score
    print(f"Simulated User Activity: {activity_data}")
    print(f"Calculated Risk Score: {risk_score}\n")

    print("### End-to-End Encryption (E2EE) Process Completed ###\n")

    # Print Final Metrics Summary
    print("### Performance Metrics Summary ###")
    print(f"RSA Key Generation Time: {metrics['rsa_keygen_time']:.4f} seconds")
    print(f"AES Encryption Time: {metrics['aes_encrypt_time']:.4f} seconds")
    print(f"AES Encryption Throughput: {metrics['encryption_throughput']:.2f} MB/s")
    print(f"RSA Encryption Time: {metrics['rsa_encrypt_time']:.4f} seconds")
    print(f"RSA Decryption Time: {metrics['rsa_decrypt_time']:.4f} seconds")
    print(f"AES Decryption Time: {metrics['aes_decrypt_time']:.4f} seconds")
    print(f"AES Decryption Throughput: {metrics['decryption_throughput']:.2f} MB/s")
    print(f"Risk Detection Score: {metrics['risk_score']}")

if __name__ == "__main__":
    main()