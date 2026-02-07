import socket


target = input("Enter target IP: ")
print(f"Scanning {target}...\n")
for port in range(8000, 8100):
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.2)

	result = s.connect_ex((target, port))

	if result == 0:
		print(f"Port {port} is OPEN")
s.close()
print("\nScan complete.")
