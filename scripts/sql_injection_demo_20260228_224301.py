#!/usr/bin/env python3
"""
SQL Injection Explained
=======================
Stop making this critical web security mistake! Developers often trust user input without validation, leading to SQL injection attacks. This happens when attackers inject malicious SQL code through fo

⚠️  EDUCATIONAL PURPOSES ONLY — Get proper authorization before testing.
📺  Watch the video walkthrough on our Instagram!
📅  2026-02-28 22:43:01
"""

import sqlite3
import sys

class SQLInjectionDemo:
    """Demonstrates SQL injection vulnerability and prevention"""
    
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self._setup_database()
    
    def _setup_database(self):
        """Create test database with sample data"""
        self.cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        self.cursor.execute('''INSERT INTO users (username, password) VALUES ('admin', 'SuperSecret123')''')
        self.cursor.execute('''INSERT INTO users (username, password) VALUES ('alice', 'AlicePass456')''')
        self.conn.commit()
    
    def vulnerable_login(self, username):
        """VULNERABLE: Direct string concatenation - DO NOT USE IN PRODUCTION"""
        query = f"SELECT * FROM users WHERE username = '{username}'"
        print(f"[VULNERABLE] Executing: {query}")
        return self.cursor.execute(query).fetchall()
    
    def safe_login(self, username):
        """SAFE: Parameterized query prevents SQL injection"""
        query = "SELECT * FROM users WHERE username = ?"
        print(f"[SAFE] Executing parameterized query")
        return self.cursor.execute(query, (username,)).fetchall()
    
    def demonstrate_attack(self):
        """Show how attacker can bypass authentication"""
        print("
=== LEGITIMATE LOGIN ===")
        print(f"Result: {self.safe_login('admin')}")
        
        print("
=== SQL INJECTION ATTACK ===")
        malicious_input = "admin' OR '1'='1"
        print(f"Attacker input: {malicious_input}")
        print(f"Result: {self.vulnerable_login(malicious_input)}")
        
        print("
=== DROP TABLE ATTACK ===")
        destructive_input = "admin'; DROP TABLE users; --"
        print(f"Attacker input: {destructive_input}")
        print("WARNING: This would delete the entire users table!")

if __name__ == "__main__":
    demo = SQLInjectionDemo()
    demo.demonstrate_attack()
