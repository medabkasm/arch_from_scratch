
from colors import *
import json


class Command:

    def __init__(self,clientConnection):
        self.clientConnection = clientConnection

    def simple_exec(self): # private methode
        try:
            self.clientConnection.send("EXC".encode("ascii"))
        except Exception as err:
            print(CRED+"Error :: while sending EXC flag : {}".format(str(err))+CEND)
            self.clientConnection.close()
            return -1

        data = self.clientConnection.recv(1024).decode().strip("\r\n")
        if data and ("CNF" in data):
            try:
                print(CGREEN+"order executed successfully"+CEND)
                self.clientConnection.send("RECV".encode("ascii"))
                self.clientConnection.close()
                return True
            except Exception as err:
                print(CRED+"Error :: while sending RECV flag : {}".format(str(err))+CEND)
                self.clientConnection.close()
                return False
        elif data and ~("CNF" in data):
            print(CYELLOW+"# WARNING: missing CNF flag in - {} - data".format(data))
            self.clientConnection.close()
        else:
            print(CRED+"Error :: no data or execution_confirmation received"+CEND)
            self.clientConnection.close()
            return -2 # no data received


    
