import socket

HEADERSIZE = 10

port = 1024 #min port without privilege
address=socket.gethostname()
sock = socket.socket()
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect((socket.gethostname(), 1024))

while True:
    full_msg = ''
    new_msg = True
    while True:
        message = sock.recv(16)
        if new_msg:
            print("new msg len:",message[:HEADERSIZE])
            messagelength = int(message[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {messagelength}")

        full_msg += message.decode("utf-8")

        print(len(full_msg))

        print(full_msg)

        if len(full_msg)-HEADERSIZE == messagelength:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True


#https://pythonprogramming.net/buffering-streaming-data-sockets-tutorial-python-3/?completed=/sockets-tutorial-python-3/