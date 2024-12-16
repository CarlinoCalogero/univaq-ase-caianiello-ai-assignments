from chess_game import ChessGame
from ab_min_max import ab_minmax
from bl_minmax import bl_minmax
from bl_minmax_l import bl_minmax_l
import math

if __name__ == '__main__':
    board_game = ChessGame()
    print(ab_minmax(board_game, 3, math.inf, math.inf, True))
    print(bl_minmax(board_game, 3, math.inf, math.inf, True, 5))
    print(bl_minmax_l(board_game, 3, math.inf, math.inf, True, 5, 1))
