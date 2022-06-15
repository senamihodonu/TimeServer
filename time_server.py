import socket
import threading
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
LOCAL_TIME = "localtime"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind to an address
server.bind(ADDR)

def local_time():
    """returns the local time"""
    t = time.asctime(time.localtime())
    return f"local time is {t}"

def handle_client(conn, addr):
    """handles each client connection"""
    print(f"[NEW CONNECTIONS] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) 
            if msg == DISCONNECT_MESSAGE:
                connected = False
            if msg == LOCAL_TIME:
                print(f"[{addr}] {msg} request")
                conn.send(local_time().encode(FORMAT))
        conn.send(f"{msg} request received".encode(FORMAT))
    conn.close()
    

def start():
    """handles new connections"""
    try:
        server.listen()
        print(F"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr = server.accept() #blocking
            thread = threading.Thread(target=handle_client,args=(conn, addr))
            thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_Count() - 1}")
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
        print ('Shutting down program')
        time.sleep(2)
        print ('Goodbye :)')

print(f"[STARTING] server is starting...")
start()

