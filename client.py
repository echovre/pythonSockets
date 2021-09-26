from collections import deque
import socket, constants

address = socket.gethostname()
numFiles=0 #TODO: make this a class instead of using global
requests=deque(maxlen=None)
requests.append("/")

def processResult(data, startingDir):
    global numFiles
    dataArray=data.decode().split("\n")
    if dataArray[0]==constants.header: dataArray.pop(0)
    if dataArray[-1]==constants.footer: dataArray.pop(-1)
    for each in dataArray:
        if each.endswith("/"):
            print("Found directory:"+startingDir+each)
            requests.append(startingDir+each)
        elif "file" in each:
            print("Found file:"+startingDir+each+" for total of:"+str(numFiles))
            numFiles=numFiles+1
        else:
            print("ERROR, received:"+each)

def traverse():
    print(len(requests))
    if requests:
        request=requests.popleft()
        print('DIRLIST '+request)
        sock.sendall( ('DIRLIST '+request).encode() )
        data = sock.recv(constants.RECIEVE_SIZE)
        processResult(data, request)
    else:
        print("Done")
        diff=time.time()-start
        print(diff,"seconds")
        exit()

import time
start=time.time()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((address, constants.port))
    """
    startingDir='/'
    sock.sendall( ('DIRLIST '+'/dir_08/').encode() )
    #sock.sendall(b'DIRLIST dir_00/dir_01/dir_99/') #invalid
    data = sock.recv(constants.RECIEVE_SIZE)
    processResult(data, startingDir)
    """

    while True:
        stop=traverse()
        if stop:
            break
 