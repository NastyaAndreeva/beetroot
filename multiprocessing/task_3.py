import socket
import multiprocessing

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def handle_client_connection(client_socket):
    try:
        print(f"Accepted connection from {client_socket.getpeername()}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break 
            print(f"Received: {data.decode()}")
            client_socket.send(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)

    print(f"Listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        client_socket, client_addr = server_socket.accept()
        client_process = multiprocessing.Process(target=handle_client_connection, args=(client_socket))
        client_process.start()

if __name__ == '__main__':
    main()
