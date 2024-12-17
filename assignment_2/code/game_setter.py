from chess_game import ChessGame
import random


def start_random_game(min_moves=3, max_moves=8):
    board_game = ChessGame()

    for _ in range(min_moves, max_moves):
        move = None
        while move is None:
            try:
                move = random.choice(list(board_game.board.legal_moves))
            except IndexError:  # Sometimes board has no legal moves, this prevents error
                board_game = ChessGame()
        board_game.make_move(move)

    return board_game
