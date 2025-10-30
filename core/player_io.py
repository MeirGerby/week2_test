
def ask_player_action() -> str:
    inp = input("Enter H for continue or S for stoping")
    check_inp = ['H', 'S']

    while inp not in check_inp:
        inp = input("Enter H for continue or S for stoping")

    return inp



