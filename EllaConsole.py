import socket

from Projects.EllaConsole.PrintFunctions import Print

UDP_IP = "127.0.0.1"
UDP_PORT = 515

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((UDP_IP, UDP_PORT))


while True:

    data = None
    try:
        data, addr = sock.recvfrom(100*1024) # buffer size is 1024 bytes
    except:
        data = "[error]:" + "Message is bigger than buffer"

    concatString = ""

    data = str(data)[2:-1]
    Print(data)


