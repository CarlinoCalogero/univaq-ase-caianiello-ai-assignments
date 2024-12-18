import math
import random
import numpy as np


def predict_board(board_game, model, scaler):
    """
        Use a trained model to predict the evaluation of the board.
    """
    eval = board_game.evaluate_board()
    # Replace NaN and inf with a valid value (e.g., 0 or mean)
    eval = np.nan_to_num(eval, nan=0.0, posinf=np.finfo(np.float64).max, neginf=np.finfo(np.float64).min)
    H0_input = np.array([eval])
    H0_input = H0_input.reshape(-1, 1)
    H0_input_scaled = scaler.transform(H0_input)
    HL_predicted = model.predict(H0_input_scaled)
    return HL_predicted


# MinMax algorithm with alpha beta pruning implementation
def pred_bl_minmax(board_game, depth, alpha, beta, maximizing_player, branch_factor, model, scaler):
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
        return predict_board(board_game, model, scaler), None

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
