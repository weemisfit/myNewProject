import random

# List of words for the game
words = ["hangman", "python", "game", "programming", "openai"]

# Hangman graphics
hangman_graphics = [
    '''
     +---+
         |
         |
         |
        ===
    ''',
    '''
     +---+
     O   |
         |
         |
        ===
    ''',
    '''
     +---+
     O   |
     |   |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|   |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|\  |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|\  |
    /    |
        ===
    ''',
    '''
     +---+
     O   |
    /|\  |
    / \  |
        ===
    '''
]


def select_word():
    """Selects a random word from the word list."""
    return random.choice(words)


def initialize_progress(word):
    """Initializes the progress string with underscores."""
    return "_" * len(word)


def update_progress(word, progress, letter):
    """Updates the progress string with correctly guessed letters."""
    updated_progress = ""
    for i in range(len(word)):
        if word[i] == letter:
            updated_progress += letter
        else:
            updated_progress += progress[i]
    return updated_progress


def display_progress(progress, guesses_left):
    """Displays the hangman graphics and the current progress."""
    print(hangman_graphics[6 - guesses_left])
    print("Progress:", progress)


def hangman():
    word = select_word()
    progress = initialize_progress(word)
    guesses_left = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    display_progress(progress, guesses_left)

    while guesses_left > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            progress = update_progress(word, progress, guess)
            display_progress(progress, guesses_left)

            if progress == word:
                print("Congratulations! You guessed the word correctly!")
                break
        else:
            guesses_left -= 1
            display_progress(progress, guesses_left)
            print("Wrong guess. You have", guesses_left, "guesses left.")

    if guesses_left == 0:
        print("You lost! The word was:", word)


hangman()
