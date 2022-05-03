import json
import asyncio
import time
#import ia
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

#repMove['move'] = none pour passer le tour
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
                    reponseMove = ia.test(message['state'],text['name']) #donner le chiffre de la case en integer
                    repMove['move']=reponseMove
                    client.send(json.dumps(repMove).encode())
                    # print(message['state']['board'][0])
                    # #client.send(json.dumps(surrend).encode())
                    # print(message['state']['board'][0]==[28, 35])
                    # if message['state']['board'][0]==[28, 35]:
                    #     repMove['move']=44
                    #     print(repMove)
                    #     client.send(json.dumps(repMove).encode())
def boardConvertion(message):
    plateau = message['board']
    boardConverted=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for i in plateau[0]:
        x=i//8
        y=i-(8*x)
        boardConverted[x][y]='X'
    for i in plateau[1]:
        x=i//8
        y=i-(8*x)
        boardConverted[x][y]='O'
    print(boardConverted[0][0])
    return boardConverted

def findOpponentMove(boardConverted,board):
    opponentMove =''
    for i in range(8):
        for j in range(8):
            if boardConverted[i][j]!='' & board[i][j]=='':
                opponentMove = str(i)+str(j)

def findOpponentTurn(message, iaPlayer):
    if message['players'][0]==iaPlayer:
        return 'computer' # ia joue en premier
    else:
        return 'opponent' # ia joue en deuxieme



def connexion():
    address = ('localhost', 3000)
    message = json.dumps(text)
    
    with socket.socket() as s: # close the socket after the execution
        s.connect(address)
        s.send(message.encode())
        reponse = json.loads(s.recv(2048).decode())
        if reponse['response'] == 'ok': # if the response is ok, it means that we succesfull connected so run communication
            communication()
        
        
            
message ={'players': ['CAVA', 'CKC'], 'current': 1, 'board': [[28, 35, 44, 36], [27]]}
if __name__=='__main__':
    # if port == '3002':
    #     text=text2
    # connexion()
    boardConvertion(message)