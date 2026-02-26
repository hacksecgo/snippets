#!/usr/bin/env python3
"""
Why Passwords Fail Without MFA
==============================
Your password alone is like leaving your front door unlocked. Hackers can steal it in seconds. But with multi-factor authentication, even if they get your password, they still need your phone or finge

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 04:10:45
"""

import hashlib
import time
from typing import Optional

class PasswordSpraySimulator:
    """Simulates credential stuffing attack against single-factor auth"""
    
    def __init__(self, target_hash: str):
        self.target_hash = target_hash  # Simulated stolen password hash
        self.common_passwords = [
            'password123', 'admin', '123456', 'qwerty', 'letmein',
            'welcome', 'monkey', 'dragon', 'baseball', 'football'
        ]
    
    def attempt_login(self, password: str) -> bool:
        """Check if password matches stolen hash"""
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return hashed == self.target_hash
    
    def spray_attack(self) -> Optional[str]:
        """Try common passwords against single factor auth"""
        print("[*] Starting credential spray attack...")
        
        for attempt, password in enumerate(self.common_passwords, 1):
            print(f"  [{attempt}] Trying: {password}")
            time.sleep(0.3)  # Simulate network delay
            
            if self.attempt_login(password):
                print(f"
[!] CRACKED: Password = '{password}'")
                print("[!] Single-factor auth breached!")
                return password
        
        print("
[*] Attack failed - but with MFA, even success wouldn't matter")
        return None

# Example usage
if __name__ == "__main__":
    # Simulate stolen password hash (in real breach, this comes from database dump)
    stolen_hash = hashlib.sha256("password123".encode()).hexdigest()
    
    attacker = PasswordSpraySimulator(stolen_hash)
    print("Simulating attack against single-factor authentication:
")
    print("Without MFA, stolen hash = instant account takeover
")
    
    result = attacker.spray_attack()
    if result:
        print(f"
\u274c Single factor failed: Attacker now has full access")
        print("\u2705 With MFA: Attacker still needs your phone/device")
