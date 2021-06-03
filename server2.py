from commonthread import SCHEME
import socket
from threading import Thread
from commonthread import CommonThread


ADDRESS = "127.0.0.1"

PORT = 2224

def main():
    s = socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    print("Listening for main server ...")
    while True:
        c , addr = s.accept()
        print("Server 2 started :  "  , addr)
        hello = c.recv(1024)
        hello = hello.decode(SCHEME)
        print(hello)
        name = c.recv(1024)
        name = name.decode(SCHEME)
        w = ""
        for i in name:
            w = i + w
         
        if (name == w):
            print("Its palidrome")
            c.send("Yes".encode(SCHEME))
        else:
            print("Not palidrome")
            c.send("No".encode(SCHEME))
        
        
if __name__ == "__main__":
    main()