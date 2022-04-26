import json
import asyncio
import time

import socket
import threading
import sys

port = sys.argv[1]
listenAddress = ('0.0.0.0', int(port))
text={
   "request": "subscribe",
   "port": 3001,
   "name": "CKC",
   "matricules": ["20253", "21306"]
}

text2={
   "request": "subscribe",
   "port": 3002,
   "name": "CAVA",
   "matricules": ["20252", "21305"]
}

repPing = {"response": "pong"}

#repMove['move'] = null pour passer le tour
repMove = {
    "response": "move",
    "move": 0,
    "message": "Un aveugle jouerais mieux que toi"
}

surrend={
   "response": "giveup",
}

def communication():
    with socket.socket() as s:
        s.bind(listenAddress)
        s.listen()
        while True:
            client, address= s.accept()
            with client:
                message = json.loads(client.recv(2048).decode())
                print(message)
                if message['request']=='ping':
                    client.send(json.dumps(repPing).encode())
                if message['request']=='play':
                    print(message['state']['board'][0])
                    #client.send(json.dumps(surrend).encode())
                    print(message['state']['board'][0]==[28, 35])
                    if message['state']['board'][0]==[28, 35]:
                        repMove['move']=44
                        print(repMove)
                        client.send(json.dumps(repMove).encode())


def connexion():
    address = ('localhost', 3000)
    message = json.dumps(text)
    
    with socket.socket() as s:
        s.connect(address)
        s.send(message.encode())
        reponse = json.loads(s.recv(2048).decode())
        if reponse['response'] == 'ok':
            communication()
        
        
            

if __name__=='__main__':
    if port == '3002':
        text=text2
    connexion()
