#!/usr/bin/env python3
"""
SQL Injection in 30 Seconds
===========================
Ever wonder how hackers steal data from websites? It's often with SQL injection. Here's how it works: When you log into a site, it asks a database 'Is this user legit?' But if you type ' OR '1'='1' as

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-27 22:25:32
"""

import sqlite3
import hashlib

class VulnerableLogin:
    """Demonstrates SQL injection vulnerability and secure fix"""
    
    def __init__(self, db_name='users.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self):
        """Create a sample users table"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                               (id INTEGER PRIMARY KEY, 
                                username TEXT, 
                                password TEXT)''')
        # Add test user
        self.cursor.execute('''INSERT OR IGNORE INTO users 
                               (username, password) VALUES (?, ?)''', 
                               ('admin', hashlib.sha256(b'password123').hexdigest()))
        self.conn.commit()
    
    def vulnerable_login(self, username, password):
        """VULNERABLE: String concatenation allows SQL injection"""
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        self.cursor.execute(query)
        return self.cursor.fetchone() is not None
    
    def secure_login(self, username, password):
        """SECURE: Parameterized queries prevent injection"""
        query = "SELECT * FROM users WHERE username=? AND password=?"
        self.cursor.execute(query, (username, password))
        return self.cursor.fetchone() is not None
    
    def close(self):
        self.conn.close()

# DEMONSTRATION
if __name__ == '__main__':
    app = VulnerableLogin()
    
    # Legitimate login attempt
    print(f"Legitimate login: {app.secure_login('admin', hashlib.sha256(b'password123').hexdigest())}")
    
    # SQL Injection attack - bypasses password check!
    malicious_password = "' OR '1'='1"
    print(f"SQL Injection bypass: {app.vulnerable_login('admin', malicious_password)}")
    
    # Secure method blocks injection
    print(f"Secure method blocks injection: {app.secure_login('admin', malicious_password)}")
    
    app.close()
