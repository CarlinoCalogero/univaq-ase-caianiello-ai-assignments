import chess
import chess.engine


class ChessGame:

    def __init__(self):
        self.__board = chess.Board()

    @property
    def board(self):
        return self.__board

    @property
    def legal_moves(self):
        return self.__board.legal_moves

    def is_game_over(self):
        return self.__board.is_game_over()

    def make_move(self, move):
        self.__board.push(move)

    def take_back_last_move(self):
        self.__board.pop()

    # Static evaluation function for chess board
    def evaluate_board(self):
        """
        Static evaluation function for chess board.
        Simple heuristic: material count (weights for pieces)
        :return:
        """
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0  # King is invaluable
        }

        evaluation = 0
        for piece_type in piece_values:
            evaluation += len(self.__board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
            evaluation -= len(self.__board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
        return evaluation

    def evaluate_move(self, move):
        """
        Evaluate a move by applying it and using the static board evaluation.
        :param move:
        :return:
        """
        self.make_move(move)
        score = self.evaluate_board()
        self.take_back_last_move()
        return score
