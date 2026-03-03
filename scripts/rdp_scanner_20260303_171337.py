#!/usr/bin/env python3
"""
How Ransomware Spreads
======================
Ransomware doesn't just magically appear on your system. It needs a way in. Here are the top 3 infection vectors hackers use right now. First: Phishing emails with malicious attachments or links. Seco

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 17:13:36
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

class RDPVulnerabilityScanner:
    """
    Educational tool demonstrating how attackers scan for vulnerable RDP ports.
    RDP (port 3389) is a common ransomware entry point when left exposed.
    """
    
    def __init__(self, timeout=2):
        self.timeout = timeout
        self.common_ports = [3389, 3388, 3390]  # Common RDP ports
    
    def scan_port(self, target_ip, port):
        """Attempt to connect to a specific port on target IP"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((target_ip, port))
            sock.close()
            
            if result == 0:
                return (port, "OPEN - Potential RDP vulnerability!")
            else:
                return (port, "Closed")
        except Exception as e:
            return (port, f"Error: {str(e)}")
    
    def scan_target(self, target_ip):
        """Scan target for common RDP ports"""
        print(f"[+] Scanning {target_ip} for exposed RDP ports...
")
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.scan_port, target_ip, port) 
                      for port in self.common_ports]
            
            for future in futures:
                port, status = future.result()
                print(f"  Port {port}: {status}")
                
        print("
[!] Open RDP ports are prime targets for ransomware attacks!")
        print("[!] Always use VPNs and strong authentication for remote access.")

# Example usage (educational purposes only)
if __name__ == "__main__":
    scanner = RDPVulnerabilityScanner()
    
    # DEMO: Scan localhost for demonstration
    # In real attacks, hackers scan entire IP ranges
    print("DEMO: Simulating attacker scanning for vulnerable RDP ports")
    print("=" * 50)
    scanner.scan_target("127.0.0.1")
