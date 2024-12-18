import math
import random


# MinMax algorithm with alpha beta pruning implementation
def pred_bl_minmax(board_game, depth, alpha, beta, maximizing_player, branch_factor, model, scaler, predict_board_function):
    """
    Branch-limited MinMax with alpha beta pruning algorithm implementation
    :param board_game:
    :param depth:
    :param alpha:
    :param beta:
    :param maximizing_player:
    :param branch_factor:
    :param model:
    :param scaler:
    :return:
    """
    if depth == 0 or board_game.is_game_over():
        return predict_board_function(board_game, model, scaler), None

    best_move = None

    # Sort moves based on heuristic evaluation to pick the most promising ones
    moves = list(board_game.legal_moves)
    random.shuffle(moves)
    moves = sorted(moves, key=lambda move: board_game.evaluate_move(move), reverse=maximizing_player)
    moves = moves[:branch_factor]  # Limit to top-N moves

    if maximizing_player:
        max_eval = -math.inf
        for move in moves:
            board_game.make_move(move)
            eval, _ = pred_bl_minmax(board_game, depth - 1, alpha, beta, False, branch_factor, model, scaler, predict_board_function)
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
        eval, _ = pred_bl_minmax(board_game, depth - 1, alpha, beta, True, branch_factor, model, scaler, predict_board_function)
        board_game.take_back_last_move()

        if eval <= min_eval:  # the '=' avoids having move set to None because there is no best move
            min_eval = eval
            best_move = move

        beta = min(beta, eval)
        if beta <= alpha:
            break

    return min_eval, best_move
