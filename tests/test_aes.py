import unittest
from encryption.aes import aes_encrypt, aes_decrypt

class TestAES(unittest.TestCase):
    def test_aes_encryption(self):
        key = b'secure_key_16_byt'
        aes_encrypt("data/sample.txt", key)
        aes_decrypt("data/encrypted_file.bin", key, "data/decrypted_sample.txt")
        with open("data/sample.txt", "rb") as original, open("data/decrypted_sample.txt", "rb") as decrypted:
            self.assertEqual(original.read(), decrypted.read())

if __name__ == "__main__":
    unittest.main()