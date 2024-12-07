import unittest
from encryption.rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt

class TestRSA(unittest.TestCase):
    def test_rsa_encryption(self):
        public_key, private_key = generate_rsa_keys()
        data = b"Hello, RSA!"
        encrypted_data = rsa_encrypt(data, public_key)
        decrypted_data = rsa_decrypt(encrypted_data, private_key)
        self.assertEqual(data, decrypted_data)

if __name__ == "__main__":
    unittest.main()