#!/usr/bin/env python3
"""
How Hackers Find Your Secrets
=============================
Ever wonder why even big companies get hacked? It's often one simple mistake: exposed secrets in their code. Developers accidentally commit API keys, passwords, or tokens to public GitHub repos. Hacke

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 17:09:48
"""

import re
import requests
import json

class GitHubSecretScanner:
    """Scans GitHub code for exposed secrets using regex patterns"""
    
    def __init__(self):
        # Common secret patterns - real hackers have much larger lists
        self.patterns = {
            'AWS_KEY': r'AKIA[0-9A-Z]{16}',
            'API_KEY': r'(?i)(api[_-]?key|secret)[\s]*[=:][\s]*["\']([a-zA-Z0-9]{32,})["\']',
            'JWT_TOKEN': r'eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}',
            'DATABASE_URL': r'(?i)(postgres|mysql|mongodb)://[a-zA-Z0-9_]+:[^@\s]+@',
        }
    
    def search_github(self, query, max_results=5):
        """Search GitHub code for potential secrets"""
        url = "https://api.github.com/search/code"
        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "per_page": max_results}
        
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                return response.json()['items']
            else:
                print(f"[!] API Error: {response.status_code}")
                return []
        except Exception as e:
            print(f"[!] Request failed: {e}")
            return []
    
    def analyze_file(self, content):
        """Check file content for secret patterns"""
        findings = []
        for secret_type, pattern in self.patterns.items():
            matches = re.findall(pattern, content)
            if matches:
                findings.append({
                    'type': secret_type,
                    'count': len(matches),
                    'sample': matches[0] if isinstance(matches[0], str) else matches[0][1]
                })
        return findings

# Example usage
if __name__ == "__main__":
    scanner = GitHubSecretScanner()
    
    # Search for config files that might contain secrets
    results = scanner.search_github("filename:.env password", max_results=3)
    
    print("[*] Scanning for exposed secrets...")
    for result in results:
        print(f"
[+] Found: {result['html_url']}")
        # In real tool, would fetch and analyze file content here
        print(f"   Potential config file with secrets")
    
    print("
⚠️  This is why companies need secret scanning tools!")
    print("   Always use .gitignore and environment variables!")
