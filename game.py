import random

suits = ('Pik','Kier','Karo','Trefl')
cards = ('As','10','Król','Dama','Walet','9')
values = {'As': 11,'10': 10,'Król': 4,'Dama': 3,'Walet': 2,'9': 0} 

# stworzenie talii kart
def create_deck():
    # deck = []
    # for suit in suits:
    #     for card in cards:
    #         card = (card, suit)
    #         deck.append(card)
    # return deck
    return [(card,suit) for card in cards for suit in suits]

# tasowanie i wyłonienie trumfa
def prepare_game(deck):
    random.shuffle(deck)

    # usuwamy karte z góry i zwracamy ją w funkcji
    trump = deck.pop() 

    # Wkładamy trumfa na spód talii
    deck.insert(0,trump)

    return deck, trump[1]

# rozdawanie
def dealing(deck):
    player_hand = []
    ai_hand = []

    for _ in range(6):
        player_hand.append(deck.pop())
        ai_hand.append(deck.pop())
    return player_hand,ai_hand

# porównywanie kard, True - wygrał lead
def compare_cards(card_lead,card_follow,trump_suit):
    if card_lead[1] == card_follow[1]:
        if values[card_lead[0]] > values[card_follow[0]]:
            return True
        else:
            return False
    elif card_follow[1] == trump_suit:
        return False
    return True

def info(player_hand,ai_hand,trump,deck):
      print(f'Ręka gracza: {player_hand}\nRęka AI: {ai_hand}\ntrump: {trump}\nPozostałe karty: {deck}')

def player_info(player_hand,deck,player_points):
    print(f'Liczba kart w talii: {len(deck)}\nKarta na dole: {deck[0][0]} {deck[0][1]}\nPunkty: {player_points}')
    print("Wybierz karte:")
    for i in range(len(player_hand)):
        print(f'[{i}] {player_hand[i][0]} {player_hand[i][1]}')

def game():
    player_points = 0
    ai_points = 0
    deck = create_deck()
    deck, trump = prepare_game(deck)
    player_hand, ai_hand = dealing(deck)
    #info(player_hand,ai_hand,trump,deck)
    player_lead = True
    if player_lead:
        player_info(player_hand,deck,player_points)
        player_pick = player_hand.pop(int(input()))
        ai_pick = ai_hand.pop()
        print(f'Gracz rzuca: {player_pick}\nAI rzuca: {ai_pick}')
        if compare_cards(player_pick,ai_pick,trump):
            player_points += values[player_pick[0]] + values[ai_pick[0]]
        else:
            player_lead = False
            ai_points += values[player_pick[0]] + values[ai_pick[0]]
    if len(deck) > 1:
        if player_lead:
            player_hand.insert(0,deck.pop())
            ai_hand.insert(0,deck.pop())
        else:
            ai_hand.insert(0,deck.pop())
            player_hand.insert(0,deck.pop())
    player_info(player_hand,deck,player_points)

game()



