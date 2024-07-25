import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
from decouple import config
import binascii
from argon2 import PasswordHasher, profiles

from core.exceptions import DecryptionError

key = config('SECRET_KEY')
aesgcm = AESGCM(bytes.fromhex(key))
ph: PasswordHasher = PasswordHasher.from_parameters(
    profiles.RFC_9106_HIGH_MEMORY)


def aesgcm_encrypt(data: bytes, aad: bytes):
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, aad)
    return binascii.hexlify(nonce).decode(), binascii.hexlify(ct).decode()


def aesgcm_decrypt(nonce: str, ct: str, aad: bytes):
    return aesgcm.decrypt(
        bytes.fromhex(nonce), bytes.fromhex(ct), aad).decode()


def hash_password(password: str):
    return ph.hash(password, salt=bytes.fromhex(config('SALT')))


def encrypt(text: str, password: str):
    nonce, enc = aesgcm_encrypt(
        text.encode(), hash_password(password).encode())
    return f"{nonce}:{enc}"


def decrypt(text: str, password: str):
    nonce, enc = text.split(':')
    try:
        return aesgcm_decrypt(nonce, enc, hash_password(password).encode())
    except InvalidTag:
        raise DecryptionError
