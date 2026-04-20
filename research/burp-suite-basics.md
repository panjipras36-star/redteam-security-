# Lab: Getting Started with Burp Suite

Just documenting my first steps into web traffic analysis. I'm setting up my environment to better understand how data moves between a browser and a server.

## What I've Done
- Set up **FoxyProxy** to route my browser traffic through Burp.
- Configured the **Proxy Listener** on `127.0.0.1:8080`.
- Successfully intercepted a basic request from `http://httpforever.com`.

## Visual Progress

### 1. FoxyProxy Setup
Simple configuration to make sure my browser is actually talking to Burp Suite.
![FoxyProxy Setup](../images/1.jpeg)

### 2. Checking the Listener
Double-checking that Burp is actually listening on the right port.
![Proxy Settings](../images/3.jpg)

### 3. First Successful Intercept
It was pretty cool to see the "hidden" data in a GET request for the first time.
![Intercept Success](../images/2.jpeg)

## Thoughts
This is a small start, but it’s the foundation for everything else. Being able to see and modify traffic is the first real step in understanding web security. Moving forward, I'll be practicing more with the Repeater and Intruder modules.
