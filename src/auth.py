import hashlib
import hmac
import os

class AuthManager:
    """Mengelola autentikasi pengguna dengan hashing SHA-256 dan salt."""

    def __init__(self):
        self._users = {}

    def register_user(self, username: str, password: str) -> bool:
        if not username or not password or len(password) < 8:
            raise ValueError("Username tidak boleh kosong dan password minimal 8 karakter.")
        if username in self._users:
            return False

        salt = os.urandom(16).hex()
        password_hash = self._hash_password(password, salt)
        self._users[username] = {"salt": salt, "hash": password_hash}
        return True

    def verify_user(self, username: str, password: str) -> bool:
        user_record = self._users.get(username)
        if not user_record:
            return False
        expected_hash = user_record["hash"]
        calculated_hash = self._hash_password(password, user_record["salt"])
        return hmac.compare_digest(expected_hash, calculated_hash)

    @staticmethod
    def _hash_password(password: str, salt: str) -> str:
        salted = f"{salt}:{password}".encode("utf-8")
        return hashlib.sha256(salted).hexdigest()