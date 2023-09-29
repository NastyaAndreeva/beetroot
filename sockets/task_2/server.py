import socketserver

def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for el in text:
        if el.isalpha():
            shift = ord('A') if el.isupper() else ord('a')
            encrypted_el = chr((ord(el) - shift + key) % 26 + shift)
            encrypted_text += encrypted_el
        else:
            encrypted_text += el
    return encrypted_text

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        message = data.decode('utf-8')

        key = int(input(f"Please, enter the Caesar cipher key for {self.client_address}: "))
        encrypted_message = caesar_cipher_encrypt(message, key)
        socket.sendto(encrypted_message.encode('utf-8'), self.client_address)

if __name__ == "__main__":
    host, port = "127.0.0.1", 12346
    with socketserver.UDPServer((host, port), UDPHandler) as server:
        print(f"UDP server listening on {host}:{port}")
        server.serve_forever()

