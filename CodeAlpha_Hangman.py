import random

# Predefined list of 5 words as specified in the scope
WORD_POOL = ["python", "programming", "developer", "computer", "keyboard"]

# ASCII art representation for the hangman stages to enhance visual feedback in the console
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def get_masked_word(word, guessed_letters):
    """
    Creates the string representing the word showing guessed letters
    and underscores for unguessed letters.
    """
    display_list = []
    for letter in word:
        if letter in guessed_letters:
            display_list.append(letter)
        else:
            display_list.append("_")
    return " ".join(display_list)

def play_hangman():
    """
    Main game loop and state management logic.
    """
    # Select a random word from the predefined pool
    secret_word = random.choice(WORD_POOL)
    
    # Track state
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("========================================")
    print("      Welcome to Console Hangman!       ")
    print("========================================")
    print("Can you guess the secret word before running out of attempts?")
    print(f"Rules: You have a maximum of {max_incorrect} incorrect attempts.")
    
    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Display current status
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Word to guess:  {get_masked_word(secret_word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect attempts remaining: {max_incorrect - incorrect_guesses}")
        print("----------------------------------------")

        # Get player input
        guess = input("Enter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("\n[!] Invalid input. Please enter exactly one alphabetical letter.\n")
            continue
        
        if guess in guessed_letters:
            print(f"\n[!] You have already guessed the letter '{guess}'. Try a different one!\n")
            continue

        # Add guess to the list of guessed letters
        guessed_letters.add(guess)

        # Process the guess
        if guess in secret_word:
            print(f"\n[+] Good job! '{guess}' is in the secret word.\n")
        else:
            incorrect_guesses += 1
            print(f"\n[-] Incorrect! '{guess}' is not in the secret word.\n")

        # Check for victory condition (no underscores left)
        # We strip spaces from the masked word representation to check
        current_masked = get_masked_word(secret_word, guessed_letters).replace(" ", "")
        if current_masked == secret_word:
            print("========================================")
            print("        🎉 CONGRATULATIONS! 🎉          ")
            print("========================================")
            print(f"You successfully guessed the word: {secret_word.upper()}!")
            print(f"You completed the game with {incorrect_guesses} incorrect attempts.\n")
            break
    else:
        # Triggered if the while loop finishes because incorrect_guesses reached max_incorrect
        print(HANGMAN_STAGES[incorrect_guesses])
        print("========================================")
        print("            💀 GAME OVER! 💀            ")
        print("========================================")
        print("You've run out of attempts and the hangman is complete.")
        print(f"The secret word was: {secret_word.upper()}\n")

if __name__ == "__main__":
    # Start the game
    play_hangman()