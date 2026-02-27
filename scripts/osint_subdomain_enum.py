#!/usr/bin/env python3
"""
3 Essential OSINT Tools
=======================
Think you're invisible online? Think again. OSINT tools can find what you thought was hidden. First: Shodan - it's Google for internet-connected devices. Find cameras, servers, even traffic lights. Se

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 21:31:22
"""

#!/usr/bin/env python3
"""
Basic subdomain enumerator using multiple OSINT techniques
Educational example - use responsibly and with proper authorization
"""

import requests
import dns.resolver
from concurrent.futures import ThreadPoolExecutor

class SubdomainEnumerator:
    """A simple subdomain discovery tool using OSINT methods"""
    
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = set()
        
    def check_crt_sh(self):
        """Query crt.sh certificate transparency logs"""
        try:
            url = f"https://crt.sh/?q=%.{self.domain}&output=json"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                for cert in response.json():
                    name = cert['name_value'].lower()
                    if self.domain in name:
                        self.subdomains.add(name.split('
')[0])
        except Exception as e:
            print(f"[!] crt.sh query failed: {e}")
    
    def dns_bruteforce(self, wordlist):
        """Brute force common subdomains using DNS resolution"""
        resolver = dns.resolver.Resolver()
        with open(wordlist, 'r') as f:
            words = [line.strip() for line in f]
        
        def check_subdomain(sub):
            try:
                full_domain = f"{sub}.{self.domain}"
                resolver.resolve(full_domain, 'A')
                return full_domain
            except:
                return None
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(check_subdomain, words)
            for result in results:
                if result:
                    self.subdomains.add(result)
    
    def run_enumeration(self, wordlist=None):
        """Execute all enumeration methods"""
        print(f"[*] Enumerating subdomains for {self.domain}")
        self.check_crt_sh()
        if wordlist:
            self.dns_bruteforce(wordlist)
        
        print(f"[+] Found {len(self.subdomains)} unique subdomains:")
        for sub in sorted(self.subdomains):
            print(f"  - {sub}")
        return list(self.subdomains)

# Example usage
if __name__ == "__main__":
    # Educational purposes only - always get proper authorization
    enumerator = SubdomainEnumerator("example.com")
    # Use a small wordlist for demonstration
    subdomains = enumerator.run_enumeration("common_subdomains.txt")
