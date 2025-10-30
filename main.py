from core import deck, game_logic, player_io






if __name__ == "__main__":
    f_deck = deck.build_standard_deck()
    full_deck = deck.shuffle_by_suit(f_deck)

    player = {"hand": []}
    dealer = {"hand": []}

    game_logic.run_full_game(full_deck, player, dealer)