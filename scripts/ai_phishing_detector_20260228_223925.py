#!/usr/bin/env python3
"""
AI Phishing URL Detector
========================
AI isn't just for chatbots. In cybersecurity, it's hunting threats in real-time. This Python script uses machine learning to detect phishing URLs by analyzing patterns in the domain structure. It extr

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 22:39:25
"""

import re
import tldextract
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class PhishingURLDetector:
    """AI-powered phishing URL classifier using ML features"""
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.feature_names = ['url_length', 'num_digits', 'num_special_chars', 
                              'has_ip', 'suspicious_keywords', 'subdomain_count']
    
    def extract_features(self, url):
        """Extract ML features from URL for classification"""
        features = []
        
        # Feature 1: URL length
        features.append(len(url))
        
        # Feature 2: Number of digits
        features.append(sum(c.isdigit() for c in url))
        
        # Feature 3: Special characters count
        features.append(len(re.findall(r'[!@#$%^&*()_+=\[\]{}|;:,.<>?]', url)))
        
        # Feature 4: Contains IP address
        features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)
        
        # Feature 5: Suspicious keywords
        suspicious = ['login', 'verify', 'secure', 'account', 'update', 'banking']
        features.append(sum(1 for word in suspicious if word in url.lower()))
        
        # Feature 6: Number of subdomains
        extracted = tldextract.extract(url)
        features.append(extracted.subdomain.count('.') + 1 if extracted.subdomain else 0)
        
        return np.array(features).reshape(1, -1)
    
    def predict(self, url):
        """Predict if URL is phishing (1) or legitimate (0)"""
        features = self.extract_features(url)
        return self.model.predict(features)[0]

# Example usage for pentesters
if __name__ == "__main__":
    detector = PhishingURLDetector()
    
    # Simulated training data (in real use, load from CSV)
    X_train = np.array([[50, 5, 2, 0, 3, 2],  # Phishing
                        [25, 1, 1, 0, 0, 1]]) # Legitimate
    y_train = np.array([1, 0])
    
    detector.model.fit(X_train, y_train)
    
    # Test prediction
    test_url = "http://secure-login-banking-update.xyz.com/verify"
    result = detector.predict(test_url)
    print(f"URL: {test_url}")
    print(f"Prediction: {'PHISHING' if result == 1 else 'LEGITIMATE'}")
