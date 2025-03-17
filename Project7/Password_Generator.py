import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # Uppercase + Lowercase
    if use_digits:
        characters += string.digits  # Add digits (0-9)
    if use_special_chars:
        characters += string.punctuation  # Add special characters (!@#$%^&*)

    if length < 4:
        print("⚠️ Password length should be at least 4 characters.")
        return "Hello"

    password = "".join(random.sample(characters, length))  # Randomly pick characters
    return password

# Get user input
try:
    length = int(input("Enter password length (min 4): "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_digits, include_special_chars)
    if password:
        print("\n Your Generated Password:", password)
except ValueError:
    print("⚠️ Please enter a valid number for password length.")
