import sys
import random
from KeyGenerator import KeyGenerator
from HMACCalculator import HMACCalculator
from Rules import Rules

class Game:
    def __init__(self, moves):
        if len(moves) < 3 or len(moves) % 2 == 0:
            self.print_error()
            sys.exit(1)

        self.moves = moves
        self.rules = Rules(moves)

    def print_error(self):
        print("Error: The number of moves must be an odd number greater than or equal to 3.")
        print("Example: python game.py rock paper scissors")

    def print_help(self):
        table = [["" for _ in range(len(self.moves) + 1)] for _ in range(len(self.moves) + 1)]
        table[0][0] = " "
        for i, move in enumerate(self.moves):
            table[0][i + 1] = move
            table[i + 1][0] = move
        
        for i in range(1, len(self.moves) + 1):
            for j in range(1, len(self.moves) + 1):
                if i == j:
                    table[i][j] = "Draw"
                elif self.moves[j - 1] in self.rules.rules[self.moves[i - 1]]:
                    table[i][j] = "Win"
                else:
                    table[i][j] = "Lose"
        
        for row in table:
            print("\t".join(row))
    
    def play(self):
        # Print available moves in column format
        print("Available moves:")
        for i, move in enumerate(self.moves):
            print(f"{i + 1} - {move}")
        print("0 - exit")
        print("? - help")

        while True:
            user_input = input("Enter your move: ").strip()

            if user_input == "?":
                self.print_help()
                continue
            elif user_input == "0":
                break

            try:
                user_choice = int(user_input) - 1
                if user_choice < 0 or user_choice >= len(self.moves):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a number corresponding to a move or '?' for help.")
                continue

            # Generate a new key for each round
            key = KeyGenerator.generate_key()
            computer_choice = random.randint(0, len(self.moves) - 1)
            user_move = self.moves[user_choice]
            computer_move = self.moves[computer_choice]

            # Calculate HMAC based on the computer's move and the generated key
            hmac_value = HMACCalculator.calculate_hmac(key, computer_move)

            # Display HMAC value for user verification
            print(f"HMAC: {hmac_value.hex()}")

            # User makes their choice
            print(f"Your move: {user_move}")
            print(f"Computer move: {computer_move}")

            # Determine the result
            result = self.rules.determine_winner(user_move, computer_move)
            print(f"You {result}!")

            # Display the key for user to verify HMAC
            print(f"HMAC key: {key.hex()}")
