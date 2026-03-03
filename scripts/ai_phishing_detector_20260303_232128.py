#!/usr/bin/env python3
"""
AI Phishing URL Detector
========================
AI isn't just for chatbots. It's revolutionizing cybersecurity. This Python script uses machine learning to detect phishing URLs in real-time. It analyzes URL structure, domain age, and suspicious pat

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-03 23:21:28
"""

import re
import tldextract
import joblib
import numpy as np
from urllib.parse import urlparse

class PhishingURLDetector:
    """AI-powered phishing URL detector using a pre-trained ML model"""
    
    def __init__(self, model_path='phishing_model.pkl'):
        # Load pre-trained model (trained on URL features)
        self.model = joblib.load(model_path)
        
    def extract_features(self, url):
        """Extract 10 key features from URL for ML prediction"""
        features = []
        
        # 1. URL length (longer URLs often suspicious)
        features.append(len(url))
        
        # 2. Number of dots in domain
        domain = urlparse(url).netloc
        features.append(domain.count('.'))
        
        # 3. Contains IP address instead of domain
        features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0)
        
        # 4. Uses HTTPS
        features.append(1 if urlparse(url).scheme == 'https' else 0)
        
        # 5. Number of special characters
        features.append(len(re.findall(r'[!@#$%^&*()\-+=]', url)))
        
        # 6. Subdomain count
        extracted = tldextract.extract(url)
        features.append(len(extracted.subdomain.split('.')) if extracted.subdomain else 0)
        
        # 7. Contains suspicious keywords
        suspicious = ['login', 'verify', 'account', 'secure', 'update']
        features.append(1 if any(word in url.lower() for word in suspicious) else 0)
        
        # 8. URL shortening service
        shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 'ow.ly']
        features.append(1 if any(short in url for short in shorteners) else 0)
        
        # 9. Number of digits in URL
        features.append(len(re.findall(r'\d', url)))
        
        # 10. Path length
        features.append(len(urlparse(url).path))
        
        return np.array(features).reshape(1, -1)
    
    def predict(self, url):
        """Predict if URL is phishing (1) or legitimate (0)"""
        features = self.extract_features(url)
        prediction = self.model.predict(features)[0]
        confidence = self.model.predict_proba(features)[0].max()
        return prediction, round(confidence, 3)

# Example usage for pentesters/SOC analysts
if __name__ == '__main__':
    detector = PhishingURLDetector('phishing_model.pkl')
    
    test_urls = [
        'https://legitimate-bank.com/login',
        'http://142.250.74.46/verify-account',
        'https://bit.ly/suspicious-offer'
    ]
    
    for url in test_urls:
        result, confidence = detector.predict(url)
        status = 'PHISHING' if result == 1 else 'LEGITIMATE'
        print(f'{url[:50]:<50} -> {status} ({confidence*100}% confidence)')
