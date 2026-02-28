#!/usr/bin/env python3
"""
Why MFA Beats Passwords Alone
=============================
Your password alone is like leaving your front door unlocked. Hackers can steal it from breaches or phishing. Multi-factor authentication adds a second lock they can't pick. It requires something you 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 16:36:52
"""

import hashlib
import time
from collections import defaultdict

class PasswordSpraySimulator:
    """
    Simulates a password spray attack against a single account.
    Shows how MFA would stop this attack even with correct credentials.
    """
    
    def __init__(self, username, common_passwords_file='rockyou.txt'):
        self.username = username
        self.common_passwords_file = common_passwords_file
        self.failed_attempts = defaultdict(int)
        self.lockout_threshold = 5
        
    def load_common_passwords(self, limit=100):
        """Load top N passwords from common wordlist"""
        try:
            with open(self.common_passwords_file, 'r', encoding='utf-8', errors='ignore') as f:
                return [line.strip() for line in f.readlines()[:limit]]
        except FileNotFoundError:
            # Fallback to built-in common passwords
            return ['password123', '123456', 'qwerty', 'letmein', 'welcome']
    
    def simulate_login(self, password, has_mfa=False):
        """Simulate login attempt with optional MFA"""
        
        # Check if account is locked
        if self.failed_attempts[self.username] >= self.lockout_threshold:
            return "🔒 Account locked - too many failed attempts"
        
        # Simulate password check (in real scenario, this would be hashed)
        correct_password = "SecurePass2024!"
        
        if password != correct_password:
            self.failed_attempts[self.username] += 1
            return "❌ Invalid password"
        
        # Password is correct!
        if has_mfa:
            return "⚠️ Password correct, but MFA required! Attack blocked."
        else:
            return "✅ LOGIN SUCCESSFUL - No MFA enabled!"
    
    def run_spray_attack(self, has_mfa=False):
        """Run password spray simulation"""
        print(f"
🔓 Targeting: {self.username}")
        print(f"🔐 MFA Enabled: {has_mfa}
")
        
        passwords = self.load_common_passwords(10)
        passwords.append("SecurePass2024!")  # Add correct password
        
        for i, pwd in enumerate(passwords, 1):
            print(f"Attempt {i}: Trying '{pwd[:10]}...'", end=" ")
            result = self.simulate_login(pwd, has_mfa)
            print(result)
            time.sleep(0.1)  # Realistic delay
            
            if "SUCCESSFUL" in result:
                print("
💀 ACCOUNT COMPROMISED!")
                return True
                
        print("
✅ Attack unsuccessful")
        return False

# Example usage
if __name__ == "__main__":
    # Simulate attack WITHOUT MFA
    attacker = PasswordSpraySimulator("admin@company.com")
    attacker.run_spray_attack(has_mfa=False)
    
    print("
" + "="*50 + "
")
    
    # Simulate attack WITH MFA
    attacker2 = PasswordSpraySimulator("admin@company.com")
    attacker2.run_spray_attack(has_mfa=True)
