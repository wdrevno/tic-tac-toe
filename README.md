# Tic Tac Toe Game

## Installation

1. Clone the repository:
```bash
git clone https://github.com/wdrevno/tic-tac-toe.git
cd tic-tac-toe
```


## Running the Game

Simply run:
```bash
python play_game.py
```

## Testing

Install pytest:
```bash
pip install pytest
```

To run tests:
```bash
pytest
```

## Sample Game Play

```
python play_game.py 

Welcome to Tic Tac Toe!

You can quit at any time by entering Q.
To make a move, enter the row and column of the cell you want to mark.
The board is indexed from 1 to 3 for both rows and columns.
For example, to mark the cell in the top-left corner, enter: 1 1
To mark the cell in the top-right corner, enter: 1 3
Make sure to enter the row and column number with a space between them.
The first row is the top row, and the first column is the left column.
Good luck!


Current board:

   |   |   
---+---+---
   |   |   
---+---+---
   |   |   


Player "X", make your move (row, column): 3 1

Current board:

   |   |   
---+---+---
   |   |   
---+---+---
 X |   |   


Player "O", make your move (row, column): 2 1

Current board:

   |   |   
---+---+---
 O |   |   
---+---+---
 X |   |   


Player "X", make your move (row, column): 2 2

Current board:

   |   |   
---+---+---
 O | X |   
---+---+---
 X |   |   


Player "O", make your move (row, column): 1 1

Current board:

 O |   |   
---+---+---
 O | X |   
---+---+---
 X |   |   


Player "X", make your move (row, column): 1 3

X wins!

Current board:

 O |   | X 
---+---+---
 O | X |   
---+---+---
 X |   |   