import socket
import threading

SERVER_IP = "192.168.1.81"   # Change this to Windows server IP
PORT = 5000

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                print("\nServer disconnected.")
                break

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except:
            print("\nConnection lost.")
            break


# Create socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to server
print(f"Connecting to {SERVER_IP}:{PORT}...")

client.connect((SERVER_IP, PORT))

print("Connected to server!")
print("Type your message.")
print("Type 'exit' to leave.")


# Start receiving thread
thread = threading.Thread(target=receive_messages,daemon=True)

thread.start()


# Send messages
while True:

    message = input("You: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())


client.close()
print("Disconnected.")