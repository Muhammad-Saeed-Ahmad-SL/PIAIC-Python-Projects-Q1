import random

# List of words to guess
words = ["python", "hangman", "developer", "software", "engineering", "computer"]

def get_random_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Number of allowed incorrect guesses

    print("Welcome to Hangman! Try to guess the word.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter!")
            continue
        
        if guess in guessed_letters:
            print(" You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(" Good job! The letter is in the word.")
        else:
            print(" Wrong guess! Try again.")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game over! The word was:", word)

# Run the game
hangman()
