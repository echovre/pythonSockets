import socket

HEADERSIZE = 10

port = 1024 #min port without privilege
#address = '' #requests from others on network
address=socket.gethostname()

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("binding to port %s" %(port))
sock.bind((address, port))

print("listening...")
sock.listen(5)

header = "HELLO"
header = f"{len(header):<{HEADERSIZE}}"+header

connection, clientAddress = sock.accept()
print ('Got connection from', clientAddress)
connection.send(bytes(header,"utf-8"))
connection.send(bytes("hello blah blha","utf-8"))
connection.send(bytes("END","utf-8"))
connection.close()
