#!/usr/bin/env python3
"""
Why MFA is non-negotiable
=========================
Your password alone is like leaving your front door unlocked. Hackers can steal it in seconds. Multi-factor authentication adds that second lock they can't pick. Even if they get your password, they n

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 16:56:44
"""

import hashlib
import time
import itertools
import string

class PasswordCracker:
    """Demonstrates how easily passwords can be cracked without MFA"""
    
    def __init__(self, hash_type='sha256'):
        self.hash_type = hash_type
        self.common_passwords = ['password123', 'admin', 'letmein', '123456', 'qwerty']
    
    def hash_password(self, password):
        """Hash a password using specified algorithm"""
        if self.hash_type == 'sha256':
            return hashlib.sha256(password.encode()).hexdigest()
        elif self.hash_type == 'md5':
            return hashlib.md5(password.encode()).hexdigest()
    
    def brute_force_attack(self, target_hash, max_length=4):
        """Brute force attack on weak passwords"""
        chars = string.ascii_lowercase + string.digits
        start_time = time.time()
        
        for length in range(1, max_length + 1):
            for attempt in itertools.product(chars, repeat=length):
                password = ''.join(attempt)
                if self.hash_password(password) == target_hash:
                    elapsed = time.time() - start_time
                    return password, elapsed, True
        
        return None, time.time() - start_time, False
    
    def dictionary_attack(self, target_hash):
        """Try common passwords first"""
        start_time = time.time()
        
        for password in self.common_passwords:
            if self.hash_password(password) == target_hash:
                elapsed = time.time() - start_time
                return password, elapsed, True
        
        return None, time.time() - start_time, False

# Example usage
if __name__ == "__main__":
    cracker = PasswordCracker('sha256')
    
    # Hash a weak password
    weak_password = "abc123"
    target_hash = cracker.hash_password(weak_password)
    
    print(f"[+] Target hash: {target_hash}")
    print("[*] Starting dictionary attack...")
    
    result, time_taken, found = cracker.dictionary_attack(target_hash)
    
    if found:
        print(f"[!] CRACKED in {time_taken:.2f}s: {result}")
        print("[!] This is why you need MFA!")
    else:
        print("[*] Dictionary attack failed, trying brute force...")
        result, time_taken, found = cracker.brute_force_attack(target_hash, 6)
        if found:
            print(f"[!] BRUTE FORCED in {time_taken:.2f}s: {result}")
