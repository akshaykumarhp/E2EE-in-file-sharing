from encryption.rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt
from encryption.aes import aes_encrypt, aes_decrypt
from encryption.integrity import calculate_hash, verify_hash
from ai.risk_detection import predict_risk
import os

def main():
    print("Starting E2EE File Sharing Demo...")

    # Key generation for RSA
    print("\nGenerating RSA Keys...")
    public_key, private_key = generate_rsa_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Encrypt the file
    print("\nEncrypting the file...")
    symmetric_key = os.urandom(16)  # Dynamically generate a 16-byte (128-bit) key
    aes_encrypt("data/sample.txt", symmetric_key)
    encrypted_key = rsa_encrypt(symmetric_key, public_key)
    print("File encrypted successfully!")

    # Decrypt the file
    print("\nDecrypting the file...")
    decrypted_symmetric_key = rsa_decrypt(encrypted_key, private_key)
    aes_decrypt("data/encrypted_file.bin", decrypted_symmetric_key, "data/decrypted_sample.txt")
    print("File decrypted successfully!")

    # Verify integrity
    print("\nVerifying file integrity...")
    original_hash = calculate_hash("data/sample.txt")
    decrypted_hash = calculate_hash("data/decrypted_sample.txt")
    verify_hash(original_hash, decrypted_hash)
    print("File integrity verified!")

    # AI-based risk prediction
    print("\nSimulating risk detection...")
    activity_data = {"failed_attempts": 3, "file_size_change": 0.1, "time": "2 AM"}
    risk_score = predict_risk(activity_data)
    print(f"Risk Score: {risk_score}")

if __name__ == "__main__":
    main()