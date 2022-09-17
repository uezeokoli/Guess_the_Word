"""
This program will have a user guess characters of a word until
they have guessed the entire word
"""
import random

words = ["rhino","elephant","tiger","zebra","mouse",\
"cow","rooster","hourse","cheetah","walrus","shark","lizard",\
"beetle","wolf"]
secret_word = random.choice(words)
numbers = "0123456789"
dashes = ("-" * len(secret_word))
guesses = 10


# This will ask user to guess and show them their progress
def get_guess(progress, guesses_left):
    while True:
        if guesses_left == 0:
            print("You lose. The word was: " + secret_word)
            break
        # This will condition will be met when all letters are guessed
        if progress == secret_word:
            print("Congrats! You win. The word was: " + secret_word)
            break
        print(str(guesses_left) + " incorrect guesses left.")
        print(progress)
        guess = input("Guess: ")
        if len(guess) > 1:
            print("Your guess must have exactly one character!")
            continue
        elif guess.isupper():
            print("Your guess must be a lowercase letter!")
            continue
        elif guess in numbers:
            print("You guess must be a lowercase letter!")
        # This is when user puts in valid information
        # Shows progress of guess after every guess
        elif guess in secret_word:
            print("That letter is in the secret word!")
            progress = update_dashes(guess, progress)
            continue
        else:
            print("That letter is not in the secret word!")
            guesses_left = guesses_left - 1
            continue
 
# Funtion will fill in dashes with guessed letter 
def update_dashes(letter, update):
    for i, value in enumerate(secret_word):
        if value == letter:
            update = update[:i] + letter + update[i+1:]
    return update
        
get_guess(dashes, guesses)
