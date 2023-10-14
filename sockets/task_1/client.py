import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter a message to send to the server (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break

    data = message.encode('utf-8')
    client_socket.sendto(data, (HOST, PORT))

client_socket.close()
