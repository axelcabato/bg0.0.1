from preGame_module import create_user
from classes import User
import sys


def main() -> None:
    # Create new User object and greet user
    user: User = create_user()
    
    
    sys.exit("Program end reached. Shutting down..")
    
    
if __name__ == "__main__":
    main()
