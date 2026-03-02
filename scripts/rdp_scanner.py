#!/usr/bin/env python3
"""
How Ransomware Spreads: RDP Scanning
====================================
Ransomware doesn't just magically appear on your system. It needs a way in. Here are the top 3 infection vectors hackers use right now. First: Phishing emails with malicious attachments. Second: Explo

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 23:07:46
"""

import socket
import concurrent.futures
from ipaddress import ip_network

class RDPVulnerabilityScanner:
    """Simulates how attackers scan for vulnerable Remote Desktop ports"""
    
    def __init__(self, timeout=1):
        self.timeout = timeout
        self.common_ports = [3389, 3390, 3391]  # Common RDP ports
    
    def check_port(self, target_ip, port):
        """Check if a specific port is open on target"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((target_ip, port))
            sock.close()
            
            if result == 0:
                return (target_ip, port, "OPEN")
            else:
                return (target_ip, port, "CLOSED")
        except Exception as e:
            return (target_ip, port, f"ERROR: {str(e)}")
    
    def scan_network(self, network_cidr, max_workers=50):
        """Scan a network range for open RDP ports"""
        vulnerable_hosts = []
        
        # Generate all IPs in network range
        network = ip_network(network_cidr, strict=False)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            
            for ip in network.hosts():
                target_ip = str(ip)
                for port in self.common_ports:
                    futures.append(executor.submit(self.check_port, target_ip, port))
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result[2] == "OPEN":
                    vulnerable_hosts.append(result)
                    print(f"[!] Found open RDP port: {result[0]}:{result[1]}")
        
        return vulnerable_hosts

# Example usage (educational purposes only)
if __name__ == "__main__":
    scanner = RDPVulnerabilityScanner()
    
    # Simulating scan on a small test range
    print("[*] Scanning for vulnerable RDP ports...")
    results = scanner.scan_network("192.168.1.0/24")
    
    if results:
        print(f"
[!] Found {len(results)} potentially vulnerable hosts!")
        print("[!] These would be prime targets for ransomware deployment")
    else:
        print("[+] No open RDP ports found in scan range")
