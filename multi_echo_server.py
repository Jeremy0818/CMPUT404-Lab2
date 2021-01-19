#!/usr/bin/env python3
from multiprocessing import Pool
from multiprocessing import Process
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_helper(conn, addr):
    print("Handling: ", addr)
    #recieve data, wait a bit, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    print(full_data)
    time.sleep(0.5)
    conn.sendall(full_data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            print(conn)
            p = Process(target=handle_helper, args=(conn, addr))
            p.daemon = True
            p.start()
            print("Started process ", p)
            conn.close()
        s.close()

if __name__ == "__main__":
    main()