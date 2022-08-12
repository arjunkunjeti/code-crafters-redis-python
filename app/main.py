# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    (client_socket, address) = server_socket.accept()
    client_socket.send(b"+PONG\r\n")
    
    server_socket.accept() # wait for client

    # while True:
    #     client_socket, address = server_socket.accept()
    #     client_socket.send(b"Hello, world!")
    #     client_socket.close()
if __name__ == "__main__":
    main()
