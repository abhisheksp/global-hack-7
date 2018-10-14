from cryptography.fernet import Fernet

cipher_key = ''
with open('cipher_key.txt') as f:
    cipher_key = bytes(f.readline(), 'utf-8')

cipher_suite = Fernet(cipher_key)


def cipher():
    return cipher_suite
