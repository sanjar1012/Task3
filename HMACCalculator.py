import hmac
import hashlib

class HMACCalculator:
    @staticmethod
    def calculate_hmac(key, message):
        return hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
