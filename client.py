from commonthread import SCHEME
import socket
import pickle


ADDRESS = '127.0.0.1'

PORT = 2222


c = socket.socket()

c.connect((ADDRESS,PORT))

print("Connected with server successfully \n")

print(" Press 1 for echo service  \n Press 2 for palidrome service \n Press 3 for checking length service  \n---------------------------------------\n")
choice = input("Enter Choice :  ")

if(choice == "1"):
    #sending choice
    c.send(choice.encode(SCHEME))
    name = input("Enter Name to be achoed : ")
    c.send(name.encode(SCHEME))
    ret = c.recv(1024)
    print("From Server : ", ret.decode(SCHEME))
elif(choice == "2"):
    #sending choice
    c.send(choice.encode(SCHEME))
    name = input("Enter String to see palidrome : ")
    c.send(name.encode(SCHEME))
    ret = c.recv(1024)
    print("From Server : ", ret.decode(SCHEME))
elif(choice == "3"):
        #sending choice
    c.send(choice.encode(SCHEME))
    name = input("Enter String to calculate length: ")
    c.send(name.encode(SCHEME))
    ret = c.recv(1024)
    length = pickle.loads(ret)
    print("From Server : ", length)
else:
    print("Invalid choice")