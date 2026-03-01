#!/usr/bin/env python3
"""
How Hackers Exploit APIs
========================
Hackers don't always break in through the front door. They exploit APIs you didn't even know were exposed. Here's how: First, they scan for endpoints using tools like Burp Suite or custom scripts. The

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 16:49:18
"""

import requests
import json
import sys

class APIFuzzer:
    """
    Simple API endpoint fuzzer to discover hidden endpoints
    and test for common API vulnerabilities
    """
    
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
    def fuzz_endpoints(self, wordlist):
        """
        Test common API endpoint patterns
        """
        discovered = []
        
        with open(wordlist, 'r') as f:
            endpoints = [line.strip() for line in f]
        
        for endpoint in endpoints:
            # Test common HTTP methods
            for method in ['GET', 'POST', 'PUT', 'DELETE']:
                url = f"{self.base_url}/{endpoint}"
                
                try:
                    if method == 'GET':
                        resp = self.session.get(url, timeout=3)
                    elif method == 'POST':
                        resp = self.session.post(url, json={"test": "data"}, timeout=3)
                    else:
                        resp = self.session.request(method, url, timeout=3)
                    
                    # Check for interesting responses
                    if resp.status_code not in [404, 403, 400]:
                        print(f"[+] Found: {method} {url} - Status: {resp.status_code}")
                        
                        # Check for excessive data exposure
                        if resp.headers.get('Content-Type', '').startswith('application/json'):
                            try:
                                data = resp.json()
                                if isinstance(data, list) and len(data) > 100:
                                    print(f"   ⚠️  Potential data overexposure: {len(data)} records")
                            except:
                                pass
                        
                        discovered.append({"url": url, "method": method, "status": resp.status_code})
                        
                except requests.exceptions.RequestException:
                    continue
        
        return discovered

# Example usage
if __name__ == "__main__":
    # Educational purposes only - use only on systems you own
    fuzzer = APIFuzzer("http://testapi.local")
    # Common API endpoint wordlist
    endpoints = ["api", "v1", "users", "admin", "config", "backup", "debug"]
    
    with open("wordlist.txt", "w") as f:
        f.write('
'.join(endpoints))
        
    print("[*] Starting API endpoint fuzzing...")
    results = fuzzer.fuzz_endpoints("wordlist.txt")
    print(f"[*] Found {len(results)} potential endpoints")
