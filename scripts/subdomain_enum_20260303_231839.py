#!/usr/bin/env python3
"""
Subdomain Finder for Bug Bounties
=================================
Want to start bug bounty hunting but don't know where to begin? Start with subdomain enumeration! It's how you find hidden attack surfaces. Most programs reward for subdomain takeovers. Use tools like

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 23:18:38
"""

import requests
import re
from concurrent.futures import ThreadPoolExecutor

class SubdomainEnumerator:
    """Realistic subdomain enumeration using certificate transparency logs"""
    
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = set()
        
    def query_crtsh(self):
        """Query crt.sh certificate transparency database"""
        url = f"https://crt.sh/?q=%.{self.domain}&output=json"
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (BugBountyScanner/1.0)'}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                for entry in data:
                    # Extract subdomains from certificate names
                    name_value = entry.get('name_value', '')
                    domains = re.findall(r'([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', name_value)
                    
                    for domain in domains:
                        if domain.endswith(self.domain):
                            self.subdomains.add(domain.lower())
        except Exception as e:
            print(f"[!] Error querying crt.sh: {e}")
    
    def enumerate(self, max_workers=10):
        """Main enumeration method with threading"""
        print(f"[*] Enumerating subdomains for {self.domain}")
        
        # Query certificate transparency (real bug hunters use multiple sources)
        self.query_crtsh()
        
        # Additional sources would go here (SecurityTrails, VirusTotal, etc.)
        
        return sorted(self.subdomains)

# Example usage for bug bounty reconnaissance
if __name__ == "__main__":
    # ALWAYS: Replace with target you have permission to test
    target_domain = "example.com"
    
    enumerator = SubdomainEnumerator(target_domain)
    results = enumerator.enumerate()
    
    print(f"
[+] Found {len(results)} subdomains:")
    for subdomain in results:
        print(f"  - {subdomain}")
