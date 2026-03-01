#!/usr/bin/env python3
"""
3 Must-Know OSINT Tools
=======================
Think you're invisible online? Think again. OSINT tools can find what you leave behind. First: Shodan - it's Google for devices. Find exposed webcams, servers, anything connected. Second: theHarvester

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 16:45:40
"""

#!/usr/bin/env python3
"""
Basic subdomain enumerator using multiple OSINT techniques
Educational example - real pentesters use this approach daily
"""

import requests
import dns.resolver
from concurrent.futures import ThreadPoolExecutor

class SubdomainEnumerator:
    """Enumerate subdomains using OSINT methods"""
    
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
        """Bruteforce common subdomains"""
        resolver = dns.resolver.Resolver()
        with open(wordlist, 'r') as f:
            words = [line.strip() for line in f]
        
        def check_subdomain(sub):
            try:
                resolver.resolve(f"{sub}.{self.domain}", 'A')
                return f"{sub}.{self.domain}"
            except:
                return None
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(check_subdomain, words)
            for result in results:
                if result:
                    self.subdomains.add(result)
    
    def run_enumeration(self, wordlist="common_subdomains.txt"):
        """Run all enumeration methods"""
        print(f"[*] Enumerating subdomains for {self.domain}")
        self.check_crt_sh()
        self.dns_bruteforce(wordlist)
        
        print(f"[+] Found {len(self.subdomains)} unique subdomains:")
        for sub in sorted(self.subdomains):
            print(f"  - {sub}")
        return list(self.subdomains)

# Example usage (pentester would run this)
if __name__ == "__main__":
    enumerator = SubdomainEnumerator("example.com")
    # In real pentest, use comprehensive wordlist
    subdomains = enumerator.run_enumeration()
