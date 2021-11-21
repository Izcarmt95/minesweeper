from enum import Enum

class State(Enum):
    ONE_MINE = 1
    TWO_MINE = 2
    THREE_MINE = 3
    FOUR_MINE = 4
    FIVE_MINE = 5
    SIX_MINE = 6
    SEVEN_MINE = 7
    EIGHT_MINE = 8
    EMPTY = 0
    MINE = 9
    FLAG = 10
    QUESTION = 11
    EXPLODED = 12
    
    def __repr__(self) -> str:
        return self.value
    
    
    def __str__(self) -> str:
        return str(self.value)