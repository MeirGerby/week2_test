import player_io

def calculate_hand_value(hand: list[dict]) -> int:
    cards_value = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10, "A": 1
    }

    rank = hand[-1]['rank']
    value = None
    if hand[-1]['rank'] in cards_value:
        value = cards_value[rank]

    return value


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck[-2:])
    dealer["hand"].append(deck[-4: -2])

    for i in range(4):
        deck.pop()

    p1_value = calculate_hand_value(player["hand"])
    p2_value = calculate_hand_value(dealer["hand"])

    print(f"the first values in the player's deck is {p1_value}.")
    print(f"the first values in the dealer's deck is {p2_value}.")


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    value = calculate_hand_value(dealer["hand"])
    while value <= 17:
        dealer["hand"].append(deck[-1])
        deck.pop()

    if value > 21:
        print("The game is over the dealer is failed")
        return False

    else:
        return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    user_input = player_io.ask_player_action()
    while user_input == 'H':
        player["hand"].append(deck[-1])
        deck.pop()
        p_value = calculate_hand_value(player["hand"])
        if p_value > 21:
            print("game over")
            break

        else:
            user_input = player_io.ask_player_action()
    if user_input == 'S':
        d_play = dealer_play(deck, dealer)
        if d_play:
            player_value = calculate_hand_value(player["hand"])
            dealer_value = calculate_hand_value(dealer["hand"])
            if player_value > dealer_value:
                print(f"player is won:\n player's score: {player_value} dealer's score: {dealer_value}")
            elif player_value > dealer_value:
                print(f"dealer is won:\n dealer's score: {dealer_value} player's score: {player_value} ")

            else:
                print(f"no one won:\n player's score: {player_value} dealer's score: {dealer_value}")
    return None

