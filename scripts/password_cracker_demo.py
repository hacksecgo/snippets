#!/usr/bin/env python3
"""
How Hackers Crack Passwords
===========================
Stop using 'password123'! In 30 seconds, I'll show you how hackers actually crack passwords. First, they use wordlists - dictionaries of common passwords. Then they try variations with numbers and sym

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 22:29:29
"""

import hashlib
import itertools
import string

class PasswordCracker:
    """Demonstrates basic password cracking techniques for educational purposes"""
    
    def __init__(self, target_hash, hash_type='sha256'):
        self.target_hash = target_hash
        self.hash_type = hash_type
        
    def dictionary_attack(self, wordlist_file):
        """Try passwords from a wordlist (most common first)"""
        try:
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    password = line.strip()
                    if self._hash_password(password) == self.target_hash:
                        return password
        except FileNotFoundError:
            print(f"[!] Wordlist {wordlist_file} not found")
        return None
    
    def brute_force_simple(self, max_length=4):
        """Brute force with lowercase letters only (SLOW for long passwords)"""
        chars = string.ascii_lowercase
        for length in range(1, max_length + 1):
            for attempt in itertools.product(chars, repeat=length):
                password = ''.join(attempt)
                if self._hash_password(password) == self.target_hash:
                    return password
        return None
    
    def _hash_password(self, password):
        """Hash the password using specified algorithm"""
        password_bytes = password.encode('utf-8')
        if self.hash_type == 'md5':
            return hashlib.md5(password_bytes).hexdigest()
        elif self.hash_type == 'sha1':
            return hashlib.sha1(password_bytes).hexdigest()
        else:  # sha256 default
            return hashlib.sha256(password_bytes).hexdigest()

# Example usage (educational only!)
if __name__ == "__main__":
    # Hash of 'secret123' using SHA256
    target = 'b7e23ec29af22b0b4e41da31e868d57226121c84e4bdbf4e3331a0955e95c4c5'
    
    cracker = PasswordCracker(target, 'sha256')
    
    # Try dictionary attack first (most realistic)
    print("[*] Starting dictionary attack...")
    found = cracker.dictionary_attack('common_passwords.txt')
    
    if found:
        print(f"[+] Password found: {found}")
    else:
        print("[-] Password not in wordlist")
        
    # Shows why complex passwords matter:
    # 'secret123' cracks instantly, 'Xk8!qL3$zP9w' would take centuries
