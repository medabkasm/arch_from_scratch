import socket # for main program
from colors import *



class Connection:

    def __init__(self,HOST,PORT):
        self.HOST = HOST
        self.PORT = PORT

    def test_server_connectivity(self):
        try:
            serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ensuer reusability of socket connection
            serverSocket.connect((self.HOST,self.PORT))
            print(CGREEN+"server is alive"+CEND)
            return serverSocket
        except Exception as err:
            print(CRED+"Error :: while creating the socket object : {}".format(str(err))+CEND)
            return 0

    def _hand_shake(self,serverSocket):
        try:
            # begin the handshake between the server and the client to start receiving data
            data = serverSocket.recv(1024).decode().strip("\r\n")
            if "STR" in data:
                print(CGREEN+"connection with the client begins"+CEND)
                serverSocket.send("STR".encode("ascii"))
                data = serverSocket.recv(1024).decode().strip("\r\n")
                if "EST" in data:
                    print(CGREEN+"connection with the client is established"+CEND)
                    return serverSocket
                else:
                    print(CRED+"Error :: bad EST flag"+CEND)
                    serverSocket.close()
                    return -1
            else:
                print(CRED+"Error :: bad STR flag"+CEND)
                serverSocket.close()
                return -2
        except Exception as err:
            print(CRED+"Error :: handshake error : {}".format(str(err))+CEND)
            if serverSocket:
                serverSocket.close()
            return -3


    def begin(self):
        serverSocket = self.test_server_connectivity()
        if isinstance(serverSocket,socket.socket):
            if isinstance(self._hand_shake(serverSocket),socket.socket):
                return serverSocket

        return False
