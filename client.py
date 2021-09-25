from collections import deque
import socket, constants

address = socket.gethostname()

numFiles=0
requests=deque(maxlen=None)
requests.append("/")

def traverse(data, startingDir):
    dataArray=data.decode().split("\n")
    if dataArray[0]==constants.header: dataArray.pop(0)
    if dataArray[-1]==constants.footer: dataArray.pop(-1)
    for each in dataArray:
        if each.endswith("/"):
            requests.append(startingDir+each)
            print("Found directory:"+startingDir+each)
        elif "file" in each:
            numFiles=numFiles+1
            print("Found file:"+startingDir+each+" for total of:"+numFiles)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((address, constants.port))
    startingDir='/'
    sock.sendall( ('DIRLIST '+startingDir).encode() )
    #sock.sendall(b'DIRLIST dir_00/dir_01/dir_99/') #invalid
    data = sock.recv(constants.RECIEVE_SIZE)
    traverse(data, startingDir)