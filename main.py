from encryption.rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt
from encryption.aes import aes_encrypt, aes_decrypt
from encryption.integrity import calculate_hash, verify_hash
from ai.risk_detection import predict_risk
import os

def main():
    print("### Starting End-to-End Encryption (E2EE) Demo ###\n")

    # Step 1: RSA Key Generation
    print("Step 1: Generating RSA Keys...")
    public_key, private_key = generate_rsa_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}\n")

    # Step 2: File Encryption with AES
    print("Step 2: Encrypting the file using AES...")
    symmetric_key = os.urandom(16)  # Dynamically generate a 16-byte (128-bit) key
    print(f"Generated Symmetric Key (AES): {symmetric_key.hex()} (in hexadecimal format)\n")
    aes_encrypt("data/sample.txt", symmetric_key)
    print("File successfully encrypted and saved as 'data/encrypted_file.bin'.\n")

    # Step 3: Encrypting the Symmetric Key with RSA
    print("Step 3: Encrypting the AES Symmetric Key using RSA...")
    encrypted_key = rsa_encrypt(symmetric_key, public_key)
    print(f"Encrypted Symmetric Key (RSA): {encrypted_key}\n")
    print("The encrypted symmetric key is now ready for secure sharing.\n")

    # Step 4: Sharing the Encrypted Symmetric Key and File
    print("Step 4: Sharing the encrypted file and symmetric key...")
    print("Simulating file and key sharing...")
    print("- Encrypted File: 'data/encrypted_file.bin'")
    print("- Encrypted Symmetric Key: (shared securely with the recipient)\n")

    # Step 5: Decrypting the Symmetric Key with RSA
    print("Step 5: Decrypting the Symmetric Key using RSA...")
    decrypted_symmetric_key = rsa_decrypt(encrypted_key, private_key)
    print(f"Decrypted Symmetric Key (AES): {decrypted_symmetric_key.hex()} (in hexadecimal format)\n")
    print("The symmetric key has been securely decrypted by the recipient.\n")

    # Step 6: Decrypting the File with AES
    print("Step 6: Decrypting the file using AES...")
    aes_decrypt("data/encrypted_file.bin", decrypted_symmetric_key, "data/decrypted_sample.txt")
    print("File successfully decrypted and saved as 'data/decrypted_sample.txt'.\n")

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
    print(f"Simulated User Activity: {activity_data}")
    print(f"Calculated Risk Score: {risk_score}\n")

    print("### End-to-End Encryption (E2EE) Process Completed Successfully ###")

if __name__ == "__main__":
    main()