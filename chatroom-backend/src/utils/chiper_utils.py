import base64

from cryptography.fernet import Fernet


class ChiperUtils:
    def __init__(
        self,
        enc_key: str,
    ) -> None:
        self._key: bytes = base64.urlsafe_b64encode(enc_key.encode())
        self._fernet = Fernet(key=self._key)

    def encrypt(self, plaintext: str) -> str:
        return self._fernet.encrypt(data=plaintext.encode()).decode()

    def decrypt(self, enc_data: str) -> str:
        return self._fernet.decrypt(token=enc_data.encode()).decode()
