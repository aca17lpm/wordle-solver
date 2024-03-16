# What makes up a wordle? A five letter word
# You can take a guess, and you have some information at your disposal
# You know the english language, ie lots of five letter words
# You might know the positions or presence of some or all of the letters from previous guesses
# When you know the position of all five letters, you have solved the wordle.


# import dataclass
from dataclasses import dataclass
from enum import Enum
# import List
from typing import List

GREEN_SQUARE = '\U0001F7E9'
YELLOW_SQUARE = '\U0001F7E8'
GREY_SQUARE = '\u2B1B'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class Result(Enum):
    GREEN = 'GREEN'
    YELLOW = 'YELLOW'
    GREY = 'GREY'
    UNKNOWN = 'UNKNOWN'
    
def emojify(result: str) -> str:
    """Translate str to result unicode emoji"""
    match result:
        case Result.GREEN:
            return GREEN_SQUARE
        case Result.YELLOW:
            return YELLOW_SQUARE
        case Result.GREY:
            return GREY_SQUARE
        case Result.UNKNOWN:
            return GREY_SQUARE

@dataclass
class LetterPosition:
    """Records the result of one position, with the letter and colour result"""
    letter: str
    result: str

class Green:
    pass

@dataclass
class GuessResult:
    """Records the result of a guess, with five GuessedPositions"""
    positions: List[LetterPosition]

    @property
    def is_correct(self) -> bool:
        return all(position.result == Result.GREEN for position in self.positions)

    @property
    def squares(self):
        return ' '.join(emojify(position.result) for position in self.positions)
    
    @property
    def word(self):
        return ''.join(position.letter for position in self.positions)

def evaluate(guess: str, answer: str) -> GuessResult:
    """Evaluate a string guess against a string answer"""
    
    # Check if guess is five letter string
    if len(guess) != 5:
        raise ValueError('Guess must be five letters')
    
    positions = []
    for i in range(5):
        if guess[i] == answer[i]:
            positions.append(LetterPosition(guess[i], Result.GREEN))
        elif guess[i] in answer:
            positions.append(LetterPosition(guess[i], Result.YELLOW))
        else:
            positions.append(LetterPosition(guess[i], Result.GREY))
    return GuessResult(positions)

class WordleSolver:
    def __init__(self, answer):
        self.answer = answer
        self.guesses : List[GuessResult] = []
        self.letters = [LetterPosition(letter, Result.UNKNOWN) for letter in ALPHABET]
        
    def play_game(self):
        starter_word = 'crane'
        self.play_round(starter_word)
    
    def play_round(self, guess: str):
        # Make some guesses
        result = evaluate(guess, self.answer)
        self.guesses.append(result)

    def next_best_guess(self):
        # Consider all the information we have
        potential_guess = 'xxxxx'

        # A 'Checker' will go into the database, find words with correct green positions,
        # which also contain any yellow letters
        self.best_information
        
    @property
    def state(self):
        return self.guesses
    
    @property
    def green_positions(self):
        green_positions = []
        for guess in self.guesses:
            for index, position in guess.positions:
                if position.result == Result.GREEN:
                    green_positions += (index, position.letter)
        return green_positions

    @property
    def best_information(self):

        best_information = []

        # Initialise with first guess
        if len(self.guesses) < 1:
            return []
        else:
            best_information = self.guesses.positions

        for guess in self.guesses:
            for i in range(5):
                guessed_position = guess.positions[i]
                if guessed_position.result == Result.GREEN:
                    best_information[i] = guessed_position

        return self.guesses
    
    
    
if __name__ == '__main__':
    print(evaluate('apole', 'apple').squares)