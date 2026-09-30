import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                pass


def handle_client(client, address):

    print(f"Connected: {address}")

    clients.append(client)

    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(f"{address}: {message}")

            broadcast(
                f"Client {address}: {message}",
                client
            )

        except:
            break

    clients.remove(client)
    client.close()

    print(f"Disconnected: {address}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

print(f"Server listening on port {PORT}")

while True:

    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()

    print(f"Active clients: {len(clients)}")