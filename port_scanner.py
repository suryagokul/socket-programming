import socket
from queue import Queue
import threading

target_ip = "192.168.0.1"


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        return True
    except:
        return False


"""for port in range(1, 1024):
    result = portscan(port)
    if result:
        print(f"port {port} is opened")
    else:
        print(f"port {port} is closed ")
"""

queue = Queue()
open_ports = []


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"port {port} is opened")
            open_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for i in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are ", open_ports)




