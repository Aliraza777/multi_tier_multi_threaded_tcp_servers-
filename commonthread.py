from threading import Thread
import socket
import time
import pickle


SCHEME = "utf-8"

servers = {
    1 : ['127.0.0.1' , 2223] , 
    2 : ['127.0.0.1' , 2224] , 
    3 : ['127.0.0.1' , 2225] , 
}



class CommonThread(Thread):
    def __init__(self,clientsocket):
        Thread.__init__(self)
        self.clientsocket = clientsocket

    def run(self):
        s = socket.socket()
        print("Client Thread Started ... ")
        choice = self.clientsocket.recv(1024)
        choice = choice.decode(SCHEME)
        if(choice == "1"):
            for x , y in servers.items():
                if x == 1:
                    addr , port = y
                    s.connect((addr, port))
                    s.send("hello server1".encode(SCHEME))
                    name = self.clientsocket.recv(1024)
                    name = name.decode(SCHEME)
                    s.send(name.encode(SCHEME))
                    retn = s.recv(1024)
                    retn = retn.decode(SCHEME)
                    self.clientsocket.send(retn.encode(SCHEME))
        elif(choice == "2"):
            for x , y in servers.items():
                if x == 2:
                    addr , port = y
                    s.connect((addr, port))
                    s.send("hello server2".encode(SCHEME))
                    name = self.clientsocket.recv(1024)
                    name = name.decode(SCHEME)
                    s.send(name.encode(SCHEME))
                    retn = s.recv(1024)
                    retn = retn.decode(SCHEME)
                    self.clientsocket.send(retn.encode(SCHEME))
        elif(choice == "3"):
            for x , y in servers.items():
                if x == 3:
                    addr , port = y
                    s.connect((addr, port))
                    s.send("hello server3".encode(SCHEME))
                    name = self.clientsocket.recv(1024)
                    name = name.decode(SCHEME)
                    s.send(name.encode(SCHEME))
                    retn = s.recv(4096)
                    length = pickle.loads(retn)
                    print(length)
                    data = pickle.dumps(length)
                    self.clientsocket.send(data)
        else:
            print("Error Encountered")
        self.clientsocket.close()