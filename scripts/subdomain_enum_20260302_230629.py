#!/usr/bin/env python3
"""
Automate Subdomain Enumeration
==============================
Want to start bug bounty hunting but don't know where to begin? Here's your first tip: automate reconnaissance! Most beginners waste hours manually checking subdomains. Use Python to automate subdomai

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 23:06:28
"""

import requests
import concurrent.futures
from urllib.parse import urlparse

class SubdomainEnumerator:
    """Realistic subdomain enumeration tool for bug bounty reconnaissance"""
    
    def __init__(self, domain, wordlist_file="subdomains.txt"):
        self.domain = domain
        self.found_subdomains = []
        self.wordlist = self.load_wordlist(wordlist_file)
        
    def load_wordlist(self, filename):
        """Load subdomain wordlist from file"""
        try:
            with open(filename, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            # Common subdomains as fallback
            return ['www', 'mail', 'admin', 'api', 'dev', 'test', 'staging']
    
    def check_subdomain(self, subdomain):
        """Check if subdomain exists via HTTP request"""
        url = f"http://{subdomain}.{self.domain}"
        try:
            # Real pentesters use timeouts and proper headers
            headers = {'User-Agent': 'Mozilla/5.0 (BugBountyScanner/1.0)'}
            response = requests.get(url, headers=headers, timeout=3, allow_redirects=False)
            
            if response.status_code < 400:
                self.found_subdomains.append(url)
                print(f"[+] Found: {url} ({response.status_code})")
        except (requests.RequestException, KeyboardInterrupt):
            pass  # Silent fail for non-existent subdomains
    
    def enumerate(self, max_workers=50):
        """Multi-threaded enumeration for speed"""
        print(f"[*] Enumerating subdomains for {self.domain}")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all subdomain checks to thread pool
            futures = [executor.submit(self.check_subdomain, sub) for sub in self.wordlist]
            concurrent.futures.wait(futures)
        
        print(f"
[*] Found {len(self.found_subdomains)} subdomains")
        return self.found_subdomains

# Example usage (real pentesters would add argument parsing)
if __name__ == "__main__":
    # Always test against authorized targets only!
    target = "example.com"
    enumerator = SubdomainEnumerator(target)
    results = enumerator.enumerate()
