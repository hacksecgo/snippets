#!/usr/bin/env python3
"""
AI Phishing URL Detector
========================
AI isn't just for chatbots—it's revolutionizing cybersecurity. This Python script uses machine learning to detect phishing URLs in real-time. It analyzes URL features like length, special characters, 

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 04:10:02
"""

import re
import tldextract
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

class PhishingURLDetector:
    """AI-powered phishing URL detector using ML features"""
    
    def __init__(self, model_path='phishing_model.pkl'):
        # Load pre-trained model (train separately with labeled data)
        try:
            self.model = joblib.load(model_path)
        except:
            # Fallback to a fresh model if file not found
            self.model = RandomForestClassifier(n_estimators=100)
        
    def extract_features(self, url):
        """Extract 10 key features from a URL for ML prediction"""
        features = []
        
        # 1. URL length
        features.append(len(url))
        
        # 2. Number of dots in domain
        ext = tldextract.extract(url)
        features.append(ext.domain.count('.'))
        
        # 3. Contains IP address?
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        features.append(1 if re.search(ip_pattern, url) else 0)
        
        # 4. Number of special chars (@, //, -)
        features.append(url.count('@') + url.count('//') + url.count('-'))
        
        # 5. Uses HTTPS?
        features.append(1 if url.startswith('https') else 0)
        
        # 6-10: Add more features like entropy, domain age lookup, etc.
        # For demo, pad with placeholder features
        features.extend([0, 0, 0, 0, 0])
        
        return np.array(features).reshape(1, -1)
    
    def predict(self, url):
        """Predict if URL is phishing (1) or legitimate (0)"""
        features = self.extract_features(url)
        prediction = self.model.predict(features)[0]
        confidence = np.max(self.model.predict_proba(features))
        return prediction, round(confidence, 3)

# Example usage for pentesters/SOC analysts
if __name__ == "__main__":
    detector = PhishingURLDetector()
    
    test_urls = [
        "https://secure-paypal.com.login.verify.net",  # Likely phishing
        "https://github.com/security-tools",           # Legitimate
        "http://192.168.1.1@malicious-site.com"        # Suspicious
    ]
    
    for url in test_urls:
        result, confidence = detector.predict(url)
        status = "PHISHING" if result == 1 else "LEGITIMATE"
        print(f"{url[:50]:<50} -> {status} (Confidence: {confidence})")
