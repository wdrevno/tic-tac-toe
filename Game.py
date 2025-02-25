from typing import List, Tuple
from time import sleep
class Game:
    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.whose_turn = 'X' #other player is O
        self.game_over = False

    def give_game_instructions(self):
        print('\nWelcome to Tic Tac Toe!\n')
        print('You can quit at any time by entering Q.')
        print('To make a move, enter the row and column of the cell you want to mark.')
        print('The board is indexed from 1 to 3 for both rows and columns.')
        print('For example, to mark the cell in the top-left corner, enter: 1 1')
        print('To mark the cell in the top-right corner, enter: 1 3')
        print('Make sure to enter the row and column number with a space between them.')
        print('The first row is the top row, and the first column is the left column.')
        print('Good luck!\n')
        sleep(1)
        

    def print_board(self) -> None:
        print('\nCurrent board:\n')
        for i, row in enumerate(self.board):
            print(f' {row[0]} | {row[1]} | {row[2]} ')
            if i < 2:  # Don't print the divider after the last row
                print('---+---+---')
        print('\n')

    def make_move(self, player: str, square: str) -> None:

        if square.upper() == 'Q':
            self.end_game()
            return
        
        if not self._is_valid_move(square):
            raise ValueError("Invalid move")

        move = square.split()
        row = int(move[0])-1
        col = int(move[1])-1

        self.board[row][col] = player
        
        if self.check_win() or self.check_draw():
            self.end_game()
            return

        if player == 'X':
            self.whose_turn = 'O'
            return
        else:
            self.whose_turn = 'X'
            return


    def _is_valid_move(self, square: str) -> bool:
        # Check if input is a string and has exactly 2 numbers separated by space
        try:
            row, col = square.split()
            row, col = int(row), int(col)
        except (ValueError, AttributeError):
            print('Invalid move. Please enter two numbers separated by a space (e.g., "1 2")')
            return False

        # Check if numbers are between 1 and 3
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print('Invalid move. Row and column numbers must be between 1 and 3')
            return False

        # Check if the selected square is empty
        if self.board[row-1][col-1] != ' ':
            print('Invalid move. That square is already taken')
            return False

        return True

    
    def check_win(self) -> bool:
        # Helper function to check if a cell is not empty
        def _is_not_empty(row: int, col: int) -> bool:
            return self.board[row][col] != ' '

        #check rows
        for row in range(3):
            if (self.board[row][0] == self.board[row][1] == self.board[row][2] 
                and _is_not_empty(row, 0)):
                print(f'\n{self.whose_turn} wins!')
                self.print_board()
                return True

        #check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] 
                and _is_not_empty(0, col)):
                print(f'\n{self.whose_turn} wins!')
                self.print_board()
                return True

        #check both diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] 
            and _is_not_empty(0, 0)):
            print(f'\n{self.whose_turn} wins!')
            self.print_board()
            return True
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] 
            and _is_not_empty(0, 2)):
            print(f'\n{self.whose_turn} wins!')
            self.print_board()
            return True
        
        return False

    def check_draw(self) -> bool:
        # Check if any empty spaces remain on the board
        for row in self.board:
            if ' ' in row:
                return False
        
        # If no empty spaces and no winner, it's a draw
        if not self.check_win():
            print('It is a draw!')
            return True
        
        return False

    def player_quit(self, move: str) -> bool:
        if move.upper() == 'Q':
            self.end_game()
        return False
    
    def end_game(self) -> None:
        print('Ending game...')
        self.game_over = True
        return

        
        