#!/usr/bin/env python3
"""
Why MFA is Non-Negotiable
=========================
Your password alone is like leaving your front door unlocked. Hackers can steal it in seconds. But with MFA, even if they get your password, they can't get in without that second factor - your phone, 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 23:17:37
"""

import pyotp
import hashlib
import time

class MFABypassSimulator:
    """
    Demonstrates why MFA matters by showing how easy it is to crack passwords
    but impossible to bypass proper MFA without the second factor.
    """
    
    def __init__(self, secret_key=None):
        """Initialize with a secret key for TOTP"""
        self.secret_key = secret_key or pyotp.random_base32()
        self.totp = pyotp.TOTP(self.secret_key)
        
    def crack_password(self, password_hash, wordlist):
        """Simulate password cracking from a leaked hash"""
        print("[*] Attempting password crack...")
        for word in wordlist:
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == password_hash:
                print(f"[!] Password cracked: {word}")
                return word
        print("[*] Password not found in wordlist")
        return None
    
    def verify_mfa(self, user_code):
        """Verify if the provided MFA code is valid"""
        current_code = self.totp.now()
        is_valid = self.totp.verify(user_code)
        
        if is_valid:
            print(f"[✓] MFA code {user_code} is VALID (matches: {current_code})")
        else:
            print(f"[✗] MFA code {user_code} is INVALID (current: {current_code})")
        return is_valid

# Example usage
if __name__ == "__main__":
    # Simulate an attack scenario
    mfa_sim = MFABypassSimulator()
    
    # Attacker gets leaked password hash
    leaked_hash = hashlib.sha256("Summer2024!".encode()).hexdigest()
    common_passwords = ["password123", "admin", "Summer2024!", "qwerty"]
    
    # They can crack the password easily
    cracked_pw = mfa_sim.crack_password(leaked_hash, common_passwords)
    
    # But without MFA code, they're stuck
    print("
[*] Attacker has password but needs MFA...")
    print("[*] Trying random codes:")
    
    # Try some random codes (will fail)
    for _ in range(3):
        fake_code = str(123456 + _).zfill(6)
        mfa_sim.verify_mfa(fake_code)
    
    print("
[!] Without MFA code, account remains secure!")
    print("[!] This is why MFA matters: password alone ≠ access")
