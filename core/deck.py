from random import randrange
def build_standard_deck() -> list[dict]:
    card_type = ['H', 'C', 'D', 'S']
    cards_value = [
        "2", "3", "4", "5", "6", "7", "8", "9",
        "10", "J", "Q", "K", "A"
    ]
    card = {"rank": str, "suite": str}
    full_deck = []
    for i in card_type:
        for j in cards_value:
            card["rank"] = i
            card["suite"] = j
            full_deck.append(card)
    return full_deck









def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(swaps):
        rand = randrange(52)
        card1 = deck[rand]
        rand2 = randrange(52)

        flag = False
        while not flag:
            rand2 = randrange(52)
            if rand2 == rand:
                flag = True
            if deck[rand2]['suite'] == 'H' and deck[rand2]["rank"] % 5 == 0:
                deck[rand2], deck[rand] = deck[rand], deck[rand2]
                flag = True
            elif deck[rand2]['suite'] == 'S' and deck[rand2]["rank"] % 7 == 0:
                deck[rand2], deck[rand] = deck[rand], deck[rand2]
                flag = True
            elif deck[rand2]['suite'] == 'C' and deck[rand2]["rank"] % 3 == 0:
                deck[rand2], deck[rand] = deck[rand], deck[rand2]
                flag = True
            elif deck[rand2]['suite'] == 'D' and deck[rand2]["rank"] % 2 == 0:
                deck[rand2], deck[rand] = deck[rand], deck[rand2]
                flag = True

    return deck
