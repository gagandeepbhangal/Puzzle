"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    return puzzle == view:

def game_over(puzzle: str, view: str, selection: str) -> bool:
    """Return True if and only if puzzle is the same as view or the selection is QUIT.

    >>> game_over('apple', 'apple', 'S')
    True
    >>> game_over('banana', 'ban^^a', 'S')
    False
    >>> game_over('apple', 'app^e', 'Q')
    True
    """
    if puzzle == view or selection == QUIT:
        return True
    return False

def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True iff the letter is a consonant that appears in the puzzle but not view.

    >>> bonus_letter('apple', 'a^^le', 'p')
    True
    >>> bonus_letter('banana', 'ba^a^a', 'b')
    False
    >>> bonus_letter('apple', '^pp^e', 'a')
    False
    """
    if letter in puzzle and letter not in view:
        if letter not in ('a', 'e', 'i', 'o', 'u'):
            return True
    return False

def update_letter_view(puzzle: str, view: str, position: int, guess: str) -> str:
    """Return the updated view based on whether the guess matches position in puzzle

    >>> update_letter_view('apple', 'a^^le', 2, 'p')
    p
    >>> update_letter_view('banana', 'ba^a^a', 0, 'b')
    b
    >>> update_letter_view('bitter', '^itter', 0, 'c')
    ^
    """
    if guess == puzzle[position]:
        return puzzle[position]
    return view[position]

def calculate_score(score: int, occurence: int, letter: str) -> int:
    """Return score by adding or subtracting points based on the occurence of the letter

    >>> calculate_score(4, 3, 'p')
    7
    >>> calculate_score(5, 8, 'e')
    4
    >>> calculate_score(3, 0, 'u')
    2
    >>> calculate_score(4, 0, 'g')
    4
    """
    if letter not in ('a', 'e', 'i', 'o', 'u'):
        return score + (occurence * CONSONANT_POINTS)
    return score - VOWEL_PRICE

def next_player(player: str, occurence: int) -> str:
    """Iff occurrences is greater than zero, the current player plays again. Return player

    >>> next_player('Player One', 2)
    'Player One'
    >>> next_player('Player Two', 6)
    'Player Two'
    >>> next_player('Player Two', 0)
    'Player One'
    >>> next_player('Player One', 0)
    'Player Two'
    """
    if occurence > 0:
        return player
    if player == PLAYER_ONE:
        return PLAYER_TWO
    return PLAYER_ONE
