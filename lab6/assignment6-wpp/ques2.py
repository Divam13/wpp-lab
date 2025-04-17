import random # type: ignore

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_wins += 1
            return 'user'
        else:
            self.computer_wins += 1
            return 'computer'

    def has_won_game(self):
        if self.user_wins > self.computer_wins:
            return 'user'
        elif self.computer_wins > self.user_wins:
            return 'computer'
        else:
            return 'tie'

    def play(self):
        while self.current_round < self.rounds:
            self.current_round += 1
            print(f"\nRound {self.current_round}")
            
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
            while user_choice not in self.choices:
                user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
            
            computer_choice = self.get_computer_choice()
            print(f"Computer's choice: {computer_choice}")

            winner = self.find_winner(user_choice, computer_choice)
            if winner == 'tie':
                print("This round is a tie!")
            elif winner == 'user':
                print("You win this round!")
            else:
                print("Computer wins this round!")
        
        overall_winner = self.has_won_game()
        if overall_winner == 'tie':
            print("\nThe game is a tie!")
        elif overall_winner == 'user':
            print("\nCongratulations! You won the game!")
        else:
            print("\nComputer wins the game! Better luck next time.")

if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds you want to play: "))
    game = Rock_paper_scissors(rounds)
    game.play()
