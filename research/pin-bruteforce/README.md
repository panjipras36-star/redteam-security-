# Vulnerability Research: Automated Authentication Bypass via Numeric Brute-Force

This repository documents the identification, exploitation, and remediation of an authentication bypass vulnerability simulated in a local API endpoint. This lab demonstrates how the absence of anti-brute-force controls can lead to complete account compromise.

## 🎯 Executive Summary
- **Vulnerability Type:** Improper Restriction of Excessive Authentication Attempts ([CWE-307](https://cwe.mitre.org/data/definitions/307.html)) / Broken Authentication ([OWASP Top 10](https://owasp.org/www-project-top-10/)).
- **Severity:** High 🔴
- **Impact:** Unauthorized data access, account takeover, and cryptographic credential stuffing.
- **Objective:** Develop a proof-of-concept (PoC) automation script to systematically exploit a rate-limitless API using zero-padded numeric permutations (`0000`-`9999`).

---

## 🛡️ Laboratory Architecture
To maintain a controlled testing environment, the architecture is split into two distinct modules:

### 1. The Target Component (`app_target.py`)
A simulated backend service built via Flask mimicking a production authentication API (`/api/auth`). 
- **Flaw:** The endpoint processes incoming JSON payloads and validates credentials against a static MD5 hash value *without* tracking request frequency, rendering it highly vulnerable to automated high-velocity requests.

### 2. The Weaponized Exploitation Script (`exploit.py`)
A custom Python-based multi-request engine designed to simulate a production-level brute-force attack.
- **Mechanics:** Utilizes the `requests` library to handle HTTP POST sessions. It features an automated string-formatting algorithm (`f"{pin:04d}"`) to ensure comprehensive coverage of all 10,000 mathematical permutations while parsing JSON API state responses dynamically.

---

## 🚀 Deployment & Proof of Concept (PoC)

### Prerequisites
Ensure Flask and Requests libraries are provisioned in your Python environment:
```bash
pip install flask requests

Execution Flow

    Initialize the Vulnerable Target Server (Terminal 1):
python3 app_target.py
Launch the Exploitation Engine (Terminal 2):
Bash
python3 exploit.py
