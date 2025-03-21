def start_new_game() -> None:
    """Starts a new game for the user upon confirmation."""
    while True:
        try:
            start_game: str = input("Start a new game? (y/n) ").lower()
        except Exception:
            print("Something went wrong. Try again.")
            continue
        else:
            if start_game == "y":
                print("Starting a new game..")
                break
            elif start_game == "n":
                print("A new game has not started.")
                continue
            else:
                print("Input can only be 'y' or 'n'. Try again.")
                continue
