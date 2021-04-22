#import socket
from connection import *
from datetime import datetime
from time import sleep
from data_recv import DataReceiver
from command_exec import Command


def client_handler(clientConnection,clientAddress):
    conn = Connection(clientAddress[0],clientAddress[1])
    print("-------------------------------------------------------")
    print("connection accepted at : {}".format(datetime.now()))
    print("IP : {}".format(clientAddress[0]))
    print("PORT : {}".format(clientAddress[1]))
    if isinstance(conn._hand_shake(clientConnection),socket.socket):
        dataRecv = DataReceiver(clientConnection)
        cmdExc = Command(clientConnection)
        
