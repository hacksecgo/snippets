#!/usr/bin/env python3
"""
AI Phishing URL Detector
========================
AI isn't just for chatbots. In cybersecurity, it's hunting threats in real-time. This Python script uses machine learning to detect phishing URLs by analyzing patterns in domain names. It extracts fea

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-03-01 22:52:48
"""

import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class PhishingURLDetector:
    """AI-powered phishing URL classifier using ML features"""
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.feature_names = ['length', 'num_digits', 'num_special', 'has_ip', 'suspicious_keywords']
    
    def extract_features(self, url):
        """Extract ML features from URL string"""
        features = []
        
        # Feature 1: URL length
        features.append(len(url))
        
        # Feature 2: Number of digits
        features.append(sum(c.isdigit() for c in url))
        
        # Feature 3: Special characters count
        special_chars = re.findall(r'[!@#$%^&*()_+=\[\]{}|;:,.<>?]', url)
        features.append(len(special_chars))
        
        # Feature 4: Contains IP address (common in phishing)
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        features.append(1 if re.search(ip_pattern, url) else 0)
        
        # Feature 5: Suspicious keywords
        suspicious = ['login', 'verify', 'account', 'secure', 'update', 'banking']
        features.append(sum(1 for word in suspicious if word in url.lower()))
        
        return np.array(features).reshape(1, -1)
    
    def train(self, X, y):
        """Train the AI model on labeled data"""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        accuracy = self.model.score(X_test, y_test)
        print(f"Model trained. Accuracy: {accuracy:.2%}")
        
    def predict(self, url):
        """Predict if URL is phishing (1) or legitimate (0)"""
        features = self.extract_features(url)
        prediction = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0][1]
        return prediction, probability

# Example usage for pentesters
if __name__ == "__main__":
    # Simulated training data (in real use, load from dataset)
    detector = PhishingURLDetector()
    
    # Mock data: 1000 URLs with labels (0=legit, 1=phishing)
    X_train = np.random.rand(1000, 5) * 10  # Simulated features
    y_train = np.random.randint(0, 2, 1000)  # Simulated labels
    
    detector.train(X_train, y_train)
    
    # Test detection
    test_url = "http://secure-login-banking-update.xyz/verify"
    result, confidence = detector.predict(test_url)
    print(f"URL: {test_url}")
    print(f"Prediction: {'PHISHING' if result == 1 else 'SAFE'}")
    print(f"Confidence: {confidence:.1%}")
