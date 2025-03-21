from classes import User

def create_user() -> User:
    """Creates a new User object and greets the user upon entry into the game.
    
    :return: A new User object.
    :rtype: User"""
    while True:
        try:
            name: str = input("What is your name? ").title()
        except Exception:
            print("Something went wrong. Try again.")
            continue
        else:
            print(f"Welcome to Baldur's Gate 0.0.1. {name}!")
            return User(name=name)
