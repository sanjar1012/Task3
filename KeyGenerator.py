import secrets

class KeyGenerator:
    @staticmethod
    def generate_key():
        return secrets.token_bytes(32)  # 256 bits
