# Uncomment this to pass the first stage
import socket
import threading


def handle_client(conn, addr):
    while True:
        try:
            # read the data from the client
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.send(b"+PONG\r\n")
        except Exception as e:
            print(e)
            break


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
