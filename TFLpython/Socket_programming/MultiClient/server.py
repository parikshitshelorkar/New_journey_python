import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def handle_client(client_socket, client_address):
    print("Client Connected: ", client_address)

    try :
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print("Received: ", message)
            response = f"Server received: {message}"

            client_socket.sendall(response.encode("utf-8"))

    finally:
        client_socket.close()
        print("Disconnected: ", client_address)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True)
        client_thread.start()
except KeyboardInterrupt:
    print("\nServer stopped")
finally:
    server_socket.close()
