import pytest
from Game import Game


def test_game():
    assert True


def test_valid_move():
    # Initialize game
    game = Game()
    
    # Test making a valid move (1,1) - top left corner
    # Note: Internal board uses 0-based indexing, but user input is 1-based
    game.make_move("X", "1 1")
    assert game.board[0][0] == 'X'  # Player 1 should place 'X'
    
    # Test second player's valid move (2,2) - center
    game.make_move("O", "2 2")
    assert game.board[1][1] == 'O'  # Player 2 should place 'O'


def test_invalid_move():
    game = Game()
    
    # Make initial valid move
    game.make_move("X", "1 1")
    
    # Try to place on an already occupied square
    with pytest.raises(ValueError):
        game.make_move("O", "1 1")
    
    # Try to place outside the board
    with pytest.raises(ValueError):
        game.make_move("X", "4 4")
    
    # Try to place with negative coordinates
    with pytest.raises(ValueError):
        game.make_move("O", "-1 1")

def test_check_draw():
    game = Game()
    game.board = [['X', 'O', 'X'],
                  ['X', 'O', 'O'],
                  ['O', 'X', 'X']]
    assert game.check_draw() == True

def test_check_win_x():
    game = Game()
    game.board = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['X', 'O', 'X']]
    assert game.check_win() == True

def test_check_win_o():
    game = Game()
    game.board = [['O', 'X', 'X'],
                  ['O', 'X', ' '],
                  ['O', 'O', 'X']]
    assert game.check_win() == True

def test_check_win_other_diagonal():
    game = Game()
    game.board = [['X', 'O', 'O'],
                  ['X', 'O', 'X'],
                  ['O', 'X', 'X']]
    assert game.check_win() == True

def test_check_win_row():
    game = Game()

    game.make_move("X", "1 1")  
    game.make_move("O", "2 1")
    game.make_move("X", "1 2") 
    game.make_move("O", "2 2")
    game.make_move("X", "1 3")
    
    assert game.check_win() == True







