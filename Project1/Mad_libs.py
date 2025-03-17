def mad_libs():
    # Asking for user inputs
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    
    # Creating the Mad Libs story
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    
    # Printing the story
    print("\nHere is your Mad Libs story:")
    print(story)
    
# Running the function
if __name__ == "__main__":
    mad_libs()
