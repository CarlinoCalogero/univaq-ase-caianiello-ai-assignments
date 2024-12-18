from game_setter import start_random_game
from ab_minmax import ab_minmax
from bl_minmax import bl_minmax
import math
import time
from tqdm import tqdm
from printer import write_csv_file
import itertools
import matplotlib.pyplot as plt
from reader import read_csv_as_dataframe

AB_MINMAX_VS_BL_MINMAX_EXPERIMENT_KEY = "ab_minmax_vs_bl_minmax"
AB_MINMAX_KEY = "ab_minmax"
BL_MINMAX_KEY = "bl_minmax"
L_KEY = "L"
BRANCH_FACTOR_KEY = "branch_factor"


def plot_stacked_bar_plot(bar_1_values, bar_2_values, bar_1_label, bar_2_label, xlabel, ylabel, title):
    fig, ax = plt.subplots()
    ax.bar(x=[i for i in range(len(bar_1_values))], height=bar_1_values, label=bar_1_label, color='orange')
    ax.bar(x=[i for i in range(len(bar_2_values))], height=bar_2_values, label=bar_2_label, color='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


def plot_ab_minmax_vs_bl_minmax_experiment_results_data(test_results_folder):
    file_path = f"{test_results_folder}{AB_MINMAX_VS_BL_MINMAX_EXPERIMENT_KEY}.csv"
    df = read_csv_as_dataframe(file_path)

    plot_dictionary = {}

    for row in df.itertuples():
        L_and_branch_factor_pair = f"({row.L},{row.branch_factor})"
        if L_and_branch_factor_pair not in plot_dictionary:
            plot_dictionary[L_and_branch_factor_pair] = {
                L_KEY: row.L,
                BRANCH_FACTOR_KEY: row.branch_factor,
                AB_MINMAX_KEY: [],
                BL_MINMAX_KEY: []
            }
        plot_dictionary[L_and_branch_factor_pair][AB_MINMAX_KEY].append(row.ab_minmax_elapsed_time)
        plot_dictionary[L_and_branch_factor_pair][BL_MINMAX_KEY].append(row.bl_minmax_elapsed_time)

    for key in plot_dictionary:
        L_and_branch_factor_pair_test_results = plot_dictionary[key]
        plot_stacked_bar_plot(
            L_and_branch_factor_pair_test_results[BL_MINMAX_KEY],
            L_and_branch_factor_pair_test_results[AB_MINMAX_KEY],
            "blMinMax",
            "abMinMax",
            "Number of tests",
            "Time",
            f"Execution Times for L={L_and_branch_factor_pair_test_results[L_KEY]} and branch_factor={L_and_branch_factor_pair_test_results[BRANCH_FACTOR_KEY]}"
        )


def generate_combinations_from_two_lists(list_1, list_2):
    # It generates all possible combinations of elements from both lists
    # Convert the result into a list of tuples
    return list(itertools.product(list_1, list_2))


def validate_L(L_min_value):
    if L_min_value == 0:
        raise Exception("Error! L_min_value equal to 0 does not make sense! It's just a static evaluation!")
    if L_min_value < 0:
        raise Exception("Error! L_min_value lower than 0 does not make sense!")


def validate_branch_factor(branch_factor_min_value):
    if branch_factor_min_value < 1:
        raise Exception("Error! branch_factor_min_value lower than 1 does not make sense!")


def get_numbers_in_interval(min_value, max_value):
    return [num for num in range(min_value, max_value + 1)]


def ab_minmax_vs_bl_minmax_experiment(number_of_tests, test_results_folder, L_min_value, L_max_value,
                                      branch_factor_min_value, branch_factor_max_value):
    validate_L(L_min_value)
    validate_branch_factor(branch_factor_min_value)

    L_interval = get_numbers_in_interval(L_min_value, L_max_value)
    branch_factor_interval = get_numbers_in_interval(branch_factor_min_value, branch_factor_max_value)

    combinations = generate_combinations_from_two_lists(L_interval, branch_factor_interval)

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

        file_path = f"{test_results_folder}{AB_MINMAX_VS_BL_MINMAX_EXPERIMENT_KEY}"
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
