#!/usr/bin/env python3
"""
How Hackers Exploit APIs
========================
Your API keys are leaking right now. Hackers exploit insecure APIs by scanning for endpoints, testing authentication, and brute-forcing credentials. They use tools like this Python script to fuzz API 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 16:58:37
"""

import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

class APIFuzzer:
    """Realistic API endpoint fuzzer for security testing"""
    
    def __init__(self, base_url, wordlist_path):
        self.base_url = base_url.rstrip('/')
        self.wordlist = self._load_wordlist(wordlist_path)
        self.found_endpoints = []
    
    def _load_wordlist(self, path):
        """Load API endpoint wordlist from file"""
        try:
            with open(path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            return ['api', 'v1', 'users', 'admin', 'config', 'data']
    
    def test_endpoint(self, endpoint):
        """Test single endpoint with common HTTP methods"""
        url = f"{self.base_url}/{endpoint}"
        methods = ['GET', 'POST', 'PUT', 'DELETE']
        
        for method in methods:
            try:
                response = requests.request(method, url, timeout=3)
                if response.status_code < 400:  # Found accessible endpoint
                    self.found_endpoints.append({
                        'url': url,
                        'method': method,
                        'status': response.status_code
                    })
                    print(f"[+] Found: {method} {url} ({response.status_code})")
                    break
            except requests.RequestException:
                continue
    
    def fuzz(self, max_workers=10):
        """Fuzz all endpoints using thread pooling"""
        print(f"[*] Starting API fuzzing on {self.base_url}")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(self.test_endpoint, self.wordlist)
        
        print(f"
[*] Found {len(self.found_endpoints)} accessible endpoints")
        return self.found_endpoints

# Example usage
if __name__ == "__main__":
    # Target API and common endpoint wordlist
    fuzzer = APIFuzzer("https://target-api.com", "api_endpoints.txt")
    
    # Run the fuzzer (ethical use only!)
    results = fuzzer.fuzz()
    
    # Save results for further analysis
    with open('found_endpoints.json', 'w') as f:
        json.dump(results, f, indent=2)
