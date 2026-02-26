#!/usr/bin/env python3
"""
Top 3 Recon Tools
=================
Your recon game is weak without these three tools. First, Nmap for network discovery - it's the industry standard. Second, Shodan - Google for internet-connected devices. Third, theHarvester for OSINT

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 04:12:20
"""

#!/usr/bin/env python3
"""
Basic Subdomain Enumeration Tool
Realistic recon script for bug bounty/pentesting
"""

import requests
import sys
from concurrent.futures import ThreadPoolExecutor

class SubdomainEnumerator:
    """Enumerate subdomains using common wordlist"""
    
    def __init__(self, domain, wordlist_path="common_subdomains.txt"):
        self.domain = domain
        self.wordlist_path = wordlist_path
        self.found_subdomains = []
        
    def load_wordlist(self):
        """Load subdomain wordlist from file"""
        try:
            with open(self.wordlist_path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            # Fallback to common subdomains if file not found
            return ['www', 'mail', 'ftp', 'admin', 'api', 'dev', 'test']
    
    def check_subdomain(self, subdomain):
        """Check if subdomain exists via HTTP request"""
        url = f"http://{subdomain}.{self.domain}"
        try:
            # Set timeout to avoid hanging on non-existent domains
            response = requests.get(url, timeout=3, allow_redirects=True)
            if response.status_code < 400:
                self.found_subdomains.append(url)
                print(f"[+] Found: {url} (Status: {response.status_code})")
        except requests.RequestException:
            # Silently fail on connection errors (common in recon)
            pass
    
    def enumerate(self, max_workers=10):
        """Run subdomain enumeration with threading"""
        wordlist = self.load_wordlist()
        print(f"[*] Enumerating subdomains for {self.domain}...")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(self.check_subdomain, wordlist)
        
        print(f"
[+] Found {len(self.found_subdomains)} subdomains")
        return self.found_subdomains

# Example usage (real pentesters would add more features)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <domain>")
        sys.exit(1)
        
    enumerator = SubdomainEnumerator(sys.argv[1])
    results = enumerator.enumerate()
