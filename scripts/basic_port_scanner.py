#!/usr/bin/env python3
"""
Bug Bounty: Start Simple
========================
Bug bounty tip: Start with the low-hanging fruit! Most beginners waste time on complex attacks. Instead, automate finding common vulnerabilities first. This Python script scans for open ports - often 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 17:10:52
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port, timeout=1):
    """Scan single port on target host"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            # Try to grab banner for more info
            try:
                sock.send(b'\r
')
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                return port, banner[:50] if banner else "No banner"
            except:
                return port, "Open (no banner)"
        sock.close()
    except Exception as e:
        pass
    return None

def scan_ports(target, ports=[21,22,23,25,53,80,443,3306,8080,8443]):
    """Scan common ports with threading for speed"""
    print(f"[*] Scanning {target}...")
    open_ports = []
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, target, port) for port in ports]
        for future in futures:
            result = future.result()
            if result:
                port, banner = result
                print(f"[+] Port {port}/tcp open - {banner}")
                open_ports.append((port, banner))
    
    return open_ports

# Example usage (always get permission first!)
if __name__ == "__main__":
    # Only scan systems you own or have permission to test
    target = "scanme.nmap.org"  # Example: Nmap's test server
    print(f"Testing against authorized target: {target}")
    open_ports = scan_ports(target)
    print(f"
Found {len(open_ports)} open ports")
