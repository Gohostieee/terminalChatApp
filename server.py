import socket
import random
from threading import Thread
#incomplete project replace by my flask chat app
#it does show however that i have a good understanding of low level socket handling
cliSock=None

sBind = ('127.0.0.1', 1234)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(sBind)
sock.listen()
sBind = ('127.0.0.1', 1235)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.bind(sBind)
sock2.listen()
clients = {}
looking = []
connect1 = 0
conversations = set()

def connect_cli():
    global cliSock, connect1, looking, clients
    print("what")
    while True:
        if len(looking) > 1:
            print(clients.keys())
            print("uwu1")
            connect1 = looking[0][0]
            connect2 = looking[1][0]
            clients[looking[0][1]]['convos'] = connect2
            clients[looking[1][1]]['convos'] = connect1
            print()
            print(looking)
            conversations.add((connect1, connect2))
            #connect2.send(f'{len(conversations)-1}'.encode('utf-8'))
            connect2.send(f'1'.encode('utf-8'))
            print(connect2)
            connect1.send('1'.encode('utf-8'))
            print(looking,'\n\n\n\n\n\n\n\n\n\n\n',connect1, '\n\n\n\n\n\n\n\n\n\n\n ', connect2)
            del looking [0]; del looking [1]
            print(connect1)
            looking.remove(connect1)
  #  sock.send(connect1.encode('utf-8'))


tCli = Thread(target=connect_cli)
try:
    tCli.start()
except Exception:
    print(Exception)

def init_client(cliSock):
    global clients,msg
    global looking
    msg = msg.decode('utf-8')
    print("dum")
    print("dum")

    print(msg)
    print(cliSock)
    clients[adr[1]] = {'name': msg, 'cli': cliSock, 'full_adr': adr, 'convo': None}
    looking.append((cliSock, adr[1]))
    print(clients)


while True:
    cliSock, adr = sock.accept()
    print(cliSock, adr)

    if adr[1] not in clients:
        cliSock.send(bytes("established connection", 'utf-8'))
        msg = cliSock.recv(164)

        init_client(cliSock)
        continue
    msg = cliSock.recv(164)


    try:

        msg.decode('utf-16')

        cliSock.send('1'.encode('utf-8'))
        print("granite")
    except:
        clients[adr[1]]['convo'].send(f"{clients[adr[1]]['name']}:{msg.decode('utf-8')}")
        pass
