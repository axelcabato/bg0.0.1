def greet_user() -> None:
    """Greets user upon entry into the game after asking for their name."""
    while True:
        try:
            username: str = input("What is your name? ").title()
        except Exception:
            print("Something went wrong. Try again.")
            continue
        else:
            print(f"Welcome to Baldur's Gate 0.0.1, {username}!")
            break