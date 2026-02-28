#!/usr/bin/env python3
"""
XSS Attacks Explained + Detector
================================
Ever wonder how hackers steal your cookies? It's often XSS - Cross-Site Scripting. Here's how it works: Attackers inject malicious JavaScript into websites you trust. When you visit the page, your bro

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 22:40:44
"""

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

class XSSDetector:
    """Simple XSS vulnerability scanner for educational purposes"""
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (XSS-Scanner)'})
        self.xss_payloads = [
            '<script>alert(1)</script>',
            '"><script>alert(1)</script>',
            'javascript:alert(1)',
            'onload=alert(1)',
            'onerror=alert(1)'
        ]
    
    def scan_form(self, form, url):
        """Test a single form for XSS vulnerabilities"""
        vulnerabilities = []
        
        # Get form details
        form_action = form.get('action', '')
        form_method = form.get('method', 'get').lower()
        form_url = urljoin(url, form_action)
        
        # Find all input fields
        inputs = form.find_all(['input', 'textarea'])
        input_data = {}
        
        for inp in inputs:
            name = inp.get('name')
            if name:
                input_data[name] = 'TEST_VALUE'
        
        # Test each payload
        for payload in self.xss_payloads:
            test_data = input_data.copy()
            for key in test_data:
                test_data[key] = payload
            
            try:
                if form_method == 'post':
                    response = self.session.post(form_url, data=test_data)
                else:
                    response = self.session.get(form_url, params=test_data)
                
                # Check if payload appears in response
                if payload in response.text:
                    vulnerabilities.append({
                        'url': form_url,
                        'payload': payload,
                        'method': form_method
                    })
            except Exception as e:
                continue
                
        return vulnerabilities
    
    def run_scan(self):
        """Main scanning function"""
        print(f"[+] Scanning {self.target_url} for XSS vulnerabilities...")
        
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            
            all_vulns = []
            for form in forms:
                vulns = self.scan_form(form, self.target_url)
                all_vulns.extend(vulns)
            
            return all_vulns
            
        except Exception as e:
            print(f"[-] Error: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # TEST ONLY ON SITES YOU OWN OR HAVE PERMISSION TO TEST
    scanner = XSSDetector("http://testphp.vulnweb.com/")
    vulnerabilities = scanner.run_scan()
    
    if vulnerabilities:
        print("[!] Potential XSS vulnerabilities found:")
        for vuln in vulnerabilities:
            print(f"  - URL: {vuln['url']}")
            print(f"    Payload: {vuln['payload']}")
            print(f"    Method: {vuln['method']}
")
    else:
        print("[+] No obvious XSS vulnerabilities detected")
    print("⚠️  Always get permission before testing websites!")

