import socket
import sys

def display_banner():
    print("\033[1;31m" + "="*60)
    print("   ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗ ██╗  ██╗")
    print("   ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║███║  ██║")
    print("   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║╚██║  ╚██║")
    print("   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██║   ██║")
    print("   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║ ██║   ██║")
    print("   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═╝   ╚═╝")
    print("                 RECON TOOL v1.1 // BY NEUROPRASSSSS")
    print("="*60 + "\033[0m\n")

def scan_specific_port(target_ip, port):
    print(f"\n\033[1;34m[*] Testing target {target_ip} on port {port}...\033[0m")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    
    try:
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"\033[1;32m[+] PORT {port}: OPEN\033[0m")
            try:
                s.sendall(b"Hello\r\n")
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"    \033[1;33m[i] Banner: {banner}\033[0m")
            except:
                print("    \033[1;30m[i] Target service remains silent.\033[0m")
        else:
            print(f"\033[1;31m[-] PORT {port}: CLOSED\033[0m")
    except Exception as e:
        print(f"\033[1;31m[-] Connection error: {e}\033[0m")
    finally:
        s.close()

def scan_common_ports(target_ip):
    common_ports = [22, 80, 443, 8000, 8888]
    print(f"\n\033[1;34m[*] Initializing rapid scan on {target_ip}...\033[0m")
    print("\033[1;30m" + "-" * 45 + "\033[0m")
    
    open_ports = 0
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"\033[1;32m[+] Port {port:<5} : OPEN\033[0m")
            open_ports += 1
        s.close()
        
    if open_ports == 0:
        print("\033[1;31m[-] No active common ports detected.\033[0m")
    print("\033[1;30m" + "-" * 45 + "\033[0m")

def main():
    display_banner()
    
    target_ip = input("\033[1;31m[?] Target IP Address -> \033[0m").strip()
    if not target_ip:
        print("\033[1;31m[-] Error: Target IP cannot be empty.\033[0m")
        sys.exit()
        
    while True:
        print("\n\033[1;35m[ CORE MENU ]\033[0m")
        print("1. Scan Standard Ports")
        print("2. Scan Single Specific Port")
        print("3. Define New Target IP")
        print("4. Terminate Session")
        
        choice = input("\n\033[1;31mnrp-recon > \033[0m").strip()
        
        if choice == "1":
            scan_common_ports(target_ip)
        elif choice == "2":
            try:
                target_port = int(input("\033[1;31m[?] Enter port number -> \033[0m"))
                scan_specific_port(target_ip, target_port)
            except ValueError:
                print("\033[1;31m[-] Error: Port must be an integer.\033[0m")
        elif choice == "3":
            target_ip = input("\033[1;31m[?] New Target IP -> \033[0m").strip()
        elif choice == "4":
            print("\n\033[1;31m[-] Session terminated. Exiting.\033[0m\n")
            break
        else:
            print("\033[1;31m[-] Invalid option.\033[0m")

if __name__ == "__main__":
    main()
