#!/usr/bin/env python3
"""
How Hackers Crack Passwords
===========================
Stop using 'password123'! In 30 seconds, I'll show you how attackers actually crack passwords. First, they use wordlists - common passwords from data breaches. Then they try variations with numbers an

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 22:51:33
"""

import hashlib
import itertools
import string
from datetime import datetime

class PasswordCracker:
    """Demonstrates common password cracking techniques"""
    
    def __init__(self, target_hash):
        self.target_hash = target_hash.lower()
        
    def dictionary_attack(self, wordlist):
        """Try common passwords from a wordlist"""
        print("[*] Starting dictionary attack...")
        for word in wordlist:
            # Hash the candidate password
            candidate_hash = hashlib.md5(word.encode()).hexdigest()
            if candidate_hash == self.target_hash:
                return word
        return None
    
    def brute_force(self, max_length=4):
        """Try all character combinations up to max_length"""
        print(f"[*] Starting brute force (up to {max_length} chars)...")
        chars = string.ascii_lowercase + string.digits
        
        for length in range(1, max_length + 1):
            for combo in itertools.product(chars, repeat=length):
                candidate = ''.join(combo)
                candidate_hash = hashlib.md5(candidate.encode()).hexdigest()
                if candidate_hash == self.target_hash:
                    return candidate
        return None

# Example usage
if __name__ == "__main__":
    # Hash of "pass123" (for demonstration only)
    TARGET_HASH = "32250170a0dca92d53ec9624f336ca24"
    
    cracker = PasswordCracker(TARGET_HASH)
    
    # Common passwords to try first
    common_passwords = ["password", "123456", "qwerty", "letmein", "pass123"]
    
    # Try dictionary attack
    result = cracker.dictionary_attack(common_passwords)
    if result:
        print(f"[+] Password found: {result}")
    else:
        # Fall back to brute force
        result = cracker.brute_force(max_length=6)
        if result:
            print(f"[+] Password found: {result}")
        else:
            print("[-] Password not found")
