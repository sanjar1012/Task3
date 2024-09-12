import hmac
import hashlib

class HMACCalculator:
    @staticmethod
    def calculate_hmac(key, message):
        
        if isinstance(key, str):
            key = key.encode()
        if isinstance(message, str):
            message = message.encode()
        
        hmac_obj = hmac.new(key, message, hashlib.sha256)
        return hmac_obj.digest()
