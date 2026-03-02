#!/usr/bin/env python3
"""
Red vs Blue: Cybersecurity Explained
====================================
Ever wondered how companies test their security? Meet the red team vs blue team. Red team: ethical hackers who attack systems to find weaknesses. Blue team: defenders who monitor, detect, and respond 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 23:03:58
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

class PortScanner:
    """Red Team Tool: Fast TCP port scanner for reconnaissance"""
    
    def __init__(self, target, max_workers=100):
        self.target = target
        self.max_workers = max_workers
        self.open_ports = []
    
    def scan_port(self, port):
        """Attempt TCP connection to specific port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Quick timeout for speed
            result = sock.connect_ex((self.target, port))
            sock.close()
            
            if result == 0:
                self.open_ports.append(port)
                return f"Port {port}: OPEN"
        except Exception:
            pass
        return None
    
    def scan_range(self, start_port=1, end_port=1024):
        """Scan a range of ports using thread pooling"""
        print(f"Scanning {self.target}...")
        ports = range(start_port, end_port + 1)
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = executor.map(self.scan_port, ports)
            
        for result in results:
            if result:
                print(result)
        
        print(f"
Found {len(self.open_ports)} open ports")
        return self.open_ports

# Example usage (Red Team reconnaissance)
if __name__ == "__main__":
    target = "192.168.1.1"  # Replace with authorized target
    scanner = PortScanner(target)
    open_ports = scanner.scan_range(20, 445)  # Common service ports
    
    # Blue Team would monitor for these scans!
