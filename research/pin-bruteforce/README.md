# Lab Research: Automated 4-Digit PIN Brute-Forcing

This documentation covers the research and development of an automation script designed to test credentials against a local simulated API endpoint.

## 🎯 Executive Summary
The objective of this lab is to understand how automated scripts can systematically guess numeric credentials (PINs) when an API lacks proper rate-limiting or account lockout mechanisms.

## 🛡️ Environment Setup
To replicate this lab environment locally, you will need to use the two separate Python scripts included in this directory:
- `app_target.py` : The simulated vulnerable target server built with Flask.
- `exploit.py` : The automated Python script that systematically tests PINs from `0000` to `9999`.
