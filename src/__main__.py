from player import Player
from preGame_module import start_new_game, create_character,load_game
import sys

def main() -> None:
    player: Player = Player()
    start_new_game()
    create_character(current_player=player)
    load_game()
        
        
    sys.exit("Program end reached. Shutting down..")
    
    
if __name__ == "__main__":
    main()
