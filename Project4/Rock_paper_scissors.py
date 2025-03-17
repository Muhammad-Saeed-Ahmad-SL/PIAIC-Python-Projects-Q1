import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def play_game():
    print("Welcome to Rock, Paper, Scissors! 🎮")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
        
        if user_choice == "quit":
            print("Thanks for playing! Goodbye! 👋")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

# Run the game
play_game()
