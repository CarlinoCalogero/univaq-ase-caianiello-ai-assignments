from game_setter import start_random_game
from ab_minmax import ab_minmax
from bl_minmax import bl_minmax
import math
import time
from tqdm import tqdm
from printer import write_csv_file
import itertools


def generate_combinations_from_two_lists(list_1, list_2):
    # It generates all possible combinations of elements from both lists
    # Convert the result into a list of tuples
    return list(itertools.product(list_1, list_2))


def ab_minmax_vs_bl_minmax_experiment(number_of_tests, test_results_folder, L_min_value, L_max_value,
                                      branch_factor_min_value, branch_factor_max_value):
    if L_min_value == 0:
        raise Exception("Error! L_min_value equal to 0 does not make sense! It's just a static evaluation!")
    if L_min_value < 0:
        raise Exception("Error! L_min_value lower than 0 does not make sense!")
    if branch_factor_min_value < 1:
        raise Exception("Error! branch_factor_min_value lower than 1 does not make sense!")

    L_inteval = [num for num in range(L_min_value, L_max_value + 1)]
    branch_factor_interval = [num for num in range(branch_factor_min_value, branch_factor_max_value + 1)]

    combinations = generate_combinations_from_two_lists(L_inteval, branch_factor_interval)

    for combination in tqdm(combinations, desc=f"Running tests..."):
        ab_minmax_vs_bl_minmax(number_of_tests, test_results_folder, combination[0], combination[1])


def ab_minmax_vs_bl_minmax(number_of_tests, test_results_folder, L, branch_factor):
    for _ in range(number_of_tests):
        board_game = start_random_game()

        starting_board_fen = board_game.fen

        H0 = board_game.evaluate_board()

        start_time = time.time()
        ab_minmax_HL, ab_minmax_best_move = ab_minmax(board_game, L, math.inf, math.inf, True)
        ab_minmax_elapsed_time = time.time() - start_time

        start_time = time.time()
        bl_minmax_HL, bl_minmax_best_move = bl_minmax(board_game, L, math.inf, math.inf, True, branch_factor)
        bl_minmax_elapsed_time = time.time() - start_time

        file_path = f"{test_results_folder}ab_minmax_vs_bl_minmax"
        write_csv_file(
            file_path,
            [
                'starting_board_fen',
                'H0',
                'L',
                'branch_factor',
                'ab_minmax_HL',
                'bl_minmax_HL',
                'ab_minmax_best_move',
                'bl_minmax_best_move',
                'ab_minmax_elapsed_time',
                'bl_minmax_elapsed_time'
            ],
            [
                starting_board_fen,
                H0,
                L,
                branch_factor,
                ab_minmax_HL,
                bl_minmax_HL,
                ab_minmax_best_move,
                bl_minmax_best_move,
                ab_minmax_elapsed_time,
                bl_minmax_elapsed_time
            ]
        )
