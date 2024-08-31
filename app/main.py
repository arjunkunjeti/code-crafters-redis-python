# Uncomment this to pass the first stage
import socket
import threading
import re

dic = {}

def handle_client(conn, addr):
    while True:
        try:
            # read the data from the client
            data = conn.recv(1024)
            if not data:
                break
            ret = parse_command(data)
            print(ret)
            conn.send(ret)
        except Exception as e:
            print(e)
            break

def parse_command(data):
    # parse RESP command
    # bytes to string
    data = data.decode("utf-8")
    if data[0] == "*":
        # split by \r\n
        x = re.split(r"\r\n", data)
        print(x)
        for idx,s in enumerate(x):
            if(s == ""):
                continue
            if s == "PING" or s == "ping":
                return b"+PONG\r\n"
            if s == "ECHO" or s == "echo":
                return f"+{x[idx+2]}\r\n".encode()
            if s == "SET" or s == "set":
                dic[x[idx+2]] = x[idx+4]
                return f"+OK\r\n".encode()
            if s == "GET" or s == "get":
                return f"+{dic[x[idx+2]]}\r\n".encode()

            if s == "$":
                print(f"{s[1:]} chars coming in")
            if s[0] == "*":
                print(f"{s[1:]} commands coming in")
            if s[0] == "+":
                print(f"{s[1:]} is the command")
    pass




def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # create an event loop
    while True:
        # HANDLe multiple connections
        conn, addr = server_socket.accept()
        print("Connected to", addr)
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    main()
