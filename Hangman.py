import random
import string

from words import words

word = random.choice(words).upper()
alphabet = string.ascii_uppercase
print(word)
guessed_letters = []
lives = 6


def shown_word(word):
    """
    This function takes the hidden word and replaces the letters with underscores.
    """
    shown_word = []
    for letter in word:
        if letter in guessed_letters:
            shown_word.append(letter)
        else:
            shown_word.append("_")
    return shown_word


def guess_letter():
    """
    This function takes user input and checks if it is in the word.
    """
    print(shown_word(word))
    guess = input("Guess a letter: ").upper()
    guessed_letters.append(guess)
    
    if guess not in alphabet:
        print("Invalid input \n, try again")
        guess_letter()

    if guess in word:
        print("Correct! \n")
    else:
        print("Incorrect! \n")
        global lives
        lives -= 1


while shown_word(word) != list(word) and lives > 0:
    print(f"You have {lives} lives left.")
    guess_letter()

    if shown_word(word) == list(word):
        print(word)
        print("You won!")
        break

    elif lives == 0:
        print(shown_word(word))
        print("You lost!")
        break
