import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import envs


class ChiperUtils:
    def __init__(
        self,
        alghoritm: hashes.HashAlgorithm,
        enc_key: str,
        salt: str = envs.SALT_KEY.encode(),
        length: int = 32,
        iterations: int = 480000,
    ) -> None:
        self._kdf = PBKDF2HMAC(algorithm=alghoritm, length=length, salt=salt, iterations=iterations)
        self._key: bytes = base64.urlsafe_b64encode(self._kdf.derive(enc_key.encode()))
        self._fernet = Fernet(key=self._key)

    def encrypt(self, plaintext: str) -> str:
        return self._fernet.encrypt(data=plaintext.encode()).decode()

    def decrypt(self, enc_data: str) -> str:
        return self._fernet.decrypt(token=enc_data.encode()).decode()
