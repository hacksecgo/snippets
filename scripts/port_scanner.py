#!/usr/bin/env python3
"""
Red Team vs Blue Team Explained
===============================
Ever wondered how companies test their security? Meet the red team vs blue team. Red team: ethical hackers attacking systems to find weaknesses. Blue team: defenders monitoring, detecting, and respond

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 10:21:16
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

class PortScanner:
    """Red Team tool: Fast TCP port scanner for reconnaissance"""
    
    def __init__(self, target, max_workers=100):
        self.target = target
        self.max_workers = max_workers
        self.open_ports = []
    
    def scan_port(self, port):
        """Attempt TCP connection to a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            sock.close()
            
            if result == 0:
                self.open_ports.append(port)
                try:
                    service = socket.getservbyport(port, 'tcp')
                except:
                    service = 'unknown'
                print(f"[+] Port {port}/tcp open - {service}")
        except:
            pass
    
    def scan_range(self, start_port=1, end_port=1024):
        """Scan a range of ports using thread pooling"""
        print(f"[*] Scanning {self.target} (ports {start_port}-{end_port})")
        start_time = datetime.now()
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.scan_port, range(start_port, end_port + 1))
        
        print(f"
[*] Scan completed in {datetime.now() - start_time}")
        print(f"[*] Found {len(self.open_ports)} open ports")
        return self.open_ports

# Example usage (Red Team reconnaissance)
if __name__ == "__main__":
    target = "scanme.nmap.org"  # Legal test target
    scanner = PortScanner(target)
    open_ports = scanner.scan_range(20, 100)  # Scan common ports
