import json
import asyncio
import time
import ia_v2
import socket
import threading
import sys

port = sys.argv[1]
listenAddress = ("0.0.0.0", int(port))
text={
   "request": "subscribe",
   "port": int(port),
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

#repMove['move'] = None pour passer le tour
repMove = {
    "response": "move",
    "move": 0,
    "message": "Un aveugle jouerais mieux que toi"
}

surrend={
   "response": "giveup",
}

def communication():
    with socket.socket() as s: # close the socket after the execution
        s.bind(listenAddress)
        s.listen()
        while True: # infinit loop
            client, address= s.accept()
            with client: # close the client after the execution
                message = json.loads(client.recv(2048).decode())
                print(message) #{'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['CAVA', 'CKC'], 'current': 1, 'board': [[28, 35, 44, 36], [27]]}}
                if message['request']=='ping': #check if the request is ping send a pong message
                    client.send(json.dumps(repPing).encode())

                if message['request']=='play':
                    reponseMove = ia_v2.getMessage(message['state'],text['name']) #get the state from message and the name of our ia
                    repMove['move']=reponseMove
                    if reponseMove == None : #just for fun if when can't play change the message associated
                        repMove['message']='Mouais, la chance du débutant'
                    client.send(json.dumps(repMove).encode())


def connexion():
    address = ('localhost', 3000) #192.168.43.178
    message = json.dumps(text)
    
    with socket.socket() as s: # close the socket after the execution
        s.connect(address)
        s.send(message.encode())
        reponse = json.loads(s.recv(2048).decode())
        print(reponse)
        if reponse['response'] == 'ok': # if the response is ok, it means that we succesfull connected so run communication
            communication()



if __name__=='__main__':
    # if port == '3002':
    #     text=text2
    connexion()