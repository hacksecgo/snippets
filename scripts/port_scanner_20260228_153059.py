#!/usr/bin/env python3
"""
Pen Testing Explained in 30s
============================
Ever wonder how hackers find weaknesses? That's penetration testing! It's authorized simulated attacks to find security flaws before real bad guys do. Think of it like a home security check, but for d

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 15:30:58
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port, timeout=1):
    """
    Attempt to connect to a specific port on target IP
    Returns port number if open, None if closed/filtered
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        
        if result == 0:
            return port
    except Exception:
        pass
    return None

def port_scanner(target, start_port=1, end_port=1024, max_workers=50):
    """
    Scan a range of ports on target using multithreading
    Common ports: 22(SSH), 80(HTTP), 443(HTTPS), 3389(RDP)
    """
    open_ports = []
    print(f"[+] Scanning {target} ports {start_port}-{end_port}")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for port in range(start_port, end_port + 1):
            future = executor.submit(scan_port, target, port)
            futures.append((port, future))
        
        for port, future in futures:
            result = future.result()
            if result:
                open_ports.append(port)
                print(f"[+] Port {port} is OPEN")
    
    return open_ports

# Example usage (for educational purposes only - test YOUR OWN systems)
if __name__ == "__main__":
    # Always scan only systems you own or have permission to test!
    target = "127.0.0.1"  # Localhost example
    open_ports = port_scanner(target, 20, 100)
    print(f"
[+] Found {len(open_ports)} open ports: {open_ports}")
