import socket

HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the insurance server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the insurance server
client_socket.connect((HOST, PORT))

customer_name = input("Enter customer name: ")

# Convert string to bytes and send
client_socket.sendall(customer_name.encode("utf-8"))

# Receive server response
data = client_socket.recv(1024)

print("Server response: ", data.decode("utf-8"))

# Close the connection
client_socket.close()
