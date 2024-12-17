import math
import random


# MinMax algorithm with alpha beta pruning implementation
def ab_minmax(board_game, depth, alpha, beta, maximizing_player):
    """
    MinMax with alpha beta pruning algorithm implementation
    :param board_game:
    :param depth:
    :param alpha:
    :param beta:
    :param maximizing_player:
    :return:
    """
    if depth == 0 or board_game.is_game_over():
        return board_game.evaluate_board(), None

    best_move = None

    legal_moves = list(board_game.legal_moves)
    random.shuffle(legal_moves)

    if maximizing_player:
        max_eval = -math.inf
        for move in legal_moves:
            board_game.make_move(move)
            eval, _ = ab_minmax(board_game, depth - 1, alpha, beta, False)
            board_game.take_back_last_move()

            if eval >= max_eval:  # the '=' avoids having move set to None because there is no best move
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval, best_move

    # we are not the maximizing player
    min_eval = +math.inf
    for move in legal_moves:
        board_game.make_move(move)
        eval, _ = ab_minmax(board_game, depth - 1, alpha, beta, True)
        board_game.take_back_last_move()

        if eval <= min_eval:  # the '=' avoids having move set to None because there is no best move
            min_eval = eval
            best_move = move

        beta = min(beta, eval)
        if beta <= alpha:
            break

    return min_eval, best_move
