from encryption.rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt

class KeyManager:
    def __init__(self):
        # Store keys in memory for demonstration purposes
        self.keys = {}  # Example: {"user1": (public_key, private_key)}

    def generate_user_keys(self, user_id):
        public_key, private_key = generate_rsa_keys()
        self.keys[user_id] = (public_key, private_key)
        return public_key, private_key

    def get_public_key(self, user_id):
        if user_id in self.keys:
            return self.keys[user_id][0]
        raise ValueError(f"Public key for user {user_id} not found.")

    def get_private_key(self, user_id):
        if user_id in self.keys:
            return self.keys[user_id][1]
        raise ValueError(f"Private key for user {user_id} not found.")

    def encrypt_for_user(self, user_id, data):
        public_key = self.get_public_key(user_id)
        return rsa_encrypt(data, public_key)

    def decrypt_for_user(self, user_id, encrypted_data):
        private_key = self.get_private_key(user_id)
        return rsa_decrypt(encrypted_data, private_key)