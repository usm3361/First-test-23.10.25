from utils.deck import shuffle

def create_player(name:str) -> dict:
    player1={}

    player=name
    won_pile=[]
    hand=[]
    player1["name"]=player
    player1["hand"]=hand
    player1["won_pile"]=won_pile
    return player1

def init_game()->dict:
    init_play={}
    p1=create_player(input("plaese enter your name:  "))
    p2=create_player("AI")
    deck=shuffle()

    init_play["p1"]=p1
    init_play["p2"]=p2
    init_play["deck"]=deck

    return init_play

def play_round(p1:dict,p2:dict):

    return None