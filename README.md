# Python Hangman

Hangman is a popular word guessing game where the player attempts to guess a word by suggesting letters. The game is won if the player successfully guesses the word with less then 10 missed attempts, otherwise looses.

![](https://github.com/JurateCepaitiene/python_hangman/blob/main/screenshot.png)

## Installation

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer.

From your command line:

```bash
# Clone this repository
$ git clone https://github.com/JurateCepaitiene/python_hangman.git
```

You'll need to have the required extensions.

```bash
# To install them
$ pip install -r requirements.txt
```

## How To Play

From here you shall open nerminal and run the game by typing:

```bash
$ python logic.py
```

## Features

- Allows guesses with letters only
- Both upper and lower-case letters accepted
- Traditional hangman figure displayed in terminal, changeing with the player's move
- Indicates player's missed guesses in seperate line
- Displayes the secret word if the player lost
