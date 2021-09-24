import socket

HEADERSIZE = 10
address = socket.gethostname()
port = 1024

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("connecting...")
sock.connect((address, port))

while True:
  msg = sock.recv(HEADERSIZE)
  result=msg.decode("utf-8")
  print(result)
  if(result=="END"):
    break

sock.close()

#https://pythonprogramming.net/buffering-streaming-data-sockets-tutorial-python-3/?completed=/sockets-tutorial-python-3/