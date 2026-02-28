#!/usr/bin/env python3
"""
Social Engineering Attacks Explained
====================================
Hackers don't always break in - sometimes they just ask nicely. That's social engineering. Attackers manipulate human psychology to trick you into revealing passwords, clicking malicious links, or gra

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 16:32:12
"""

import requests
import re
from urllib.parse import urljoin

class OSINTGatherer:
    """
    Demonstrates how attackers gather Open Source Intelligence (OSINT)
    for social engineering attacks - finding employee emails/names
    """
    
    def __init__(self, target_domain):
        self.target_domain = target_domain
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    def find_employee_emails(self):
        """Search for email patterns on company website"""
        emails = set()
        try:
            # Common email pattern regex
            email_pattern = r'[a-zA-Z0-9._%+-]+@' + re.escape(self.target_domain)
            
            # Check main website
            response = self.session.get(f"https://{self.target_domain}", timeout=5)
            
            if response.status_code == 200:
                found_emails = re.findall(email_pattern, response.text)
                emails.update(found_emails)
                
                # Also check common paths for contact/team pages
                common_paths = ['/about', '/team', '/contact', '/staff']
                for path in common_paths:
                    try:
                        url = urljoin(f"https://{self.target_domain}", path)
                        resp = self.session.get(url, timeout=3)
                        if resp.status_code == 200:
                            more_emails = re.findall(email_pattern, resp.text)
                            emails.update(more_emails)
                    except:
                        continue
                        
        except Exception as e:
            print(f"Error: {e}")
        
        return list(emails)
    
    def generate_email_variants(self, first_name, last_name):
        """Generate common email formats for phishing"""
        variants = [
            f"{first_name}.{last_name}@{self.target_domain}",
            f"{first_name[0]}{last_name}@{self.target_domain}",
            f"{first_name}@{self.target_domain}",
            f"{last_name}.{first_name}@{self.target_domain}"
        ]
        return variants

# Example usage - how attackers prepare for spear phishing
if __name__ == "__main__":
    # Attacker researching a target company
    gatherer = OSINTGatherer("example-company.com")
    
    print("[*] Searching for employee emails...")
    emails = gatherer.find_employee_emails()
    
    if emails:
        print(f"[+] Found {len(emails)} emails:")
        for email in emails[:3]:  # Show first 3 for demo
            print(f"  - {email}")
    
    # Generate potential email addresses for targeted attacks
    print("
[*] Generating email variants for 'John Smith':")
    variants = gatherer.generate_email_variants("John", "Smith")
    for variant in variants:
        print(f"  - {variant}")
