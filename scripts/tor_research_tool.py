#!/usr/bin/env python3
"""
Dark Web Explained + Python Demo
================================
The dark web isn't just for hackers. It's the unindexed part of the internet you can't find on Google. You need special software like Tor to access it. While it has legitimate uses like protecting jou

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 10:20:27
"""

import requests
import socks
import socket
from stem.control import Controller
from stem import Signal

class TorSession:
    """Educational example: Creating a session through Tor for research"""
    
    def __init__(self, tor_port=9050, control_port=9051):
        """Initialize Tor proxy settings"""
        self.tor_port = tor_port
        self.control_port = control_port
        self.session = None
        
    def create_session(self):
        """Create a requests session that routes through Tor"""
        # Set up SOCKS proxy for Tor
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", self.tor_port)
        socket.socket = socks.socksocket
        
        # Create session with Tor user-agent
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        })
        return self.session
    
    def renew_identity(self, password=""):
        """Request new Tor circuit (new IP address)"""
        with Controller.from_port(port=self.control_port) as controller:
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)
            print("[*] Tor identity renewed")
    
    def check_ip(self):
        """Verify Tor is working by checking public IP"""
        if not self.session:
            self.create_session()
        response = self.session.get("https://check.torproject.org/api/ip")
        return response.json()

# Example usage for educational purposes
if __name__ == "__main__":
    print("[*] Educational Tor demonstration")
    print("[*] Requires: pip install requests pysocks stem")
    print("[*] Note: Tor service must be running locally")
    
    # This would only work if Tor is installed and configured
    # tor_session = TorSession()
    # session = tor_session.create_session()
    # print("IP Info:", tor_session.check_ip())
