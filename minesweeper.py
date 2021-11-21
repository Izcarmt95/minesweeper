from typing import Counter, List
from utils import State
import random


DEFAULT_ROW = 10
DEFAULT_COLUMN = 10
DEFAULT_MINE = 90


class Minesweeper():
    rows: int =  0
    column: int = 0
    mine: int = 0 
    board: List[List[State]] = []
    mine_list : List[int] = []
    
    
    def __init__(self, rows: int = DEFAULT_ROW , column: int = DEFAULT_COLUMN, mine: int = DEFAULT_MINE) -> None:
        
        self.rows = rows
        self.column = column
        self.mine = mine
        self.board = [[State.EMPTY for j in range(0, self.column)] for i in range(0, self.rows)]


    def _generate_random_mine(self) -> List[int]:
        
        length = self.rows * self.column
        cell_list: List[int] = list(range(0, self.rows * self.column))   
        mine_list: List[int] = [] 
                          
        random.shuffle(mine_list)
        
        for k in range(0, self.mine):
            index = random.randint(0, length - k - 1)
            mine_list.append(cell_list.pop(index))
            
        return mine_list

    
    def _set_nearby_mines_number(self, mine_i: int, mine_j: int) -> None:
        
        """ 
        args: pos_i , pos_j of mine position 
        
        return None
        """
        cells_pos = ((mine_i - 1, mine_j), (mine_i - 1, mine_j - 1), (mine_i - 1, mine_j + 1), 
                     (mine_i, mine_j - 1),(mine_i, mine_j + 1), 
                     (mine_i + 1, mine_j - 1), (mine_i + 1, mine_j), (mine_i + 1, mine_j + 1))

        for pos in cells_pos:
            if not (pos[0] == self.rows or pos[0] < 0 or pos[1] == self.column or pos[1] < 0):
                if not self.board[pos[0]][pos[1]] == State.MINE:
                    self.board[pos[0]][pos[1]] = State(self.board[pos[0]][pos[1]].value + 1)
               
               
    def set_board(self) -> None:
        
        self.mine_list: List[int] = sorted(self._generate_random_mine())
        
        for m in self.mine_list:
            self.board[m // self.column][m % self.column] = State.MINE
       
        for m in self.mine_list:
           self._set_nearby_mines_number(m // self.column, m % self.column)


    def __repr__(self) -> str:
        
        column_repr = ''
        row_repr: List[str] = []
        
        for row in self.board:
            column_repr = ' | '.join(map(str, row))
            column_repr = '| {} |\n {}'.format(column_repr, '-' * (len(column_repr) + 2))
            row_repr.append(column_repr)
        
        to_string = ' {}\n{}\n'.format('-' * (len(column_repr)//2 - 2), '\n'.join(row_repr))
    
        return to_string 
    
        
        
        
        
        
        
        
        
        

