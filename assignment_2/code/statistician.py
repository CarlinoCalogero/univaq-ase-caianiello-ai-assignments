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
import random

AB_MINMAX_VS_BL_MINMAX_EXPERIMENT_KEY = "ab_minmax_vs_bl_minmax"
ELAPSED_TIME_EXPERIMENT_KEY = "elapsed_time"
BEST_MOVE_EXPERIMENT_KEY = "best_move"
H0_EXPERIMENT_KEY = "H0"
HL_EXPERIMENT_KEY = "HL"
AB_MINMAX_KEY = "ab_minmax"
BL_MINMAX_KEY = "bl_minmax"
L_KEY = "L"
BRANCH_FACTOR_KEY = "branch_factor"


def plot_stacked_bar_plot(bar_1_x_values, bar_1_y_values, bar_2_x_values, bar_2_y_values, bar_1_label, bar_2_label,
                          xlabel, ylabel, title):
    fig, ax = plt.subplots()
    ax.bar(x=bar_1_x_values, height=bar_1_y_values, label=bar_1_label, color='orange')
    ax.bar(x=bar_2_x_values, height=bar_2_y_values, label=bar_2_label, color='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


def plot_lines_plot(lines_x_points_list, lines_y_points_list, lines_point_labels, xlabel, ylabel, title):
    fig, ax = plt.subplots()
    for index in range(len(lines_x_points_list)):
        line_x_points = lines_x_points_list[index]
        line_y_points = lines_y_points_list[index]
        label = lines_point_labels[index]
        ax.plot(line_x_points, line_y_points, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


def plot_scatter_plot(lines_x_points_list, lines_y_points_list, lines_point_labels, xlabel, ylabel, title,
                      y_ticks=None):
    fig, ax = plt.subplots()
    for index in range(len(lines_x_points_list)):
        line_x_points = lines_x_points_list[index]
        line_y_points = lines_y_points_list[index]
        label = lines_point_labels[index]
        ax.scatter(line_x_points, line_y_points, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    if y_ticks is not None:
        plt.yticks(y_ticks, [str(y_tick) for y_tick in y_ticks])
    plt.show()


def add_to_plot_dictionary(L_and_branch_factor_pair, plot_dictionary, plot_dictionary_parameter_key, row, row_value_1,
                           row_value_2):
    if L_and_branch_factor_pair not in plot_dictionary[plot_dictionary_parameter_key]:
        plot_dictionary[plot_dictionary_parameter_key][L_and_branch_factor_pair] = {
            L_KEY: row.L,
            BRANCH_FACTOR_KEY: row.branch_factor,
            AB_MINMAX_KEY: [],
            BL_MINMAX_KEY: []
        }
    plot_dictionary[plot_dictionary_parameter_key][L_and_branch_factor_pair][AB_MINMAX_KEY].append(row_value_1)
    plot_dictionary[plot_dictionary_parameter_key][L_and_branch_factor_pair][BL_MINMAX_KEY].append(row_value_2)


def plot_ab_minmax_vs_bl_minmax_experiment_results_data(test_results_folder):
    file_path = f"{test_results_folder}{AB_MINMAX_VS_BL_MINMAX_EXPERIMENT_KEY}.csv"
    df = read_csv_as_dataframe(file_path)

    plot_dictionary = {
        H0_EXPERIMENT_KEY: {},
        ELAPSED_TIME_EXPERIMENT_KEY: {},
        HL_EXPERIMENT_KEY: {},
        BEST_MOVE_EXPERIMENT_KEY: {}
    }

    for row in df.itertuples():
        L_and_branch_factor_pair = f"({row.L},{row.branch_factor})"

        if L_and_branch_factor_pair not in plot_dictionary[H0_EXPERIMENT_KEY]:
            plot_dictionary[H0_EXPERIMENT_KEY][L_and_branch_factor_pair] = []
        plot_dictionary[H0_EXPERIMENT_KEY][L_and_branch_factor_pair].append(row.H0)

        add_to_plot_dictionary(
            L_and_branch_factor_pair,
            plot_dictionary,
            ELAPSED_TIME_EXPERIMENT_KEY,
            row,
            row.ab_minmax_elapsed_time,
            row.bl_minmax_elapsed_time
        )

        add_to_plot_dictionary(
            L_and_branch_factor_pair,
            plot_dictionary,
            HL_EXPERIMENT_KEY,
            row,
            row.ab_minmax_HL,
            row.bl_minmax_HL
        )

        add_to_plot_dictionary(
            L_and_branch_factor_pair,
            plot_dictionary,
            BEST_MOVE_EXPERIMENT_KEY,
            row,
            row.ab_minmax_best_move,
            row.bl_minmax_best_move
        )

    for key in plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]:
        L_and_branch_factor_pair_elapsed_time_test_results = plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY][key]
        plot_stacked_bar_plot(
            [i for i in range(len(L_and_branch_factor_pair_elapsed_time_test_results[BL_MINMAX_KEY]))],
            L_and_branch_factor_pair_elapsed_time_test_results[BL_MINMAX_KEY],
            [i for i in range(len(L_and_branch_factor_pair_elapsed_time_test_results[AB_MINMAX_KEY]))],
            L_and_branch_factor_pair_elapsed_time_test_results[AB_MINMAX_KEY],
            "blMinMax",
            "abMinMax",
            "Number of tests",
            "Time",
            f"Execution Times for L={L_and_branch_factor_pair_elapsed_time_test_results[L_KEY]} and branch_factor={L_and_branch_factor_pair_elapsed_time_test_results[BRANCH_FACTOR_KEY]}"
        )

        L_and_branch_factor_pair_HL_test_results = plot_dictionary[HL_EXPERIMENT_KEY][key]
        plot_lines_plot(
            [
                [i for i in range(len(plot_dictionary[H0_EXPERIMENT_KEY][key]))],
                [i for i in range(len(L_and_branch_factor_pair_HL_test_results[AB_MINMAX_KEY]))],
                [i for i in range(len(L_and_branch_factor_pair_HL_test_results[BL_MINMAX_KEY]))]
            ],
            [
                plot_dictionary[H0_EXPERIMENT_KEY][key],
                L_and_branch_factor_pair_HL_test_results[AB_MINMAX_KEY],
                L_and_branch_factor_pair_HL_test_results[BL_MINMAX_KEY]
            ],
            [
                "H0",
                "abMinMax",
                "blMinMax"
            ],
            "Number of tests",
            "HL",
            f"HL for L={L_and_branch_factor_pair_HL_test_results[L_KEY]} and branch_factor={L_and_branch_factor_pair_HL_test_results[BRANCH_FACTOR_KEY]}"
        )

        L_and_branch_factor_pair_best_move_test_results = plot_dictionary[BEST_MOVE_EXPERIMENT_KEY][key]
        shrunk_number_of_test = [i for i in range(len(L_and_branch_factor_pair_HL_test_results[AB_MINMAX_KEY]) // 30)]
        shrunk_ab_minmax_best_moves_list = [L_and_branch_factor_pair_best_move_test_results[AB_MINMAX_KEY][i] for i in shrunk_number_of_test]
        shrunk_bl_minmax_best_moves_list = [L_and_branch_factor_pair_best_move_test_results[BL_MINMAX_KEY][i] for i in shrunk_number_of_test]
        y_ticks = shrunk_ab_minmax_best_moves_list + shrunk_bl_minmax_best_moves_list
        random.shuffle(y_ticks)
        plot_scatter_plot(
            [
                shrunk_number_of_test,
                shrunk_number_of_test
            ],
            [
                shrunk_ab_minmax_best_moves_list,
                shrunk_bl_minmax_best_moves_list
            ],
            [
                "abMinMax",
                "blMinMax"
            ],
            "Number of tests",
            "Best Move",
            f"Best moves for L={L_and_branch_factor_pair_HL_test_results[L_KEY]} and branch_factor={L_and_branch_factor_pair_HL_test_results[BRANCH_FACTOR_KEY]}",
            y_ticks
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
