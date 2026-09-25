import socket

HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(1)
print(f"Insurance Server is listening on {HOST} : {PORT}")

# Accept one client connection
client_socket, client_address = server_socket.accept()
print("Client connected: ", client_address)

# Receive data from client
data = client_socket.recv(1024)

customer_name = data.decode("utf-8")
print("Customer name: ", customer_name)

# Sends response to client
response = f"Hello {customer_name}, welcome to TFL Insurance!"
client_socket.sendall(response.encode("utf-8"))

# Close the client and server sockets
client_socket.close()
server_socket.close()

print("Server Stopped")

