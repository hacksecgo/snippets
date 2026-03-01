#!/usr/bin/env python3
"""
Why MFA is non-negotiable
=========================
Your password alone isn't enough anymore. Hackers can steal it in seconds. That's why you need MFA. It adds a second layer - like a code on your phone - so even if they get your password, they can't g

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 22:53:43
"""

import pyotp
import hashlib
import time
from cryptography.fernet import Fernet

class MFASimulator:
    """Simulates MFA token generation and validation for educational purposes"""
    
    def __init__(self, secret_key=None):
        # Generate or use provided secret for TOTP
        self.secret = secret_key or pyotp.random_base32()
        self.totp = pyotp.TOTP(self.secret, interval=30)
        
    def generate_token(self):
        """Generate current time-based OTP token"""
        return self.totp.now()
    
    def validate_token(self, user_token):
        """Validate if provided token matches current valid token"""
        # TOTP allows small time drift - verifies current and previous tokens
        return self.totp.verify(user_token, valid_window=1)
    
    def demonstrate_attack(self, stolen_password):
        """Show why password alone is insufficient"""
        print(f"[!] Attacker has password: {stolen_password}")
        print(f"[+] Without MFA token, access GRANTED: False")
        print(f"[+] With MFA token required, access GRANTED: False")
        return False

# Example usage
if __name__ == "__main__":
    # Simulate MFA setup
    mfa = MFASimulator()
    
    # Generate current token
    current_token = mfa.generate_token()
    print(f"[+] Current MFA token: {current_token}")
    
    # Validate correct token
    print(f"[+] Validating correct token: {mfa.validate_token(current_token)}")
    
    # Show attack scenario
    mfa.demonstrate_attack("P@ssw0rd123!")
    
    print(f"
[+] Secret key (keep secure!): {mfa.secret}")
