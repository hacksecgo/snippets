#!/usr/bin/env python3
"""
Why You NEED a VPN on Public Wi-Fi
==================================
Ever wonder how easy it is for hackers to see your data on public Wi-Fi? Without a VPN, everything you send is visible. Your passwords, messages, even your location. A VPN encrypts your connection, cr

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 10:22:14
"""

import socket
import ssl
from datetime import datetime

class UnencryptedTrafficSniffer:
    """Demonstrates how unencrypted HTTP traffic can be intercepted on a network"""
    
    def __init__(self, interface='lo', port=8080):
        self.interface = interface
        self.port = port
        self.socket = None
    
    def start_proxy(self):
        """Create a simple proxy to intercept HTTP traffic"""
        try:
            # Create socket to listen for connections
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(('127.0.0.1', self.port))
            self.socket.listen(5)
            
            print(f"[+] Proxy listening on port {self.port}")
            print(f"[+] Configure browser to use proxy 127.0.0.1:{self.port}")
            print(f"[+] Intercepting unencrypted HTTP traffic...
")
            
            while True:
                client_sock, addr = self.socket.accept()
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Connection from {addr[0]}")
                
                # Receive client request
                request = client_sock.recv(4096).decode('utf-8', errors='ignore')
                
                # Extract sensitive info from unencrypted HTTP
                self._analyze_request(request)
                
                # Forward request (simplified - real proxy would handle response)
                client_sock.send(b"HTTP/1.1 200 OK\r
\r
Traffic intercepted!")
                client_sock.close()
                
        except KeyboardInterrupt:
            print("
[!] Stopping proxy...")
        finally:
            if self.socket:
                self.socket.close()
    
    def _analyze_request(self, request):
        """Look for sensitive data in unencrypted HTTP traffic"""
        keywords = ['password', 'login', 'email', 'username', 'credit', 'ssn']
        
        for keyword in keywords:
            if keyword in request.lower():
                print(f"  [!] Found '{keyword}' in plaintext traffic!")
                
        # Show first 200 chars of request
        preview = request[:200].replace('
', ' ').replace('\r', '')
        if preview:
            print(f"  [>] Request: {preview}...
")

# Example usage
if __name__ == "__main__":
    # This simulates what an attacker could see on unencrypted networks
    proxy = UnencryptedTrafficSniffer(port=8888)
    proxy.start_proxy()
