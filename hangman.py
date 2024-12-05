import random
from collections import Counter

# List of words to choose from
words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''.split()

# Randomly select a word
word = random.choice(words)

# Initialize game state
guesses_left = len(word) + 2
guessed_letters = set()
