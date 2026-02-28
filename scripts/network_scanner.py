#!/usr/bin/env python3
"""
Secure Your Home Wi-Fi in 30 Sec
================================
Your home Wi-Fi is a hacker's favorite target. Here's how to lock it down in 30 seconds. First, change your router's default admin password—attackers know the defaults. Second, enable WPA3 encryption,

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 16:34:31
"""

import socket
import subprocess
import platform
from datetime import datetime

def scan_local_network(base_ip='192.168.1.', timeout=1):
    """
    Scans for active devices on local network.
    Real pentesters use this to find vulnerable devices on home networks.
    """
    active_hosts = []
    
    # Ping sweep to find live hosts
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    print(f"[+] Scanning {base_ip}0/24 network...")
    
    for i in range(1, 255):
        ip = f"{base_ip}{i}"
        
        # Using ping to check if host is up
        command = ['ping', param, '1', '-W', str(timeout), ip]
        
        try:
            output = subprocess.run(command, capture_output=True, text=True)
            
            if 'ttl=' in output.stdout.lower() or 'ttl=' in output.stderr.lower():
                active_hosts.append(ip)
                print(f"  [+] Found active host: {ip}")
                
                # Try to get hostname
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                    print(f"     Hostname: {hostname}")
                except socket.herror:
                    pass
                    
        except Exception as e:
            continue
    
    return active_hosts

# Example usage
if __name__ == "__main__":
    print("Home Network Device Scanner")
    print("=" * 30)
    devices = scan_local_network()
    print(f"
Total devices found: {len(devices)}")
    print("
⚠️  If you see unknown devices, someone might be on your network!")
