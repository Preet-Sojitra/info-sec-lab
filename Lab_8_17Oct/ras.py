from math import gcd

p = int(input("Enter the prime number p: "))
q = int(input("Enter the prime number q: "))

# TODO: Can be extend to work for strings. But not interested :D
print("\nNOTE: THIS PROGRAM ONLY WORKS FOR NUMBERS")
plain_text = int(input("Enter the message to be encrypted: "))


def generate_n(p, q):
    return p * q


def totient_function(p, q):
    return (p - 1) * (q - 1)


def generate_e(p, q):
    phi_n = totient_function(p, q)

    # find e such that gcd(e, phi_n) = 1
    e = 2
    while e < phi_n:
        if gcd(e, phi_n) == 1:
            return e
        e += 1


def generate_private_key(e, phi_n):
    d = 2
    while d < phi_n:
        if (d * e) % phi_n == 1:
            return d
        d += 1


def generate_public_key(e, n):
    return e, n


def encrypt_message(message, p, q):
    n = generate_n(p, q)
    e = generate_e(p, q)
    phi_n = totient_function(p, q)

    public_key = generate_public_key(e, n)

    encrypted_message = message**e % n
    return encrypted_message, public_key, e


def decrypt_message(encrypted_message, p, q):
    e = generate_e(p, q)
    n = generate_n(p, q)
    phi_n = totient_function(p, q)
    private_key = generate_private_key(e, phi_n)
    decrypted_message = encrypted_message**private_key % n
    return decrypted_message, private_key  # private_key = (d, n)


encrypted_message, public_key, e = encrypt_message(plain_text, p, q)
decrypted_message, private_key = decrypt_message(encrypted_message, p, q)

print("Public key: ", public_key)
print("Private key: ", private_key)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)
