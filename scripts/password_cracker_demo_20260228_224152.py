#!/usr/bin/env python3
"""
Why MFA Beats Passwords Every Time
==================================
Your password alone isn't enough anymore. Hackers can steal it in seconds. That's why multi-factor authentication matters. It adds a second layer - like a code on your phone - that hackers can't acces

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 22:41:52
"""

import hashlib
import time
from typing import Optional

class PasswordCracker:
    """Demonstrates why passwords alone are vulnerable"""
    
    def __init__(self, wordlist_path: str):
        self.wordlist = self._load_wordlist(wordlist_path)
    
    def _load_wordlist(self, path: str) -> list:
        """Load common passwords from file"""
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            return ['password123', 'admin', '123456', 'letmein', 'qwerty']
    
    def crack_hash(self, target_hash: str, salt: Optional[str] = None) -> Optional[str]:
        """Brute force attempt against hashed password"""
        print(f"[+] Starting attack on hash: {target_hash[:16]}...")
        start_time = time.time()
        
        for password in self.wordlist:
            # Simulate common hashing patterns
            test_string = salt + password if salt else password
            test_hash = hashlib.sha256(test_string.encode()).hexdigest()
            
            if test_hash == target_hash:
                elapsed = time.time() - start_time
                print(f"[!] CRACKED in {elapsed:.2f}s: '{password}'")
                print(f"[!] Without MFA, account is now COMPROMISED")
                return password
        
        print(f"[-] Failed after {len(self.wordlist)} attempts")
        print(f"[+] With MFA: Even with password, attacker needs your 2nd factor")
        return None

# Example usage
if __name__ == "__main__":
    # Simulate stolen password hash from a breach
    stolen_hash = hashlib.sha256(b'Summer2024!').hexdigest()
    
    cracker = PasswordCracker("common_passwords.txt")
    result = cracker.crack_hash(stolen_hash)
    
    if result:
        print(f"
⚠️  This is why MFA matters! Password alone: FAIL")
        print(f"✅ With MFA: Password + phone = SECURE")
