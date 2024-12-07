import random
from math import gcd

def generate_large_prime(bits=512):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def modular_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def generate_rsa_keys(bits=512):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = modular_inverse(e, phi)
    return (e, n), (d, n)

def rsa_encrypt(message, public_key):
    e, n = public_key
    # Convert to integer, whether message is string or bytes
    if isinstance(message, str):
        message_as_int = int.from_bytes(message.encode(), 'big')  # For string input
    elif isinstance(message, bytes):
        message_as_int = int.from_bytes(message, 'big')  # For bytes input
    else:
        raise TypeError("Message must be a string or bytes")
    # Encrypt the integer
    return pow(message_as_int, e, n)

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_as_int = pow(ciphertext, d, n)  # Decrypt the integer
    # Convert decrypted integer back to bytes
    return decrypted_as_int.to_bytes((decrypted_as_int.bit_length() + 7) // 8, 'big')