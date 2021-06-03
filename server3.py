from commonthread import SCHEME
import socket
from threading import Thread
from commonthread import CommonThread
import pickle

ADDRESS = "127.0.0.1"

PORT = 2225

def main():
    s = socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    print("Listening for main server ...")
    while True:
        c , addr = s.accept()
        print("Server 3 started :  "  , addr)
        tname = c.recv(1024)
        tname = tname.decode(SCHEME)
        print(tname)
        name = c.recv(1024)
        name = name.decode(SCHEME)
        length = len(name)
        print("Length of String is : " , length)
        data = pickle.dumps(length)
        c.send(data)
        
        # c.send(name.encode(SCHEME))

if __name__ == "__main__":
    main()