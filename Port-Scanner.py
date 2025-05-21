import socket

import threading

from datetime import datetime

def chk_uint(st):
	try:
		return int(st)
	except ValueError:
		return -1

# Scan 2^11 ports
def scan_port(tgt, prt):
	for p in range(prt, prt+2048):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.001)
		result = s.connect_ex((tgt, p))
		if (result == 0):
			print(f"Port {p}: Open")
			s.close()
			portlist.append(p)
		else:
			#print(f"Port {p}: Closed")
			s.close()


# Main

if __name__ == "__main__":
	global portlist
	portlist = []
	print("Python port scanner\nMade by: @MadlyAbi, edited by: @7654jp")
	target = input("Target IP/Hostname:")

	target_ip = socket.gethostbyname(target)

	print("-" * 32)
	print(f"Scanning Target: {target_ip}")
	print(f"Scanning started at: {str(datetime.now())}")
	print("-" * 32)

	for port in range(0, 32):
		thread = threading.Thread(target=scan_port, args=(target_ip, port * 2048))
		thread.start()
