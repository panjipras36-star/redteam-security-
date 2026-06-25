# RECON1.1 - Active Network Scanner

RECON1.1 is a lightweight tactical active recon tool built natively in Python. It’s designed for quick network vector mapping and port auditing during engagement phases without relying on heavy third-party dependencies.

---

## What it does & Why it's useful

The tool maps out open ports using standard TCP full-handshake verification. 

* **Fast Port Auditing:** Instantly scans standard operational ports to find exposed entry points.
* **Service Banner Grabbing:** Attempts to grab service banners upon discovering an open port to help identify what's running.
* **Zero-Dependency:** Written completely in pure Python socket programming, meaning it runs out-of-the-box on any standard Kali Linux or Ubuntu environment.

### 🖥️ Interface Preview

```text
============================================================
   ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗ ██╗  ██╗
   ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║███║  ██║
   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║╚██║  ╚██║
   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██║   ██║
   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║ ██║   ██║
   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═╝   ╚═╝
                  RECON TOOL v1.1 // BY NEUROPRASSSSS
============================================================

[?] Target IP Address -> 192.168.1.14

[ CORE MENU ]
1. Scan Standard Ports
2. Scan Single Specific Port
3. Define New Target IP
4. Terminate Session

nrp-recon >
```
⚡ Run it instantly (One-Liner Execution)

You don't even need to clone this whole repository or manually copy-paste the source code. Just hit the copy button on the code block below, paste it straight into your Linux terminal, and press Enter:
curl -s [https://raw.githubusercontent.com/panjipras36-star/redteam-security-/main/recon11.py](https://raw.githubusercontent.com/panjipras36-star/redteam-security-/main/recon11.py) | python3
How it works behind the scenes:

    curl -s fetches the raw script code directly from this GitHub repo quietly in the background.

    The pipe | python3 instantly streams that code straight into the Python interpreter to execute it on the fly, leaving zero trash files on your system.
    
  ⚠️ Disclaimer

This tool is developed strictly for educational purposes, authorized penetration testing, and defensive hardening research. Scanning targets without explicit written consent is illegal. Use it responsibly.
