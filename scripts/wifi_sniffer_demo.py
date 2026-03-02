#!/usr/bin/env python3
"""
Why You NEED a VPN on Public Wi-Fi
==================================
Think your coffee shop Wi-Fi is safe? Think again. Without a VPN, every website you visit, every password you type, is visible to anyone on that network. A VPN encrypts your connection, creating a sec

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-02 17:01:04
"""

import socket
import struct
from datetime import datetime

class PublicWiFiSniffer:
    """
    Demonstrates how unencrypted traffic on public Wi-Fi can be intercepted.
    Educational tool only - use on networks you own or have permission to test.
    """
    
    def __init__(self, interface='eth0'):
        self.interface = interface
        
    def sniff_http_headers(self, max_packets=50):
        """
        Captures unencrypted HTTP traffic to show what data is exposed.
        In reality, attackers use tools like Wireshark, but this demonstrates the concept.
        """
        try:
            # Create raw socket to capture packets
            sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
            sock.bind((self.interface, 0))
            
            print(f"[+] Sniffing on {self.interface} (stop with Ctrl+C)")
            print(f"[!] Without VPN, attackers can see:
")
            
            packet_count = 0
            while packet_count < max_packets:
                raw_data, _ = sock.recvfrom(65535)
                
                # Extract Ethernet header (first 14 bytes)
                eth_header = raw_data[:14]
                eth_protocol = struct.unpack('!H', eth_header[12:14])[0]
                
                # Check for IP packets (0x0800 = IPv4)
                if eth_protocol == 0x0800:
                    ip_header = raw_data[14:34]
                    protocol = ip_header[9]
                    
                    # Check for TCP (protocol 6)
                    if protocol == 6:
                        tcp_header_start = 14 + (ip_header[0] & 0x0F) * 4
                        tcp_header = raw_data[tcp_header_start:tcp_header_start+20]
                        
                        # Extract source/dest ports
                        src_port = struct.unpack('!H', tcp_header[:2])[0]
                        dst_port = struct.unpack('!H', tcp_header[2:4])[0]
                        
                        # Look for HTTP traffic (port 80) or unencrypted data
                        if dst_port == 80 or src_port == 80:
                            data_start = tcp_header_start + ((tcp_header[12] >> 4) * 4)
                            payload = raw_data[data_start:]
                            
                            if payload:
                                try:
                                    text = payload.decode('utf-8', errors='ignore')
                                    if 'GET' in text or 'POST' in text or 'Host:' in text:
                                        print(f"[{datetime.now().strftime('%H:%M:%S')}] HTTP traffic detected")
                                        for line in text.split('
')[:3]:
                                            if line.strip():
                                                print(f"   {line[:60]}")
                                        print()
                                        packet_count += 1
                                except:
                                    pass
                
        except KeyboardInterrupt:
            print("
[!] Sniffing stopped")
            print("[✓] This is why you need a VPN - it encrypts ALL this data!")
        except PermissionError:
            print("[!] Run with sudo/administrator privileges")
        finally:
            sock.close()

# Example usage
if __name__ == "__main__":
    # Educational demonstration - requires appropriate permissions
    sniffer = PublicWiFiSniffer('eth0')
    # In real pentest, you'd use proper tools like Scapy
    # This shows the CONCEPT of traffic interception
    sniffer.sniff_http_headers(max_packets=10)
