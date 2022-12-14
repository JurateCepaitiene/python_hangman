import random
from pics import HANGMAN_PICS
from words import SECRET_WORDS

def get_random_word(SECRET_WORDS: list) -> str:
    list_index = random.randint(0, len(SECRET_WORDS) - 1)
    return SECRET_WORDS[list_index]

def display_board(missed_letters: str, correct_letters: str, secret_word: str) ->None:
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('Missed letters:')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)
    for index in range(len(secret_word)): 
        if secret_word[index] in correct_letters:
            blanks = blanks[:index] + secret_word[index] + blanks[index+1:]
    for symbol in blanks: 
        print(symbol, end=' ')
    print()

def get_guess(already_guessed: str) ->str:
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def play_again() ->bool:
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

if __name__=="__main__":
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''
    game_is_done = False
    secret_word = get_random_word(SECRET_WORDS)

    while True:
        display_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess
            found_all_letters = True
        else:
            missed_letters = missed_letters + guess

        for index in range(len(secret_word)):
            if secret_word[index] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yes! The secret word is "' + secret_word + '"! You have won!')
            game_is_done = True


        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
            game_is_done = True

        if game_is_done:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                game_is_done = False
                secret_word = get_random_word(SECRET_WORDS)
            else:
                break