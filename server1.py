from commonthread import SCHEME
import socket
from threading import Thread
from commonthread import CommonThread


ADDRESS = "127.0.0.1"

PORT = 2223

def main():
    s = socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    print("Listening for main server ...")
    while True:
        c , addr = s.accept()
        print("Server 1 started :  "  , addr)
        tname = c.recv(1024)
        tname = tname.decode(SCHEME)
        print(tname)
        name = c.recv(1024)
        name = name.decode(SCHEME)
        print("Name to be echoed is :  ",name)
        c.send(name.encode(SCHEME))
        
        # c.send(name.encode(SCHEME))

if __name__ == "__main__":
    main()