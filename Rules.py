class Rules:
    def __init__(self, moves):
        self.moves = moves
        self.rules = self.generate_rules()

    def generate_rules(self):
        n = len(self.moves)
        rules = {}
        # Custom rules (adjust as needed)
        win_conditions = {
            "rock": ["scissors"],
            "paper": [],  # paper loses to all
            "scissors": ["paper"]
        }
        for move in self.moves:
            rules[move] = win_conditions.get(move, [])
        return rules

    def determine_winner(self, user_move, computer_move):
        if user_move == computer_move:
            return "Draw"
        elif computer_move in self.rules[user_move]:
            return "Win"
        else:
            return "Lose"
