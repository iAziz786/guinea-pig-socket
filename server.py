import socket

# new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(socket.gethostname())
# new_socket.bind(('192.168.0.102', 9999))

# while True:
#     new_socket.listen(5)

print (socket.create_connection(('https://python.org', 80)))