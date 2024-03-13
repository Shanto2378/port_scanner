import socket
import termcolor

def scan(target, ports):
    print("\n" + "[+] Starting Scan for: " + str(target))
    for port in range(1, ports):
        scan_port(target,port)

def scan_port(ipaddress, port): # Function to scan port
    try:
        sock = socket.socket() # Create a socket object
        sock.connect((ipaddress, port)) # Connect to the port
        print("[+] Port Opened: " + str(port))
    except:
        pass

targets = input("[*] Enter Target to Scan(Split them by ,): ") # Input target to scan
ports = int(input("[*] Enter How Many Ports You want to scan: ")) # Input port to scan

if ',' in targets:
    print("[+] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)