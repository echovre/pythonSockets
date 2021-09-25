import socket, constants

address = socket.gethostname()
#address = '' #requests from others on network

#function contract: spaces in directory path will be ignored
def handleCommand(data):
    if " " in data: print("WARNING: space in directory path:",data)
    if data.startswith("/"): data=data.lstrip("/")
    if data.endswith("/"): data=data.rstrip("/")

    dirsArray=data.split("/")
    if len(dirsArray)<3:
        return generateResponse(returnDirectoryListing())
    elif len(dirsArray)==3:
        return generateResponse(returnFileListing())
    else:
        return returnNothing()

def returnNothing():
    #return header+"\n"+footer
    return "ERROR: invalid command, check that your path begins with root /"

def generateResponse(listingArray):
    response = constants.header+"\n"
    for each in listingArray:
        response += each+"\n"
    response += constants.footer
    return response

def returnDirectoryListing():
    listing=[]
    for i in range(0,constants.NUM_DIRECTORIES):
        numString = str(i) if i>9 else "0"+str(i)
        listing.append("dir_"+numString+"/")
    return listing

def returnFileListing():
    return ["file_01",
            "file_02",
            "file_03"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((address, constants.port))
    print("listening on port %s" %(constants.port))
    sock.listen()
    connection, addr = sock.accept()
    with connection:
        print(addr, "is connected!")
        while True:
            data = connection.recv(constants.RECIEVE_SIZE).decode("utf-8")
            print("Received:",data)
            if not data:
                break
            elif ("DIRLIST /" in data):
                result=handleCommand(data.split(" ",1)[1])
                connection.sendall(result.encode())
            else:
                print("Received invalid command:",data)
                connection.sendall(returnNothing().encode())