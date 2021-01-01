import socket
import threading

ip = "127.0.0.1"      # Local host

port = 55555          # take any port which is not used for any other resourrces

# Internet addr i.e ipv4 and scoket stream i.e tcp.

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss.bind((ip, port))     # binding socket with (ip address and port)

ss.listen()             # listening server for requests from clients

clients = []            # list  of clients
nicknames = []          # nickname of the client to show on the chat


def broadcast(message):                              # send message to each and every client
    for client in clients:
        client.send(message)


def handle(client):                                  # handle every client
    while True:
        try:
            message = client.recv(1024)               # receiving message from one client and broadcast to all other clients
            broadcast(message)
        except:                                         # If client disconnected then we remove client and his nickname and terminates using break.
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():                                                # It is initial function which is called
    while True:
        client, address = ss.accept()                           # It accepts client connection
        print(f"Connected with {str(address)}")

        client.send("NICK".encode('ascii'))

        nickname = client.recv(1024).decode('ascii')             # Nickname is entered and send by client side and it is received
        nicknames.append(nickname)
        clients.append(client)                                   # adding client and nickname to lists

        print(f"Nickname of the client is {nickname}!")

        broadcast(f"{nickname} Joined the chat!".encode('ascii'))              # sends message to every client

        client.send("Connected to server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))           # creates thread for each and every client using handle function.

        thread.start()


print("Server is Listening...")                 # Our server will start by printing this and then
receive()                                       # calls this function
