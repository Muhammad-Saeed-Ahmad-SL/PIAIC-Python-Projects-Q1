import random

def computer_guess():
    print("Think of a number between 1 and 100, and I'll try to guess it!")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        print(f"Is your number {guess}?")

        feedback = input("Enter 'H' if too high, 'L' if too low, or 'C' if correct: ").strip().upper()

        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        elif feedback == 'C':
            print(f"Yay! I guessed your number in {attempts} attempts.")
            return
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

    print("Something seems wrong. Are you sure you are providing correct hints?")

# Run the game
computer_guess()
