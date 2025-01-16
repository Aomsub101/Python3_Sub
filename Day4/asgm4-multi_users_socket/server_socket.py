"""Server socket"""

import socket
import sys
import threading
# from pyexpat.errors import messages

HOST = '0.0.0.0' # accept connections from any IP
PORT = 12345 # port to listen on
s = None

class Client:
    """
    Client class
    """
    def __init__(self, connected_socket, client_id):
        self.connected_socket = connected_socket
        self.client_id = client_id

clients = []

def send_message_function(client_socket):
    while True:
        message = input("Enter message: ")
        client_socket.send((message+"\n").encode())

def broadcast_message(message, author):
    """
    For broadcasting message to all users
    """
    for client in clients:
        if client.client_id != author.client_id:
            try:
                client.connected_socket.send((message + "\n").encode())
            except:
                print(f"Sorry, client {client.client_id} looks broken!")

def handle_client_communication(client):
    while True:
        send_thread = threading.Thread(target=send_message_function, args=(conn,))
        send_thread.start()

        message_received = ''

        while True:
            data = conn.recv(1024)
            if data:
                if data.decode() == 'exit\n':
                    break
                print('Received data chunk from client: ', repr(data))
                message_received += data.decode()
                if message_received.endswith('\n'):
                    break
            else:
                print('Connection lost!')
                break

        if message_received:
            print('Received message: ', message_received)
            broadcast_message(message_received, client)
        else:
            break

# create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
except OSError as msg:
    s = None
    print(f'Error creating socket: {msg}')
    sys.exit(1)

# bind and listen
try:
    s.bind((HOST, PORT))
    s.listen()
    print('Socket bound and listening')
except OSError as msg:
    print('Error binding/listening!')
    s.close()
    sys.exit(1)

while True:
    conn, addr = s.accept()
    cli = Client(conn, len(clients))
    clients.append(cli)
    cli_thread = threading.Thread(target=handle_client_communication, args=(cli, ))
    cli_thread.start()

s.close()
print("server finished")