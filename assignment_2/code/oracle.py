import numpy as np
from trainer import POSITIVE_INFINITE_PLACEHOLDER, NEGATIVE_INFINITE_PLACEHOLDER


def predict_HL(board_game, model, scaler):
    """
        Use a trained model to predict the evaluation of the board.
    """
    eval = board_game.evaluate_board()
    # Replace NaN and inf with a valid value (e.g., 0 or mean)
    eval = np.nan_to_num(eval, nan=0.0, posinf=POSITIVE_INFINITE_PLACEHOLDER, neginf=NEGATIVE_INFINITE_PLACEHOLDER)
    H0_input = np.array([eval])
    H0_input = H0_input.reshape(-1, 1)
    H0_input_scaled = scaler.transform(H0_input)
    HL_predicted = model.predict(H0_input_scaled)
    return HL_predicted[0]

def predict_HL_extended(board_game, model, scaler):
    """
        Use a trained model to predict the evaluation of the board.
    """
    H0 = board_game.evaluate_board()
    # Replace NaN and inf with a valid value (e.g., 0 or mean)
    H0 = np.nan_to_num(H0, nan=0.0, posinf=POSITIVE_INFINITE_PLACEHOLDER, neginf=NEGATIVE_INFINITE_PLACEHOLDER)
    material_balance, piece_square_table, king_safety, center_control, pawn_structure, piece_activity, checks = board_game.compute_heuristics()

    input = np.array([H0, material_balance, piece_square_table, king_safety, center_control, pawn_structure, piece_activity, checks])
    input = input.reshape(1, -1)
    input_scaled = scaler.transform(input)
    HL_predicted = model.predict(input_scaled)
    return HL_predicted[0]
