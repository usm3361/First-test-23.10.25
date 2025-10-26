import random
SUITES=["H","C","D","S"]
RANKS=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def create_card(suite:str, rank:str) -> dict:

    dict_card={}
    dict_card["suite"]=suite
    dict_card["rank"]=rank
    special_rank={
        "J":11,
        "Q":12,
        "K":13,
        "A":14
        }
    
    try:
        dict_card["value"]=(int(rank))
    except ValueError:
        dict_card["value"]=special_rank[rank]
      
    return dict_card

def create_deck()-> list[dict]:
    cards=[]
    for s in SUITES:
        for r in RANKS:
            cards.append(create_card(s,r))

    return cards 
    
    
def shuffle(deck:list[dict])-> list[dict]:

    for _ in range(1000):
        index_card1=random.randint(0,51)
        index_card2=random.randint(0,51)
        if index_card1 == index_card2:
            continue
        else: 
            deck[index_card1] , deck[index_card2] = deck[index_card2] , deck[index_card1]

    return deck


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    p1_card=["value"]
    p2_card=()
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p1"
    return "war"

print(shuffle(create_deck()))