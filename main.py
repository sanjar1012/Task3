import sys
from Game import Game

def main():
    if len(sys.argv) < 4:
        print("Error: The number of moves must be an odd number greater than or equal to 3.")
        print("Example: python main.py rock paper scissors lizard Spock")
        sys.exit(1)

    moves = sys.argv[1:]
    
    if len(moves) % 2 == 0:
        print("Error: The number of moves must be an odd number greater than or equal to 3.")
        print("Example: python main.py rock paper scissors lizard Spock")
        sys.exit(1)

    game = Game(moves)
    game.play()

if __name__ == "__main__":
    main()
