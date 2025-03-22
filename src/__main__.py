from player import Player
from preGame_module import start_new_game, create_character
import sys

def main() -> None:
    start_new_game()
    player: Player = Player()
    create_character(current_player=player)
        
        
    sys.exit("Program end reached. Shutting down..")
    
    
if __name__ == "__main__":
    main()
