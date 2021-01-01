import socket
import threading

ip = "127.0.0.1"

port = 55555

nickname = input("Enter a nickname > ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip, port))                  # Connecting to server


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')                # server sends NICK message which is receiving here
            if message == "NICK":
                client.send(nickname.encode('ascii'))                  # sending nickname to server
            else:
                print(message)
        except:
            print("Error Occured!")                                     # If any issues occurs in client side then closes connection
            client.close()
            break


def write():                                                           # this function is used to shows name and message who is sending and receiving.
    while True:
        message = f'{nickname} : {input("")}'                          # for ex  surya : hi, bunny
        client.send(message.encode('ascii'))                           # bunny : hello,surya


receive_thread = threading.Thread(target=receive)                      # creating separate thread for receive and write functions as shown below
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
