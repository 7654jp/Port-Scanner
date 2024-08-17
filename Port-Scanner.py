import socket

import threading

from datetime import datetime

import argparse



# Function to scan a single port

def scan_port(target, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:

        print(f"Port {port}: Open")

    else:

        print(f"Port {port}: Closed")

    s.close()



# Function to scan a range of ports

def port_scan(target, start_port, end_port):

    target_ip = socket.gethostbyname(target)

    print("-" * 50)

    print(f"Scanning Target: {target_ip}")

    print(f"Scanning started at: {str(datetime.now())}")

    print("-" * 50)



    for port in range(start_port, end_port + 1):

        thread = threading.Thread(target=scan_port, args=(target_ip, port))

        thread.start()



# Main

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple Port Scanner")

    parser.add_argument("target", help="Target IP address or hostname")

    parser.add_argument("start_port", type=int, help="Start port range")

    parser.add_argument("end_port", type=int, help="End port range")

    args = parser.parse_args()



    port_scan(args.target, args.start_port, args.end_port)

