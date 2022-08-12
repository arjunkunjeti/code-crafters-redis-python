# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    # while there are still clients connected to the server
    while True:
        # accept a new client connection
        client, _ = server_socket.accept()

        # receive data from the client
        data = client.recv(1024)

        # if the data is not empty
        if data:
            # send data back to the client
            client.send(b"+PONG\r\n")

        # close the client connection
        client.close()

if __name__ == "__main__":
    main()
