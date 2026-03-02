#!/usr/bin/env python3
"""
Secure Your Home Wi-Fi in 30 Sec
================================
Your home Wi-Fi is probably wide open to hackers. Let's lock it down in 30 seconds. First, change your router's default admin password—attackers know the defaults. Second, enable WPA3 encryption or at

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 23:05:13
"""

import scapy.all as scapy
import socket
import sys

class NetworkDiscovery:
    """Realistic tool to discover devices on a local network"""
    
    def __init__(self, interface):
        self.interface = interface
    
    def arp_scan(self, target_ip_range):
        """Perform ARP scan to find active devices"""
        print(f"[+] Scanning {target_ip_range} on {self.interface}")
        
        # Create ARP request packet
        arp_request = scapy.ARP(pdst=target_ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast/arp_request
        
        # Send packet and capture responses
        answered_list = scapy.srp(packet, timeout=2, 
                                 iface=self.interface, verbose=False)[0]
        
        devices = []
        for element in answered_list:
            device_info = {
                "ip": element[1].psrc,
                "mac": element[1].hwsrc,
                "vendor": self.get_vendor(element[1].hwsrc)
            }
            devices.append(device_info)
            
        return devices
    
    def get_vendor(self, mac_address):
        """Try to identify device manufacturer from MAC"""
        # Simplified vendor lookup (real version uses OUI database)
        vendors = {
            "a4:5e:60": "Apple",
            "dc:a6:32": "Raspberry Pi",
            "00:50:56": "VMware",
            "c8:3a:35": "TP-Link"
        }
        prefix = mac_address[:8].lower()
        return vendors.get(prefix, "Unknown")

# Example usage
if __name__ == "__main__":
    # Ethical use: Only scan YOUR OWN network
    scanner = NetworkDiscovery("eth0")
    devices = scanner.arp_scan("192.168.1.0/24")
    
    print("
[+] Devices found on network:")
    for device in devices:
        print(f"   IP: {device['ip']} | MAC: {device['mac']} | Vendor: {device['vendor']}")
