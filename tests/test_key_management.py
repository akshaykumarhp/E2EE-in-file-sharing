import unittest
from encryption.key_management import KeyManager

class TestKeyManagement(unittest.TestCase):
    def setUp(self):
        self.key_manager = KeyManager()
        self.key_manager.generate_user_keys("user1")
        self.key_manager.generate_user_keys("user2")

    def test_generate_user_keys(self):
        public_key, private_key = self.key_manager.generate_user_keys("user3")
        self.assertIsNotNone(public_key)
        self.assertIsNotNone(private_key)

    def test_get_public_key(self):
        public_key = self.key_manager.get_public_key("user1")
        self.assertIsNotNone(public_key)

    def test_encrypt_decrypt(self):
        data = b"Test message for encryption"
        encrypted_data = self.key_manager.encrypt_for_user("user1", data)
        decrypted_data = self.key_manager.decrypt_for_user("user1", encrypted_data)
        self.assertEqual(data, decrypted_data)

    def test_encrypt_with_invalid_user(self):
        with self.assertRaises(ValueError):
            self.key_manager.encrypt_for_user("unknown_user", b"Test data")

    def test_decrypt_with_invalid_user(self):
        with self.assertRaises(ValueError):
            self.key_manager.decrypt_for_user("unknown_user", b"Encrypted data")

if __name__ == "__main__":
    unittest.main()