#!/usr/bin/env python3
"""
Pen Testing Explained in 30 Sec
===============================
Ever wonder how hackers find vulnerabilities before the bad guys do? That's penetration testing! It's authorized simulated cyber attacks to find security weaknesses. Think of it like a fire drill for 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 22:50:23
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor
import ipaddress

class SimplePortScanner:
    """A basic TCP port scanner for educational pentesting"""
    
    def __init__(self, target, timeout=1.0, max_workers=50):
        """Initialize scanner with target IP/hostname"""
        self.target = target
        self.timeout = timeout
        self.max_workers = max_workers
        self.open_ports = []
    
    def scan_port(self, port):
        """Attempt TCP connection to specific port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                self.open_ports.append(port)
                print(f"[+] Port {port}: OPEN")
            sock.close()
        except Exception as e:
            pass  # Silent fail for demo
    
    def scan_range(self, start_port=1, end_port=1024):
        """Scan a range of ports using thread pooling"""
        print(f"Scanning {self.target} (ports {start_port}-{end_port})")
        ports = range(start_port, end_port + 1)
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.scan_port, ports)
        
        print(f"
Scan complete! Found {len(self.open_ports)} open ports.")
        return self.open_ports

# Example usage (for authorized testing only!)
if __name__ == "__main__":
    # ALWAYS get permission before scanning!
    target = "scanme.nmap.org"  # Nmap's test server
    scanner = SimplePortScanner(target)
    scanner.scan_range(20, 80)  # Scan common service ports
