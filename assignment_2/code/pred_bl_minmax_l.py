import math
from pred_bl_minmax import pred_bl_minmax
import random


def predict_board_l(move, eval_level, board_game, alpha, beta, maximizing_player, branch_factor, model, scaler):
    board_game.make_move(move)
    score, best_move = pred_bl_minmax(board_game, eval_level, alpha, beta, maximizing_player, branch_factor, model, scaler)
    board_game.take_back_last_move()
    return score


# MinMax algorithm with alpha beta pruning implementation
def pred_bl_minmax_l(board_game, depth, alpha, beta, maximizing_player, branch_factor, eval_level, model, scaler):
    """
    Predictive branch-limited MinMax with state evaluation at level l and alpha beta pruning algorithm implementation using trained model
    :param board_game:
    :param depth:
    :param alpha:
    :param beta:
    :param maximizing_player:
    :param branch_factor:
    :param eval_level:
    :param model:
    :param scaler:
    :return:
    """
    if depth == 0 or board_game.is_game_over():
        return board_game.evaluate_board(), None

    best_move = None

    # Sort moves based on heuristic evaluation at level l to pick the most promising ones
    moves = list(board_game.legal_moves)
    random.shuffle(moves)
    moves = sorted(moves, key=lambda move: predict_board_l(move, eval_level, board_game, alpha, beta, maximizing_player, branch_factor, model, scaler), reverse=maximizing_player)
    moves = moves[:branch_factor]  # Limit to top-N moves

    if maximizing_player:
        max_eval = -math.inf
        for move in moves:
            board_game.make_move(move)
            eval, _ = pred_bl_minmax(board_game, depth - 1, alpha, beta, False, branch_factor, model, scaler)
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
    for move in moves:
        board_game.make_move(move)
        eval, _ = pred_bl_minmax(board_game, depth - 1, alpha, beta, True, branch_factor, model, scaler)
        board_game.take_back_last_move()

        if eval <= min_eval:  # the '=' avoids having move set to None because there is no best move
            min_eval = eval
            best_move = move

        beta = min(beta, eval)
        if beta <= alpha:
            break

    return min_eval, best_move
