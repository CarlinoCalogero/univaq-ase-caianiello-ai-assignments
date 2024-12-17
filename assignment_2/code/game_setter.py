from chess_game import ChessGame
import random


def start_random_game(min_moves, max_moves):
    board_game = ChessGame()

    for _ in range(min_moves, max_moves):
        move = random.choice(list(board_game.board.legal_moves))
        board_game.make_move(move)

    return board_game
