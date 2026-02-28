#!/usr/bin/env python3
"""
Subdomain Enumeration for Beginners
===================================
Want to start bug bounty hunting but don't know where to begin? Start with subdomain enumeration! It's how you find hidden attack surfaces. Most beginners miss this crucial recon step. Use tools like 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 16:35:39
"""

import requests
import json
from typing import List

class SubdomainFinder:
    """
    Find subdomains using certificate transparency logs
    Real-world technique used in bug bounty reconnaissance
    """
    
    def __init__(self):
        self.ct_log_apis = [
            "https://crt.sh/",
            "https://api.certspotter.com/v1/issuances"
        ]
    
    def find_from_crtsh(self, domain: str) -> List[str]:
        """Query crt.sh certificate transparency logs"""
        subdomains = set()
        
        try:
            # crt.sh API endpoint
            url = f"https://crt.sh/json?q=%.{domain}&output=json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                certificates = json.loads(response.text)
                
                for cert in certificates:
                    # Extract common name and SANs
                    common_name = cert.get('common_name', '')
                    if common_name and domain in common_name:
                        subdomains.add(common_name)
                    
                    # Check Subject Alternative Names
                    san_field = cert.get('name_value', '')
                    if san_field:
                        for name in san_field.split('
'):
                            if domain in name:
                                subdomains.add(name.strip())
                
        except Exception as e:
            print(f"[!] Error querying crt.sh: {e}")
        
        return sorted(list(subdomains))
    
    def enumerate(self, domain: str) -> List[str]:
        """Main enumeration method"""
        print(f"[+] Enumerating subdomains for: {domain}")
        subdomains = self.find_from_crtsh(domain)
        
        print(f"[+] Found {len(subdomains)} unique subdomains")
        for sub in subdomains[:10]:  # Show first 10
            print(f"  - {sub}")
        
        return subdomains

# Example usage (for authorized testing only!)
if __name__ == "__main__":
    # ALWAYS test only domains you own or have permission to test
    finder = SubdomainFinder()
    
    # Example: Test with example.com (public domain)
    results = finder.enumerate("example.com")
    
    # Save results for further testing
    with open("subdomains.txt", "w") as f:
        for sub in results:
            f.write(f"{sub}
")
