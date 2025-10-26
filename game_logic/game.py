from utils.deck import shuffle, create_deck, compare_cards

def create_player(name:str="AI") -> dict:
    player1={}

    player=name
    won_pile=[]
    hand=[]
    player1["name"]=player
    player1["hand"]=hand
    player1["won_pile"]=won_pile
    return player1

def init_game()->dict:
    p1=create_player(input("plaese enter your name:  "))
    p2=create_player()
    deck=(create_deck())
    shuffles=shuffle(deck)

    p1["hand"]=shuffles[:26]
    p2["hand"]=shuffles[26:]

    game={
        "p1":p1,
        "p2":p2,
        "deck":shuffles
        }

    return game

def play_round(p1:dict,p2:dict):
    card_p1=p1["hand"].pop()
    card_p2=p2["hand"].pop()
    round_winner= compare_cards(card_p1,card_p2)
    if round_winner==p1:
        p1["won_pile"].appand
    return None

print(init_game())
