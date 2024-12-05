import random
from collections import Counter

# List of words to choose from
words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''.split()

# Randomly select a word
word = random.choice(words)

# Initialize game state
guesses_left = len(word) + 2
guessed_letters = set()
while guesses_left > 0:
    # Display the current word state
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(display_word)

    # Get user's guess
    guess = input('Guess a letter: ').lower()

    # Validate the guess
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print('You already guessed that letter.')
        continue
# Add the guessed letter to the set of guessed letters
    guessed_letters.add(guess)

    # Check if the guess is correct
    if guess in word:
        print('Correct guess!')
        if set(word) == guessed_letters:
            print('You win!')
            break
    else:
        guesses_left -= 1
        print('Incorrect guess. Guesses left:', guesses_left)
