#!/usr/bin/env python3
"""
OSINT Tool: TheHarvester
========================
Ever wonder what information about you is publicly available online? OSINT tools can show you exactly what's exposed. Today, let's look at theHarvester - one of the most powerful reconnaissance tools.

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 17:01:37
"""

#!/usr/bin/env python3
"""
Basic OSINT collector using theHarvester API
Educational example - always get proper authorization before scanning
"""

import subprocess
import json
import sys
from datetime import datetime

class OSINTCollector:
    def __init__(self, domain):
        self.domain = domain
        self.results = {}
        
    def run_theharvester(self, source='all', limit=100):
        """
        Execute theHarvester tool to collect OSINT data
        
        Args:
            source: Data source (google, bing, linkedin, etc.)
            limit: Number of results to collect
        """
        try:
            # Build theHarvester command
            cmd = [
                'theHarvester',
                '-d', self.domain,
                '-b', source,
                '-l', str(limit),
                '-f', f'report_{self.domain}'
            ]
            
            print(f"[+] Collecting OSINT for {self.domain} from {source}")
            
            # Execute command
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                self.parse_results(result.stdout)
                return True
            else:
                print(f"[-] Error: {result.stderr}")
                return False
                
        except FileNotFoundError:
            print("[-] theHarvester not found. Install with: pip install theHarvester")
            return False
        except subprocess.TimeoutExpired:
            print("[-] Scan timed out")
            return False
    
    def parse_results(self, output):
        """Parse theHarvester output for key information"""
        self.results['emails'] = []
        self.results['hosts'] = []
        
        for line in output.split('
'):
            if '@' in line and self.domain in line:
                email = line.strip()
                if email not in self.results['emails']:
                    self.results['emails'].append(email)
            elif self.domain in line and '://' not in line:
                host = line.strip()
                if host not in self.results['hosts']:
                    self.results['hosts'].append(host)
    
    def save_report(self):
        """Save findings to JSON report"""
        filename = f"osint_report_{self.domain}_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"[+] Report saved to {filename}")
        return filename

# Example usage
if __name__ == "__main__":
    # Always verify you have authorization before scanning
    target_domain = "example.com"  # Replace with authorized target
    
    collector = OSINTCollector(target_domain)
    
    # Run basic OSINT collection
    if collector.run_theharvester(source='google', limit=50):
        print(f"[+] Found {len(collector.results.get('emails', []))} emails")
        print(f"[+] Found {len(collector.results.get('hosts', []))} hosts")
        
        # Save results
        collector.save_report()
        
        # Display sample findings
        if collector.results['emails']:
            print("
Sample emails found:")
            for email in collector.results['emails'][:3]:
                print(f"  - {email}")
