#!/usr/bin/env python3
"""
Password Security Essentials
============================
Your passwords are probably terrible. Let's fix that. First, never reuse passwords across sites. One breach means they all fall. Second, use a password manager to generate and store unique, complex pa

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 10:23:06
"""

import hashlib
import requests
from typing import List

class PasswordChecker:
    """Check if passwords have been exposed in data breaches using Have I Been Pwned API"""
    
    def __init__(self):
        self.api_url = "https://api.pwnedpasswords.com/range/"
    
    def check_password(self, password: str) -> int:
        """
        Check password against known breaches
        Returns: number of times password appears in breaches
        """
        # Hash password using SHA-1 (required by HIBP API)
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        
        # Send first 5 chars to API (k-anonymity model)
        prefix, suffix = sha1_hash[:5], sha1_hash[5:]
        
        try:
            response = requests.get(f"{self.api_url}{prefix}", timeout=5)
            response.raise_for_status()
            
            # Parse response to find full hash matches
            hashes = (line.split(':') for line in response.text.splitlines())
            for hash_suffix, count in hashes:
                if hash_suffix == suffix:
                    return int(count)
            return 0
                    
        except requests.RequestException as e:
            print(f"Error checking password: {e}")
            return -1

# Example usage
def main():
    checker = PasswordChecker()
    
    # Test passwords (never use these in real life!)
    test_passwords = ["password123", "qwerty", "MySecurePassw0rd!"]
    
    for pwd in test_passwords:
        count = checker.check_password(pwd)
        if count > 0:
            print(f"⚠️  '{pwd}' found in {count:,} breaches!")
        elif count == 0:
            print(f"✅ '{pwd}' not found in known breaches")
        else:
            print(f"❌ Could not check '{pwd}'")

if __name__ == "__main__":
    main()
