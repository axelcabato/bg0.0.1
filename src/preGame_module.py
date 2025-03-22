from player import Player
import time

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

def create_character(current_player: Player) -> None:
    """Creates a new Player character by setting their name and class.
    
    :param current_player: A Player object.
    :type current_player: Player"""

    def set_name(current_player: Player) -> None:
        """Sets the Player character's name.
        
        :param current_player: A Player object.
        :type current_player: Player"""
        while True:
            try:
                name: str = input("Enter character name: (case sensitive) ")
            except Exception:
                print("Something went wrong. Try again.")
                continue
            else:
                time.sleep(1.0)
                current_player.char_name = name
                print(f"Character name set: [{current_player.char_name}]")
                break

    def set_class(current_player: Player) -> None:
        """Sets the Player character's class.
        
        :param current_player: A Player object.
        :type current_player: Player"""
        classes: tuple = (
            "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
        )
        print(classes)
        while True:
            try:
                desired_class: str = input("Choose a class: ").capitalize()
            except Exception:
                print("Something went wrong. Try again.")
                continue
            else:
                if desired_class in classes:
                    time.sleep(1.0)
                    current_player.char_class = desired_class
                    print(f"Character class set: [{current_player.char_class}]")
                    break
                else:
                    print("Pick a valid class. Try again.")
                    continue

    set_name(current_player=current_player)
    set_class(current_player=current_player)
    print("Creating character..")
    time.sleep(2.0)
    print(f"Character created: [Name = {current_player.char_name}; Class = {current_player.char_class}]")

def load_game() -> None:
    """Loads the Player into the game."""
    print("Loading game..")
    time.sleep(1.0)
    print("Initializing GPU..")
    time.sleep(3.0)
    print("Loading assets..")
    time.sleep(2.0)
    print("Setting up scenes..")
    time.sleep(2.0)
    print("Complete.")
    time.sleep(2.0)
