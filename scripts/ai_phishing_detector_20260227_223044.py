#!/usr/bin/env python3
"""
AI Phishing Detector
====================
AI isn't just for chatbots. In cybersecurity, it's hunting threats in real-time. This Python script shows how AI can detect phishing URLs by analyzing patterns in the domain structure. It uses a simpl

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 22:30:43
"""

import re
from urllib.parse import urlparse
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class PhishingURLDetector:
    """AI-powered phishing URL detector using ML features"""
    
    def __init__(self):
        # Initialize ML model (in real use, this would be pre-trained)
        self.model = RandomForestClassifier(n_estimators=100)
        self.feature_names = ['length', 'num_digits', 'num_special', 'has_ip', 'suspicious_keywords']
        
    def extract_features(self, url):
        """Extract ML features from URL"""
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path
        
        features = [
            len(url),  # URL length
            sum(c.isdigit() for c in url),  # Number of digits
            sum(not c.isalnum() for c in url),  # Special characters
            1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0,  # IP address
            1 if any(kw in url.lower() for kw in ['login', 'secure', 'account', 'verify']) else 0  # Suspicious keywords
        ]
        return np.array(features).reshape(1, -1)
    
    def predict(self, url):
        """Predict if URL is phishing (simulated)"""
        features = self.extract_features(url)
        # In production, use model.predict() with trained data
        # For demo, simulate based on heuristic rules
        score = sum(features[0]) / 100
        return "PHISHING" if score > 0.3 else "LEGITIMATE"

# Example usage
if __name__ == "__main__":
    detector = PhishingURLDetector()
    
    test_urls = [
        "https://google.com",
        "http://192.168.1.1/login.php",
        "https://secure-account-verify-xyz123.com"
    ]
    
    print("AI Phishing Detection Results:")
    for url in test_urls:
        result = detector.predict(url)
        print(f"{url[:40]:<40} -> {result}")
