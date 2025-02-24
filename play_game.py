'''
Game of tic tac toe in terminal
'''

from Game import Game

def main():
    game = Game()
    game.give_game_instructions()

    while not game.game_over:
        game.print_board()
        row_input = input(f'Player "{game.whose_turn}", make your move (row, column): ')
            
        try:
            game.make_move(game.whose_turn, row_input)
        except ValueError:
            print('Please try again.')
            
if __name__ == '__main__':
    main()
