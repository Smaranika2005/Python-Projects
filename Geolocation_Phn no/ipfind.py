import socket

hostname=socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"here is my {ip_address}")