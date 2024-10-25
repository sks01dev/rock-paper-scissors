import random
import sys

class RPS:
    def __init__(self):
        # Initialize game with welcome message, move options, and scores
        print('Welcome to RPS 9000!')
        self.moves = {'rock': '🥊', 'paper': '📜', 'scissors': '✂'}
        self.user_score = 0
        self.ai_score = 0

    def play_game(self):
        # Prompt user for their move; end game if they type "exit"
        user_move = input('Rock, paper or scissors? (type "exit" to quit) >> ').lower()

        if user_move == 'exit':
            print(f"Final Score => You: {self.user_score} | AI: {self.ai_score}")
            sys.exit()

        # Check for valid move; restart if invalid
        if user_move not in self.moves:
            print("Invalid move...")
            return self.play_game()

        # AI selects a random move from available options
        ai_move = random.choice(list(self.moves.keys()))

        self.display_moves(user_move, ai_move)  # Show moves of both players
        
        self.check_move(user_move, ai_move)     # Determine winner and update score
        
        print(f"Score => You: {self.user_score} | AI: {self.ai_score}")
            
    def display_moves(self, user_move, ai_move):
        # Display moves of both the user and AI with symbols
        print('-----')
        
        print(f'You: {self.moves[user_move]}')
        
        print(f'AI: {self.moves[ai_move]}')
        
        print('------')

    def check_move(self, user_move, ai_move):
        # Determine game outcome and update scores accordingly
        if user_move == ai_move:
            print("It's a tie!")
        
        elif (user_move == "rock" and ai_move == "scissors") or \
             (user_move == "scissors" and ai_move == "paper") or \
             (user_move == "paper" and ai_move == "rock"):
            print("You win!")
            self.user_score += 1
        
        else:
            print("AI wins...")
            self.ai_score += 1


if __name__ == '__main__':
    # Initialize the game and start playing in a continuous loop
    rps = RPS()
    while True:
        rps.play_game()
