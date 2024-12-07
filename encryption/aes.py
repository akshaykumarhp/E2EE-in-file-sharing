from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def aes_encrypt(input_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC)  # Create AES cipher in CBC mode
    ciphertext = cipher.encrypt(pad(data, AES.block_size))  # Pad and encrypt data

    with open("data/encrypted_file.bin", "wb") as ef:
        ef.write(cipher.iv + ciphertext)  # Prepend IV to ciphertext

def aes_decrypt(input_file, key, output_file):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Read the first 16 bytes (IV)
        ciphertext = f.read()  # Read the rest (ciphertext)
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Create AES cipher with the IV
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Decrypt and unpad data

    with open(output_file, 'wb') as df:
        df.write(plaintext)  # Save the decrypted plaintext