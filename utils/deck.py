import random
def create_card(suite:str, rank:str) -> dict:

    dict_card={}
    dict_card["suite"]=suite
    dict_card["rank"]=rank
    if rank=="2":
        dict_card["value"]=2
    elif rank=="3":
        dict_card["value"]=3
    elif rank=="4":
        dict_card["value"]=4
    elif rank=="5":
        dict_card["value"]=5
    elif rank=="6":
        dict_card["value"]=6
    elif rank=="7":
        dict_card["value"]=7
    elif rank=="8":
        dict_card["value"]=8
    elif rank=="9":
        dict_card["value"]=9
    elif rank=="10":
        dict_card["value"]=10
    elif rank=="J":
        dict_card["value"]=11
    elif rank=="Q":
        dict_card["value"]=12
    elif rank=="K":
        dict_card["value"]=13
    elif rank=="A":
        dict_card["value"]=14

    return dict_card

def create_deck()-> list[dict]:
    cards=[]

    suites=["H","C","D","S"]
    ranks=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    for s in suites:
        for r in ranks:
            cards.append(create_card(s,r))

    return cards 
    

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    p1_card=["value"]
    p2_card=()
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    else:
        return "p2"
    

def shuffle(deck:list[dict])-> list[dict]:    

    
    index_card1=random.randint(0,51)
    index_card2=random.randint(0,51)

    shuffle=deck[index_card1],deck[index_card2]= deck[index_card2],deck[index_card1]

    return shuffle

shuffle(create_deck)