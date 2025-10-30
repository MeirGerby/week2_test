from core import deck, game_logic






if __name__ == "__main__":
    full_deck = deck.build_standard_deck()
    full_deck = deck.shuffle_by_suit(full_deck)

    player = {"hand": []}
    dealer = {"hand": []}

    game_logic.run_full_game(full_deck, player, dealer)