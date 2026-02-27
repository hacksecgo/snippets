#!/usr/bin/env python3
"""
Top 4 Recon Tools
=================
Want to find vulnerabilities before the bad guys do? You need these recon tools. First, Nmap for network discovery and port scanning. Shodan to find exposed devices and services. Amass for subdomain e

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 22:28:06
"""

import socket
import sys
import concurrent.futures
from datetime import datetime

class PortScanner:
    """A basic multi-threaded port scanner for reconnaissance"""
    
    def __init__(self, target, timeout=1.0):
        self.target = target
        self.timeout = timeout
        self.open_ports = []
    
    def scan_port(self, port):
        """Attempt to connect to a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            sock.close()
            
            if result == 0:
                return port
        except Exception:
            pass
        return None
    
    def scan_range(self, start_port=1, end_port=1024, max_threads=100):
        """Scan a range of ports using thread pooling"""
        print(f"[+] Scanning {self.target} from port {start_port} to {end_port}")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            future_to_port = {
                executor.submit(self.scan_port, port): port 
                for port in range(start_port, end_port + 1)
            }
            
            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                try:
                    result = future.result()
                    if result:
                        self.open_ports.append(result)
                        print(f"[+] Port {result} is OPEN")
                except Exception as e:
                    print(f"[-] Error scanning port {port}: {e}")
        
        return sorted(self.open_ports)

# Example usage for educational purposes
if __name__ == "__main__":
    # Always get proper authorization before scanning!
    target = "scanme.nmap.org"  # Nmap's test server
    scanner = PortScanner(target)
    
    # Scan common ports (educational use only)
    open_ports = scanner.scan_range(20, 100)
    print(f"
[+] Found {len(open_ports)} open ports: {open_ports}")
