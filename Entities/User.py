class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
