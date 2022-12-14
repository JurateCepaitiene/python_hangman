# Hangman

Hangman is a popular word guessing game where the player attempts to guess a word or phrase by suggesting letters or numbers. The game is won if the player successfully guesses the word, and is lost if they run out of guesses.

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

## How To Use

From here you can run it by typing:

```bash
$ python logic.py
```

## Features

- Allows guesses with letters only
- Traditional hangman figure displayed in terminal, changeing with the player move
- Indicates player's missed guesses in seperate line
- Displayes the secret word if the player lost
