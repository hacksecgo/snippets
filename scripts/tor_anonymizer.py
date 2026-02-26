#!/usr/bin/env python3
"""
Dark Web Explained + Tool Demo
==============================
The dark web isn't just for hackers and criminals. It's actually a small part of the deep web - everything not indexed by search engines. Think medical records, private databases, and yes, illegal mar

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 04:11:32
"""

import requests
from stem import Signal
from stem.control import Controller
import time

class TorAnonymizer:
    """Educational tool demonstrating Tor network principles"""
    
    def __init__(self, tor_port=9050, control_port=9051):
        self.tor_port = tor_port
        self.control_port = control_port
        self.session = self._create_tor_session()
    
    def _create_tor_session(self):
        """Create a requests session that routes through Tor"""
        session = requests.session()
        session.proxies = {
            'http': f'socks5h://127.0.0.1:{self.tor_port}',
            'https': f'socks5h://127.0.0.1:{self.tor_port}'
        }
        return session
    
    def renew_identity(self, password=''):
        """Request new Tor circuit (new IP address)"""
        try:
            with Controller.from_port(port=self.control_port) as controller:
                controller.authenticate(password=password)
                controller.signal(Signal.NEWNYM)
                time.sleep(controller.get_newnym_wait())
                return True
        except Exception as e:
            print(f"[!] Error renewing identity: {e}")
            return False
    
    def check_ip(self):
        """Check current public IP through Tor"""
        try:
            response = self.session.get('http://httpbin.org/ip', timeout=10)
            return response.json()['origin']
        except Exception as e:
            return f"Error: {e}"

# Example usage (educational purposes only)
if __name__ == "__main__":
    print("[*] Educational Tor Anonymizer Demo")
    print("[*] This simulates how dark web browsers work
")
    
    # Note: Requires Tor service running locally
    # tor = TorAnonymizer()
    # print(f"Current Tor IP: {tor.check_ip()}")
    # tor.renew_identity()
    # print(f"New Tor IP: {tor.check_ip()}")
