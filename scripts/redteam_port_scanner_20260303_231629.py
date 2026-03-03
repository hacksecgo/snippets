#!/usr/bin/env python3
"""
Red vs Blue Team Explained
==========================
Ever wonder what red team vs blue team really means? Red team attacks like hackers to find weaknesses. Blue team defends and monitors for threats. Think offense vs defense! Red team uses tools like th

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 23:16:29
"""

import socket
import sys
from datetime import datetime

class RedTeamPortScanner:
    """Red team tool to identify open ports on a target system"""
    
    def __init__(self, target):
        self.target = target
        self.open_ports = []
    
    def scan_port(self, port):
        """Attempt to connect to a specific port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Timeout after 1 second
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                self.open_ports.append(port)
                service = self.get_service_name(port)
                print(f"[+] Port {port}/tcp open - {service}")
            sock.close()
            
        except KeyboardInterrupt:
            print("
Scan interrupted by user")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved")
            sys.exit()
        except socket.error:
            print("Could not connect to server")
            sys.exit()
    
    def get_service_name(self, port):
        """Map common ports to their services"""
        common_ports = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            443: "HTTPS",
            3306: "MySQL",
            3389: "RDP"
        }
        return common_ports.get(port, "Unknown service")
    
    def scan_range(self, start_port=1, end_port=1024):
        """Scan a range of ports (default: well-known ports)"""
        print(f"Scanning target: {self.target}")
        print(f"Scan started: {datetime.now()}")
        
        for port in range(start_port, end_port + 1):
            self.scan_port(port)
        
        print(f"
Scan completed. Found {len(self.open_ports)} open ports.")
        return self.open_ports

# Example usage (for educational purposes only)
if __name__ == "__main__":
    # Always scan only systems you own or have permission to test
    scanner = RedTeamPortScanner("127.0.0.1")  # Localhost example
    open_ports = scanner.scan_range(1, 100)  # Scan first 100 ports
