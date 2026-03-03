#!/usr/bin/env python3
"""
XSS Attacks Explained
=====================
Ever wonder how hackers steal your cookies? It's called XSS - Cross-Site Scripting. Here's how it works: Attackers inject malicious JavaScript into vulnerable websites. When you visit that page, your 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 17:15:00
"""

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class XSSDetector:
    """
    A simple XSS vulnerability scanner that tests for reflected XSS.
    """
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (XSS-Scanner)'})
        
        # Common XSS payloads for testing
        self.payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "\" onmouseover=\"alert('XSS')\"",
            "javascript:alert('XSS')"
        ]
    
    def scan_form(self, form):
        """Test a single form for XSS vulnerabilities."""
        action = form.get('action', '')
        method = form.get('method', 'get').lower()
        form_url = urljoin(self.target_url, action)
        
        inputs = form.find_all('input')
        params = {}
        
        for inp in inputs:
            name = inp.get('name')
            if name:
                params[name] = 'test_value'  # Default value
        
        vulnerabilities = []
        
        for payload in self.payloads:
            test_params = params.copy()
            # Inject payload into first parameter
            if test_params:
                first_key = list(test_params.keys())[0]
                test_params[first_key] = payload
                
                try:
                    if method == 'post':
                        response = self.session.post(form_url, data=test_params, timeout=5)
                    else:
                        response = self.session.get(form_url, params=test_params, timeout=5)
                    
                    # Check if payload is reflected in response
                    if payload in response.text:
                        vulnerabilities.append({
                            'form_url': form_url,
                            'parameter': first_key,
                            'payload': payload,
                            'method': method.upper()
                        })
                except requests.RequestException as e:
                    print(f"Error testing {form_url}: {e}")
        
        return vulnerabilities
    
    def run_scan(self):
        """Main scanning function."""
        try:
            response = self.session.get(self.target_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            
            print(f"Found {len(forms)} forms on {self.target_url}")
            
            all_vulns = []
            for form in forms:
                vulns = self.scan_form(form)
                all_vulns.extend(vulns)
                
            return all_vulns
            
        except Exception as e:
            print(f"Scan failed: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # TEST ONLY ON SITES YOU OWN OR HAVE PERMISSION TO TEST
    scanner = XSSDetector("http://testphp.vulnweb.com/")  # Demo site
    vulnerabilities = scanner.run_scan()
    
    if vulnerabilities:
        print("
[!] Potential XSS vulnerabilities found:")
        for vuln in vulnerabilities:
            print(f"  - Parameter '{vuln['parameter']}' in {vuln['method']} request to {vuln['form_url']}")
    else:
        print("
[+] No reflected XSS vulnerabilities detected.")
