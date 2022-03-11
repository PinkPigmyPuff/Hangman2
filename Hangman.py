import random
import string

from words import words


def hangman():
    word = random.choice(words).upper()
    print(word)
    word_letters = set(word)
    print(word_letters)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters guessed
        print('You have ', lives, ' lives left')
        print('You have guessed these letters: ', ''.join(used_letters))
        guess = input("Guess a letter: ").upper()

        # current word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ''.join(word_list))

        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1

        elif guess in used_letters:
            print("You have already guessed this letter")

        else:
            print("invalid character")

    if lives == 0:
        print("You died")
    else:
        print("You win!")


hangman()
