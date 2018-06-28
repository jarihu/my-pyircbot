import socket as Socket
import sys
import time
class Server:
    def __init__(self, name, port, network):
        self.name = name
        self.port = port
        self.nickName = ""
        self.network = network
        self.serverSocket = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
        #self.serverSocket.settimeout(5)
        self.channels = []

    def connect(self):
        print(self.name + " connecting to server...")
        self.serverSocket.connect((self.name, self.port))
        data = ""
        max_retries = 15
        tries = 0
 #       while True:
 #           try:
        data = self.serverSocket.recv(2048).decode("UTF-8").strip('\n\r')
#                if len(data) > 0:
#                    print(time.time +  " log:" + data)
#                if data.find("MOTD") != -1:
#                    print(self.name + " CONNECTED!")
#                    break
#            except Socket.timeout:
#                print("retrying...")
#                if tries > max_retries:
#                    print("connect error")
#                    return
#                tries += 1

    def read(self):
        try:
            data = self.serverSocket.recv(2048).decode("UTF-8").strip('\n\r')
            return data
        except Socket.timeout:
            return ""

    def ping(self): 
        self.serverSocket.send(bytes("PONG :pingis\n", "UTF-8"))

    def joinChannel(self, channel):
        self.serverSocket.send(bytes("JOIN "+ channel +"\n", "UTF-8")) 
        self.channels.append(channel)

    def sendMessage(self, message, targets):
        for target in targets:
            print("sending message")
            self.serverSocket.send(bytes("PRIVMSG "+ target +" :"+ message +"\n", "UTF-8"))

    def sendCommand(self, command, parameter):
        self.serverSocket.send(bytes(command.upper() + " " + parameter + "\n", "UTF-8"))
        return self.serverSocket.recv(2048).decode("UTF-8")
        
    def setNickName(self, nickName):
        self.serverSocket.send(bytes("USER "+ nickName +" "+ nickName +" "+ nickName + " " + nickName + "\n", "UTF-8"))
        self.serverSocket.send(bytes("NICK "+ nickName +"\n", "UTF-8")) 
        self.nickName = nickName
