import random

suits = ('Pik','Kier','Karo','Trefl')
cards = ('A','10','K','Q','J','9')
values = {'A': 11,'10': 10,'K': 4,'Q': 3,'J': 2,'9': 0} 

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
    if len(deck) > 0:
        print(f'Liczba kart w talii: {len(deck)}\nKarta na dole: {deck[0][0]} {deck[0][1]}\nPunkty: {player_points}')
    else:
        print("Talia pusta")
    for i in range(len(player_hand)):
        print(f'[{i}] {player_hand[i][0]} {player_hand[i][1]}')

def chosse_winner(player_points,ai_points):
    if player_points > 66:
        print(f'Wygrywa gracz {player_points} - {ai_points}')
        return 0
    elif ai_points > 66:
        print(f'Wygrywa AI {ai_points} - {player_points}')
        return 1
    else:
        print(f'Remis {player_points} - {ai_points}')
        return 2
def get_user_choice(player_hand):
    while True:
        try:
            pick = int(input())
            if 0 <= pick < len(player_hand):
                return pick
            else:
                print("Nieprawidłowy wybór!")
        except ValueError:
            print("To nie jest cyfra!")

def check_marriages(card, hand, trump):
    if card[0] == 'Q' or card[0] == 'K':
        for hand_card in hand:
            if hand_card[1] == card[1]:
                if hand_card[0] == 'Q' or hand_card[0] == 'K':
                    if card[1] == trump:
                        print('Meldunek 40!!!')
                        return 40
                    else:
                        print('Meldunek 20!')
                        return 20
    return 0

def game():
    player_points = 0
    ai_points = 0
    deck = create_deck()
    # trump - kolor karty na dnie
    deck, trump = prepare_game(deck)
    player_hand, ai_hand = dealing(deck)
    player_lead = True
    while len(player_hand) > 0 and player_points < 66 and ai_points < 66:
        player_info(player_hand,deck,player_points)
        if player_lead:
            lead_pick = player_hand.pop(get_user_choice(player_hand))
            player_points += check_marriages(lead_pick,player_hand, trump)
            follow_pick = ai_hand.pop()
            print(f'Gracz rzuca: {lead_pick}\nAI rzuca: {follow_pick}')
        else:
            lead_pick = ai_hand.pop()
            ai_points += check_marriages(lead_pick,ai_hand,trump)
            print(f'AI rzuca: {lead_pick}')
            follow_pick = player_hand.pop(get_user_choice(player_hand))
            print(f'Gracz rzuca: {follow_pick}\nAI rzuca: {lead_pick}')

       # Dystrybucja punktów i określanie kto wychodzi 
        winner_is_lead = compare_cards(lead_pick,follow_pick,trump)
        player_is_winner = False
        trick_points =  values[lead_pick[0]] + values[follow_pick[0]]
       
        if winner_is_lead:
            if player_lead:
                player_is_winner = True
                player_points += trick_points
            else:
                ai_points += trick_points
        # Wychodzący przegrał
        else:
            if player_lead:
                ai_points += trick_points
            else:
                player_points += trick_points
                player_is_winner = True
            player_lead = not player_lead
            
        # Dobieranie kart
        if len(deck) > 0:
            if player_is_winner:
                player_hand.append(deck.pop())
                ai_hand.append(deck.pop())
            else:
                ai_hand.append(deck.pop())
                player_hand.append(deck.pop())
    # 0 - gracz, 1 - ai, 2 - remis
    game_result = chosse_winner(player_points,ai_points)
game()

# TODO
# - Gra gdy talia się skonczy
# - wyjmowanie karty ze spodu