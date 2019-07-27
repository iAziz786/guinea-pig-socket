import socket


s = socket.socket()

s.connect(('192.168.0.102', 9999))

while True:
    print(s.recv(1024))