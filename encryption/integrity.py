import hashlib

def calculate_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def verify_hash(original_hash, decrypted_hash):
    if original_hash == decrypted_hash:
        print("Integrity check passed!")
    else:
        raise ValueError("Integrity check failed!")