# What makes up a wordle? A five letter word
# You can take a guess, and you have some information at your disposal
# You know the english language
# You might know the positions or presence of some or all of the letters
# When you know the position of all five letters, you have solved the wordle.


# import dataclass
from dataclasses import dataclass
from enum import Enum
# import List
from typing import List

GREEN_SQUARE = '\U0001F7E9'
YELLOW_SQUARE = '\U0001F7E8'
GREY_SQUARE = '\u2B1B'



class Result(Enum):
    GREEN = 'GREEN'
    YELLOW = 'YELLOW'
    GREY = 'GREY'
    
def emojify(result: str) -> str:
    match result:
        case Result.GREEN:
            return GREEN_SQUARE
        case Result.YELLOW:
            return YELLOW_SQUARE
        case Result.GREY:
            return GREY_SQUARE

@dataclass
class GuessedPosition:
    letter: str
    result: str
    

@dataclass
class Guess:
    positions: List[GuessedPosition]

    @property
    def is_correct(self) -> bool:
        return all(position.result == Result.GREEN for position in self.positions)

    @property
    def squares(self):
        return ' '.join(emojify(position.result) for position in self.positions)

def evaluate(guess: str, answer: str) -> Guess:
    positions = []
    for i in range(5):
        if guess[i] == answer[i]:
            positions.append(GuessedPosition(guess[i], Result.GREEN))
        elif guess[i] in answer:
            positions.append(GuessedPosition(guess[i], Result.YELLOW))
        else:
            positions.append(GuessedPosition(guess[i], Result.GREY))
    return Guess(positions)
    
if __name__ == '__main__':
    print(evaluate('apole', 'apple').squares)