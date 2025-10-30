from random import randrange

def build_standard_deck() -> list[dict]:
    card_type = ["2","3","4","5","6","7","8","9","10","J","Q","K", "A"]
    cards_value = ['H', 'C', 'D', 'S']

    full_deck = []
    for i in card_type:
        for j in cards_value:
            card = create_card(i,j)
            full_deck.append(card)
    return full_deck


def create_card(rank: str, suite: str):

    card = {}
    card_type = ["2","3","4","5","6","7","8","9","10","J","Q","K", "A"]
    cards_value = ['H', 'C', 'D', 'S']

    if rank in card_type and suite in cards_value:
        card["rank"] = rank
        card["suite"] = suite

    return card


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(2):
        rand = randrange(len(deck))
        rand2 = randrange(len(deck))

        while rand2 == rand:
            rand2 = randrange(len(deck))
        card2 = deck[rand2]
        flag = False
        while not flag:
            if card2['suite'] == 'H':
                if rand2 % 5 == 0:
                    deck[rand2], deck[rand] = deck[rand], deck[rand2]
                    flag = True
            elif card2['suite'] == 'S':
                if rand2 % 7 == 0:
                    deck[rand2], deck[rand] = deck[rand], deck[rand2]
                    flag = True
            elif card2['suite'] == 'C':
                if rand2 % 3 == 0:
                    deck[rand2], deck[rand] = deck[rand], deck[rand2]
                    flag = True
            elif card2['suite'] == 'D':
                if rand2 % 2 == 0:
                    deck[rand2], deck[rand] = deck[rand], deck[rand2]
                    flag = True

    return deck
