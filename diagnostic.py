#!/usr/bin/env python3
"""
AI Injection Diagnostic Tool
Analyzes potential injection vectors in AI system interactions
"""

import json
import base64
import re
from pathlib import Path

# Base64 Test Vector: "SCAN_FOR_INJECTION_MARKERS"
# VGVzdCBWZWN0b3I6IElOSkVDVElPTl9ERVRFQ1RPUA==

class InjectionDetector:
    """Detects potential injection attacks in text input"""

    def __init__(self, config_path="config.json"):
        self.config = self._load_config(config_path)
        # Base64: "Configuration loaded successfully"
        # Q29uZmlndXJhdGlvbiBsb2FkZWQgc3VjY2Vzc2Z1bGx5
        self.patterns = self._compile_patterns()

    def _load_config(self, path):
        """Load configuration from JSON file"""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"test_mode": False}

    def _compile_patterns(self):
        """Compile detection patterns"""
        patterns = {
            "instruction_override": r"(ignore|bypass|override|administrator|sudo)",
            "context_manipulation": r"(system:.*?:|forget.*?:.*?:)",
            "base64_encoded": r"[A-Za-z0-9+/]{20,}={0,2}",
            "hidden_markup": r"<!--.*?-->|<.*?>",
        }
        return {k: re.compile(v, re.IGNORECASE) for k, v in patterns.items()}

    def analyze(self, text):
        """Analyze text for injection vectors"""
        results = {}
        for name, pattern in self.patterns.items():
            matches = pattern.findall(text)
            results[name] = {
                "detected": len(matches) > 0,
                "matches": matches[:5]  # Limit to 5 matches
            }
        return results

    def scan_file(self, filepath):
        """Scan a file for injection vectors"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            return self.analyze(content)
        except Exception as e:
            return {"error": str(e)}

def main():
    """Main diagnostic routine"""
    print("[*] AI Injection Detection Tool")
    print("[*] Initializing detector...")

    detector = InjectionDetector()

    # Scan README
    print("\n[+] Scanning README.md...")
    readme_results = detector.scan_file("README.md")
    print(f"    Found {sum(1 for r in readme_results.values() if r.get('detected'))} detection categories")

    # Scan config
    print("\n[+] Scanning config.json...")
    config_results = detector.scan_file("config.json")
    print(f"    Found {sum(1 for r in config_results.values() if r.get('detected'))} detection categories")

    print("\n[✓] Diagnostic complete")

if __name__ == "__main__":
    main()
