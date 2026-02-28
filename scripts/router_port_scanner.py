#!/usr/bin/env python3
"""
Secure Your Home Network
========================
Your home Wi-Fi is a hacker's favorite target. Here's how to lock it down in 30 seconds. First, change your router's default admin password—attackers know the defaults. Second, enable WPA3 encryption 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 22:38:14
"""

import socket
import sys
from datetime import datetime

class HomeNetworkScanner:
    """Scans common router ports to identify potential vulnerabilities"""
    
    def __init__(self, target_ip):
        self.target = target_ip
        self.common_ports = [
            80,    # HTTP (admin panel)
            443,   # HTTPS
            22,    # SSH
            23,    # Telnet (insecure!)
            8080,  # Alternative web
            21,    # FTP
            53     # DNS
        ]
    
    def scan_ports(self):
        """Scan common ports on home router"""
        print(f"Scanning {self.target}...")
        print("-" * 50)
        
        open_ports = []
        
        for port in self.common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout
            
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                service = self.get_service_name(port)
                print(f"[!] PORT {port}/TCP OPEN - {service}")
                open_ports.append((port, service))
                
                # Security warnings for dangerous ports
                if port == 23:
                    print("    ⚠️  Telnet is insecure! Disable immediately.")
                if port == 21:
                    print("    ⚠️  FTP transmits passwords in plain text!")
            
            sock.close()
        
        return open_ports
    
    def get_service_name(self, port):
        """Map port numbers to common services"""
        services = {
            80: "HTTP",
            443: "HTTPS",
            22: "SSH",
            23: "Telnet",
            8080: "HTTP-Alt",
            21: "FTP",
            53: "DNS"
        }
        return services.get(port, "Unknown")

# Example usage
if __name__ == "__main__":
    # Replace with your router's IP (commonly 192.168.1.1 or 192.168.0.1)
    router_ip = "192.168.1.1"
    
    scanner = HomeNetworkScanner(router_ip)
    open_ports = scanner.scan_ports()
    
    if open_ports:
        print(f"
Found {len(open_ports)} open port(s).")
        print("Secure your router by closing unnecessary ports!")
    else:
        print("No common ports open. Good!")

