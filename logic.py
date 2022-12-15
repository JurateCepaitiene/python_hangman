import os
import random
from pics import HANGMAN_PICS
from words import SECRET_WORDS

def clear():
    os.system("cls")

def get_random_word(SECRET_WORDS: list) -> str:
    list_index = random.randint(0, len(SECRET_WORDS) - 1)
    return SECRET_WORDS[list_index]

def get_hangman_pics(image_index: int) -> str:
    line_count = HANGMAN_PICS[image_index].count('\n') + 1
    lines = [""] * line_count

    for index in range(image_index + 1):
        picture_lines = HANGMAN_PICS[index].split('\n')
        for line_index in range(line_count):
            lines[line_index] += picture_lines[line_index] + " "

    result = ""
    for line in lines:
        result += line + "\n"

    return result

def get_board_text(missed_letters: str, correct_letters: str, secret_word: str) -> str:
    result_board = "H A N G M A N\n"

    image_index = len(missed_letters)
    image = get_hangman_pics(image_index)
    result_board += f"{image}\n\n"

    result_board += "Missed letters: "
    for letter in missed_letters:
        result_board += f"{letter} "
    result_board += "\n"

    for letter in secret_word: 
        if letter in correct_letters:
            result_board += f"{letter} "
        else:
            result_board += f"_ "
    result_board += "\n"

    return result_board

def display_board(missed_letters: str, correct_letters: str, secret_word: str) -> None:
    clear()
    result_board = get_board_text(missed_letters, correct_letters, secret_word)
    print(result_board)

def get_guess(already_guessed: str) -> str:
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

def play_again() -> bool:
    print('If you want to play again - enter anything starting with "y" :).')
    return input().lower().startswith('y')

def found_all_letters(secret_word: str, correct_letters: str) -> bool:
    result = True
    for letter in secret_word:
        if letter not in correct_letters:
            result = False
            break
    return result

def reset_state():
    global missed_letters, correct_letters, game_is_done, secret_word
    missed_letters = ""
    correct_letters = ""
    game_is_done = False
    secret_word = get_random_word(SECRET_WORDS).lower()


max_missed_count = len(HANGMAN_PICS) - 1
reset_state()
while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters = correct_letters + guess
    else:
        missed_letters = missed_letters + guess

    lost_the_game = len(missed_letters) == max_missed_count
    if lost_the_game or found_all_letters(secret_word, correct_letters):
        display_board(missed_letters, correct_letters, secret_word)
        if lost_the_game:
            print(f"You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses, the word was \"{secret_word}\"")
        else:
            print(f"Yes! The secret word is \"{secret_word}\"! You have won!")

        if play_again():
            reset_state()
        else:
            break