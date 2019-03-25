import threading
import socket

HOST = "127.0.0.1"
PORT = 50000
global s

def recieve(conn):
    while True:
        data=conn.recv(1024)
        if not data:
            break
        print(data)



def main():
    global s
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    T=threading.Thread(target=recieve,args=(s,))
    T.start()
    ID=input("請輸入ID：")
    s.send(str.encode("ID_register"))
    s.send(str.encode(ID))

if __name__=="__main__":
    main()