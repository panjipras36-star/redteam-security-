# Lab: Web Traffic Analysis with Burp Suite

This lab covers the essential steps for intercepting and analyzing web traffic. The goal is to establish a working proxy environment between the browser and Burp Suite.

## Setup & Workflow
- **Proxy:** Configured FoxyProxy to route traffic through `127.0.0.1:8080`.
- **Listener:** Verified the Burp Proxy Listener is active and running.
- **Interception:** Captured HTTP requests from `http://httpforever.com` to analyze headers and parameters.

## Visual Documentation

### 1. FoxyProxy Configuration
Browser proxy settings for routing traffic.
![FoxyProxy Setup](../images/1.jpeg)

### 2. Traffic Interception
Captured a GET request. This confirms the connection between the browser and Burp Suite is working.
![Intercept Success](../images/2.jpeg)

### 3. Proxy Listener Settings
Verified that the listener is properly bound to the local interface and port.
![Proxy Settings](../images/3.jpeg)

## Conclusion
The environment is fully functional. The next step is to perform manual request manipulation using the Repeater and Intruder modules.
