#!/usr/bin/env python3
"""
Kubernetes Port Scanner
=======================
Ever wonder how attackers find exposed Kubernetes dashboards? They're scanning for port 443 and 6443. Here's a Python script that checks for open Kubernetes API ports. It uses socket connections to id

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 04:06:36
"""

#!/usr/bin/env python3
"""
Kubernetes API Port Scanner
Checks for exposed Kubernetes API endpoints on common ports
"""

import socket
import concurrent.futures
from typing import List

class K8sPortScanner:
    """Scans for open Kubernetes-related ports on target hosts"""
    
    # Common Kubernetes API ports
    K8S_PORTS = [443, 6443, 8443, 10250, 10255]
    
    def __init__(self, timeout: float = 2.0):
        self.timeout = timeout
    
    def check_port(self, target: str, port: int) -> dict:
        """Check if a specific port is open on target"""
        result = {"target": target, "port": port, "open": False}
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            # Attempt connection
            connection_result = sock.connect_ex((target, port))
            
            if connection_result == 0:
                result["open"] = True
                
                # Try to get banner for additional info
                try:
                    sock.send(b"GET / HTTP/1.0\r
\r
")
                    banner = sock.recv(1024).decode('utf-8', errors='ignore')
                    if "k8s" in banner.lower() or "kubernetes" in banner.lower():
                        result["k8s_indicator"] = True
                except:
                    pass
            
            sock.close()
            
        except Exception as e:
            result["error"] = str(e)
        
        return result
    
    def scan_target(self, target: str, ports: List[int] = None) -> List[dict]:
        """Scan multiple ports on a single target using threads"""
        if ports is None:
            ports = self.K8S_PORTS
        
        results = []
        
        # Use thread pool for concurrent scanning
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(self.check_port, target, port): port for port in ports}
            
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        
        return results

# Example usage for penetration testing
if __name__ == "__main__":
    scanner = K8sPortScanner(timeout=1.5)
    
    # Scan a target (in real pentest, this would be authorized testing)
    target_ip = "192.168.1.100"  # Replace with authorized target
    print(f"[+] Scanning {target_ip} for Kubernetes ports...")
    
    results = scanner.scan_target(target_ip)
    
    # Display results
    for result in results:
        status = "OPEN" if result["open"] else "closed"
        indicator = " (K8s indicator)" if result.get("k8s_indicator") else ""
        print(f"  Port {result['port']}: {status}{indicator}")
