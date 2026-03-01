#!/usr/bin/env python3
"""
Red Team vs Blue Team Explained
===============================
Ever wonder how companies test their own security? Meet red team vs blue team. Red team: ethical hackers who attack systems like real criminals would. Blue team: defenders who monitor, detect, and res

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 16:48:01
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

class PortScanner:
    """Red Team tool: Fast TCP port scanner to discover open services"""
    
    def __init__(self, target, timeout=1.0, max_workers=100):
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
            sock.close()
            
            if result == 0:
                self.open_ports.append(port)
                return f"[+] Port {port}: OPEN"
        except Exception:
            pass
        return None
    
    def scan_range(self, start_port=1, end_port=1024):
        """Scan a range of ports using thread pooling for speed"""
        print(f"Scanning {self.target} (ports {start_port}-{end_port})")
        start_time = datetime.now()
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = executor.map(self.scan_port, range(start_port, end_port + 1))
            
            for result in results:
                if result:
                    print(result)
        
        scan_time = datetime.now() - start_time
        print(f"
Scan completed in {scan_time.total_seconds():.2f} seconds")
        print(f"Found {len(self.open_ports)} open ports")
        return self.open_ports

# Example usage (Red Team perspective)
if __name__ == "__main__":
    # Always get proper authorization before scanning!
    target_ip = "192.168.1.1"  # Replace with authorized target
    scanner = PortScanner(target_ip)
    
    # Scan common ports (ethical hackers would scan specific ranges)
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3389, 8080]
    
    print("Red Team Port Scanner - Educational Use Only
")
    for port in common_ports:
        result = scanner.scan_port(port)
        if result:
            print(result)
