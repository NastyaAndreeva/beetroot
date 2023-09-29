import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP server listening on {HOST}:{PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode('utf-8')
    print(f"Received from {client_address}: {message}")
server_socket.close()
