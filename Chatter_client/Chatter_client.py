import threading
import socket


HOST = "127.0.0.1"
PORT = 50000
global s

def recieve(conn):
    while True:
        try:
            data=conn.recv(1024)
            if not data:
                break
            print(str(data,encoding="utf-8"))
        except:
            print("\n連線失敗")
            break



def main():
    global s
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((HOST,PORT))
        T=threading.Thread(target=recieve,args=(s,))
        T.start()
        ID=input("請輸入ID：")
        s.send(str.encode("ID_register"))
        s.send(str.encode(ID))
        while True:
            message=input("若想查詢自身IP，請輸入\myip，若想查詢對方ip，請輸入\herip\n請輸入訊息:\n")
            s.send(str.encode(message))
    except:
        print("\n連線失敗")

if __name__=="__main__":
    main()