
import threading
import socket
from client_handling import client_handler
from colors import *

HOST = '0.0.0.0'
PORT = 65000

print(CRED+"---------------------------------------------"+CEND)
print(CGREEN+" SMADECT, The Art of IOT"+CEND)
print(CYELLOW+"Created by medabkasm"+CEND)
print("github : https://github.com/medabkasm")
print("email : medabkasm@gmail.com")
print(CRED+"---------------------------------------------"+CEND)


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as serverSocket:
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ensuer reusability of socket connection
        serverSocket.bind((HOST,PORT)) # bind the socket to the specified host,port
        serverSocket.listen() # listen to the clients(ESP)
        serverSocket.settimeout(360) # timeout for 6 minutes
        while True:
            try:
                clientConnection , clientAddress = serverSocket.accept() # accepting the ESP connection
                # handle the client
                clientThread = threading.Thread(target = client_handler , args = (clientConnection,clientAddress) )
                clientThread.start()

            except Exception as err:
                print(CRED+"Error :: during handling threads / clients :: {}".format(str(err))+CEND)
                clientConnection.close()
