#!/usr/bin/env python3
"""
Social Engineering Explained
============================
Hackers don't always break systems—they break people. Social engineering manipulates human psychology, not code. Phishing emails, fake tech support, tailgating into buildings—all exploit trust. Attack

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 23:20:12
"""

import requests
import json
import time
from typing import Dict, List

class SocialEngineeringRecon:
    """OSINT tool for gathering information for targeted social engineering attacks"""
    
    def __init__(self, target_company: str):
        self.target_company = target_company
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
    def find_employees_linkedin(self) -> List[Dict]:
        """Simulate LinkedIn employee search (educational example)"""
        # In real attacks, attackers use LinkedIn API or scrape profiles
        print(f"[+] Searching for {self.target_company} employees on professional networks...")
        
        # Simulated data - real attackers would use actual LinkedIn scraping
        employees = [
            {"name": "John Smith", "title": "IT Manager", "email_pattern": "john.smith@company.com"},
            {"name": "Sarah Johnson", "title": "HR Director", "email_pattern": "sarah.j@company.com"},
            {"name": "Mike Chen", "title": "Finance Assistant", "email_pattern": "mike.chen@company.com"}
        ]
        
        print(f"[+] Found {len(employees)} potential targets")
        for emp in employees:
            print(f"  - {emp['name']} ({emp['title']})")
        return employees
    
    def generate_phishing_email(self, employee: Dict) -> str:
        """Create targeted phishing email based on employee role"""
        if "IT" in employee["title"]:
            subject = "URGENT: Security Patch Required"
            body = f"Hi {employee['name'].split()[0]}, we need you to apply critical security updates immediately."
        elif "HR" in employee["title"]:
            subject = "Important: Employee Benefits Update"
            body = f"Dear {employee['name']}, please review the attached benefits document."
        else:
            subject = "Action Required: Invoice Processing"
            body = f"Hello, please process the attached invoice for payment."
            
        email = f"From: 'IT Support' <support@{self.target_company.lower().replace(' ', '')}.com>
"
        email += f"To: {employee['email_pattern']}
"
        email += f"Subject: {subject}

"
        email += f"{body}

"
        email += "Click here to review: http://malicious-link.com/secure-doc"
        
        return email

# Example usage
if __name__ == "__main__":
    # Educational demonstration only - for authorized testing
    recon = SocialEngineeringRecon("TechCorp Inc")
    targets = recon.find_employees_linkedin()
    
    print("
[+] Generating targeted phishing email for first employee:")
    phishing_email = recon.generate_phishing_email(targets[0])
    print("
" + phishing_email)
    print("
⚠️  This demonstrates how attackers personalize social engineering attacks!")
