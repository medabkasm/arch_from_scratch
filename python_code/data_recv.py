import json
from datetime import datetime
from colors import *


class DataReceiver:

    def __init__(self,clientConnection):
        self.clientConnection = clientConnection

    def simple_recv(self):
        try:
            data = self.clientConnection.recv(1024)
            return data
        except Exception as err:
            print(CRED+"Error :: error with receiving data from client : {}".format(str(err))+CEND)
            self.clientConnection.close()
            return -1

    
