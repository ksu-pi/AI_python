import random
from collections import Counter

words = '''apple banana mango strawberry'''
words = words.split(' ')

random_word = random.choice(words)

def main():

    print('Guess the word')

    for i in random_word:
        print('_', end='')
    print()

    chances = len(random_word) + 3
    correct = 0
    guessed_letter = ''

    try:
        while (chances != 0):
            chances =- 1
            try:
                guess = str(input('Enter your letter to guess the word: '))
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Only characters allowed')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter')
            elif guess in guessed_letter:
                print('Already guessed that letter')
                continue

            if guess in random_word:
                guessed_letter += guess

            for w in random_word:
                if w in guessed_letter:
                    print(w, end='')
                    correct += 1
                else:
                    print('_', end='')

            if (Counter(guessed_letter) == Counter(random_word)):
                print()
                print('Congratulations, you won!')
                break

        if chances == 0:
            print()
            print('Woops, you lost')
            print('The word was {}'.format(random_word))

    except:
        print()
        print('Bye!')
        exit()

main()

