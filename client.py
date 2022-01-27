import socket
from threading import Thread
#incomplete project replace by my flask chat app
#it does show however that i have a good understanding of low level socket handling
print("what")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("what")
sock.connect(('127.0.0.1', 1234))
print("what")
msg = sock.recv(1024)
print("what")
print(msg.decode('utf-8'))
msg = input("Enter username:").encode('utf-8')
sock.send(msg)
connections = 0
sent = 0
def send_message():
    global sock
    sock.send(input("enter message:").encode('utf-8'))
    print("opfsu")

Tsend = Thread(target=send_message)

while True:
    print(connections, sent)
    if not connections and not sent:
        sock.send("kekw".encode('utf-16'))
        sent = sock.recv(50).decode()
        print(sent)
        sent=int(sent)
        print("kay")
    elif not connections and sent:
        print()
        connections = int(sock.recv(124).decode('utf-8'))
        print("uwwu")

    elif connections == 1:
        connections = 2
        print("what")
    else:
        sock.recv(124).decode('utf-8')

    print("what outside")
    print(connections, sent)
