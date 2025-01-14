import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4646        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'GET / HTTP/1.1\r\nHost: test.net\r\n\r\n')
    s.send(b'Hi from client')
    data = s.recv(1024)
    print('Received', repr(data))
