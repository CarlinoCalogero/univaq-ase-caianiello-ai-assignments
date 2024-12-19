from game_setter import start_random_game
from ab_minmax import ab_minmax
from bl_minmax import bl_minmax
import math
import time
from tqdm import tqdm
from printer import write_csv_file
from itertools import product
import matplotlib.pyplot as plt
from reader import read_csv_as_dataframe
import random
from bl_minmax_l import bl_minmax_l
import randomcolor
from trainer import train_mlp_regressor
from pred_minmax import pred_minmax
from oracle import predict_HL

AB_MINMAX_VS_BL_MINMAX_EXPERIMENT_KEY = "ab_minmax_vs_bl_minmax"
BL_MINMAX_L_OPTIMAL_L_EXPERIMENT_KEY = "bl_minmax_l_optimal_l"
BL_MINMAX_L_DIFFERENT_CHOICE_OF_L_EXPERIMENT_KEY = "bl_minmax_l_different_choice_of_l"
PRED_MINMAX_VS_AB_MINMAX_EXPERIMENT_KEY = "pred_minmax_vs_ab_minmax"
ELAPSED_TIME_EXPERIMENT_KEY = "elapsed_time"
BEST_MOVE_EXPERIMENT_KEY = "best_move"
H0_EXPERIMENT_KEY = "H0"
HL_EXPERIMENT_KEY = "HL"
AB_MINMAX_KEY = "ab_minmax"
BL_MINMAX_KEY = "bl_minmax"
L_KEY = "L"
BRANCH_FACTOR_KEY = "branch_factor"
l_KEY = "l"
VALUES_KEY = "values"


def plot_stacked_bar_plot(bar_1_x_values, bar_1_y_values, bar_2_x_values, bar_2_y_values, bar_1_label, bar_2_label,
                          xlabel, ylabel, title):
    fig, ax = plt.subplots()
    ax.bar(x=bar_1_x_values, height=bar_1_y_values, label=bar_1_label, color='orange')
    ax.bar(x=bar_2_x_values, height=bar_2_y_values, label=bar_2_label, color='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Adjust position
    plt.show()


def plot_bar_plot(bars_x_points, bars_y_points, bar_labels, xlabel, ylabel, title):
    colors = []
    fig, ax = plt.subplots()
    for index in range(len(bars_x_points)):
        line_x_points = bars_x_points[index]
        line_y_points = bars_y_points[index]
        label = bar_labels[index]
        while True:
            color = randomcolor.RandomColor().generate()
            if color not in colors:
                colors.append(color)
                break
        ax.bar(line_x_points, line_y_points, label=label, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Adjust position
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
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Adjust position
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
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Adjust position
    if y_ticks is not None:
        plt.yticks(y_ticks, [str(y_tick) for y_tick in y_ticks])
    plt.show()


def add_to_ab_minmax_vs_bl_minmax_experiment_plot_dictionary(L_and_branch_factor_pair, plot_dictionary,
                                                             plot_dictionary_parameter_key, row, row_value_1,
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

        add_to_ab_minmax_vs_bl_minmax_experiment_plot_dictionary(
            L_and_branch_factor_pair,
            plot_dictionary,
            ELAPSED_TIME_EXPERIMENT_KEY,
            row,
            row.ab_minmax_elapsed_time,
            row.bl_minmax_elapsed_time
        )

        add_to_ab_minmax_vs_bl_minmax_experiment_plot_dictionary(
            L_and_branch_factor_pair,
            plot_dictionary,
            HL_EXPERIMENT_KEY,
            row,
            row.ab_minmax_HL,
            row.bl_minmax_HL
        )

        add_to_ab_minmax_vs_bl_minmax_experiment_plot_dictionary(
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
        shrunk_ab_minmax_best_moves_list = [L_and_branch_factor_pair_best_move_test_results[AB_MINMAX_KEY][i] for i in
                                            shrunk_number_of_test]
        shrunk_bl_minmax_best_moves_list = [L_and_branch_factor_pair_best_move_test_results[BL_MINMAX_KEY][i] for i in
                                            shrunk_number_of_test]
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


def add_to_bl_minmax_l_optimal_l_experiment_plot_dictionary(plot_dictionary, plot_dictionary_parameter_key, row,
                                                            row_value):
    if row.l not in plot_dictionary[plot_dictionary_parameter_key]:
        plot_dictionary[plot_dictionary_parameter_key][row.l] = []
    plot_dictionary[plot_dictionary_parameter_key][row.l].append(row_value)


def plot_bl_minmax_l_optimal_l_experiment_results_data(test_results_folder):
    file_path = f"{test_results_folder}{BL_MINMAX_L_OPTIMAL_L_EXPERIMENT_KEY}.csv"
    df = read_csv_as_dataframe(file_path)

    plot_dictionary = {
        H0_EXPERIMENT_KEY: {},
        ELAPSED_TIME_EXPERIMENT_KEY: {},
        HL_EXPERIMENT_KEY: {},
        BEST_MOVE_EXPERIMENT_KEY: {}
    }

    for row in df.itertuples():
        if L_KEY not in plot_dictionary:
            plot_dictionary[L_KEY]: row.L

        if BRANCH_FACTOR_KEY not in plot_dictionary:
            plot_dictionary[BRANCH_FACTOR_KEY]: row.branch_factor

        if row.l not in plot_dictionary[H0_EXPERIMENT_KEY]:
            plot_dictionary[H0_EXPERIMENT_KEY][row.l] = []
        plot_dictionary[H0_EXPERIMENT_KEY][row.l].append(row.H0)

        add_to_bl_minmax_l_optimal_l_experiment_plot_dictionary(
            plot_dictionary,
            ELAPSED_TIME_EXPERIMENT_KEY,
            row,
            row.elapsed_time,
        )

        add_to_bl_minmax_l_optimal_l_experiment_plot_dictionary(
            plot_dictionary,
            HL_EXPERIMENT_KEY,
            row,
            row.HL
        )

        add_to_bl_minmax_l_optimal_l_experiment_plot_dictionary(
            plot_dictionary,
            BEST_MOVE_EXPERIMENT_KEY,
            row,
            row.best_move
        )

    plot_lines_plot(
        [
            [l_value for l_value in plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]],
        ],
        [
            [sum(plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY][l_value]) / len(
                plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY][l_value]) for l_value in
             plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]],  # average
        ],
        [
            "Average Elapsed Time",
        ],
        "l",
        "Time",
        f"Average elapsed time"
    )

    plot_bar_plot(
        [
            [l_value] for l_value in plot_dictionary[HL_EXPERIMENT_KEY]
        ],
        [
            [sum(plot_dictionary[HL_EXPERIMENT_KEY][l_value]) / len(plot_dictionary[HL_EXPERIMENT_KEY][l_value])] for
            l_value in plot_dictionary[HL_EXPERIMENT_KEY]  # average
        ],
        [
            [f"l={l_value}"] for l_value in plot_dictionary[HL_EXPERIMENT_KEY]
        ],
        "l",
        "HL",
        f"Average HL"
    )

    for l_value in plot_dictionary[HL_EXPERIMENT_KEY]:
        l_value_HL_test_results = plot_dictionary[HL_EXPERIMENT_KEY][l_value]
        plot_lines_plot(
            [
                [i for i in range(len(plot_dictionary[H0_EXPERIMENT_KEY][l_value]))],
                [i for i in range(len(l_value_HL_test_results))],
            ],
            [
                plot_dictionary[H0_EXPERIMENT_KEY][l_value],
                l_value_HL_test_results,
            ],
            [
                "H0",
                "HL"
            ],
            "Number of tests",
            "HL",
            f"HL for l={l_value}"
        )


def add_to_bl_minmax_l_different_choice_of_l_experiment_plot_dictionary(L_and_l_pair, plot_dictionary,
                                                                        plot_dictionary_parameter_key, row, row_value):
    if L_and_l_pair not in plot_dictionary[plot_dictionary_parameter_key]:
        plot_dictionary[plot_dictionary_parameter_key][L_and_l_pair] = {
            L_KEY: row.L,
            l_KEY: row.l,
            VALUES_KEY: [],
        }
    plot_dictionary[plot_dictionary_parameter_key][L_and_l_pair][VALUES_KEY].append(row_value)


def plot_bl_minmax_l_different_choice_of_l_experiment_results_data(test_results_folder):
    file_path = f"{test_results_folder}{BL_MINMAX_L_DIFFERENT_CHOICE_OF_L_EXPERIMENT_KEY}.csv"
    df = read_csv_as_dataframe(file_path)

    plot_dictionary = {
        H0_EXPERIMENT_KEY: {},
        ELAPSED_TIME_EXPERIMENT_KEY: {},
        HL_EXPERIMENT_KEY: {},
        BEST_MOVE_EXPERIMENT_KEY: {}
    }

    for row in df.itertuples():
        if BRANCH_FACTOR_KEY not in plot_dictionary:
            plot_dictionary[BRANCH_FACTOR_KEY]: row.branch_factor

        L_and_l_pair = f"({row.L},{row.l})"

        if L_and_l_pair not in plot_dictionary[H0_EXPERIMENT_KEY]:
            plot_dictionary[H0_EXPERIMENT_KEY][L_and_l_pair] = []
        plot_dictionary[H0_EXPERIMENT_KEY][L_and_l_pair].append(row.H0)

        add_to_bl_minmax_l_different_choice_of_l_experiment_plot_dictionary(
            L_and_l_pair,
            plot_dictionary,
            ELAPSED_TIME_EXPERIMENT_KEY,
            row,
            row.elapsed_time
        )

        add_to_bl_minmax_l_different_choice_of_l_experiment_plot_dictionary(
            L_and_l_pair,
            plot_dictionary,
            HL_EXPERIMENT_KEY,
            row,
            row.HL
        )

        add_to_bl_minmax_l_different_choice_of_l_experiment_plot_dictionary(
            L_and_l_pair,
            plot_dictionary,
            BEST_MOVE_EXPERIMENT_KEY,
            row,
            row.best_move
        )

    plot_lines_plot(
        [
            [L_and_l_pair for L_and_l_pair in plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]],
        ],
        [
            [sum(plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY][L_and_l_pair][VALUES_KEY]) / len(
                plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY][L_and_l_pair][VALUES_KEY]) for L_and_l_pair in
             plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]],  # average
        ],
        [
            "Average Elapsed Time",
        ],
        "(L,l)",
        "Time",
        f"Average elapsed time"
    )

    plot_bar_plot(
        [
            [L_and_l_pair] for L_and_l_pair in plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]
        ],
        [
            [sum(plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY][L_and_l_pair][VALUES_KEY]) / len(
                plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY][L_and_l_pair][VALUES_KEY])] for L_and_l_pair in
            plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]  # average
        ],
        [
            [L_and_l_pair] for L_and_l_pair in plot_dictionary[HL_EXPERIMENT_KEY]
        ],
        "(L,l)",
        "Time",
        f"Average elapsed time"
    )

    plot_bar_plot(
        [
            [L_and_l_pair] for L_and_l_pair in plot_dictionary[HL_EXPERIMENT_KEY]
        ],
        [
            [sum(plot_dictionary[HL_EXPERIMENT_KEY][L_and_l_pair][VALUES_KEY]) / len(
                plot_dictionary[HL_EXPERIMENT_KEY][L_and_l_pair][VALUES_KEY])] for
            L_and_l_pair in plot_dictionary[HL_EXPERIMENT_KEY]  # average
        ],
        [
            [L_and_l_pair] for L_and_l_pair in plot_dictionary[HL_EXPERIMENT_KEY]
        ],
        "(L,l)",
        "HL",
        f"Average HL"
    )

    for key in plot_dictionary[ELAPSED_TIME_EXPERIMENT_KEY]:
        L_and_l_pair_HL_test_results = plot_dictionary[HL_EXPERIMENT_KEY][key]
        plot_lines_plot(
            [
                [i for i in range(len(plot_dictionary[H0_EXPERIMENT_KEY][key]))],
                [i for i in range(len(L_and_l_pair_HL_test_results[VALUES_KEY]))],
            ],
            [
                plot_dictionary[H0_EXPERIMENT_KEY][key],
                L_and_l_pair_HL_test_results[VALUES_KEY],
            ],
            [
                "H0",
                "HL",
            ],
            "Number of tests",
            "HL",
            f"HL for L={L_and_l_pair_HL_test_results[L_KEY]} and l={L_and_l_pair_HL_test_results[l_KEY]}"
        )


def generate_combinations_from_n_lists(*lists):
    """
        Generate all possible combinations from n lists.

        Parameters:
            *lists: Variable number of lists as input.

        Returns:
            A list of tuples, where each tuple is a combination of one element from each input list.
        """
    return list(product(*lists))


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

    combinations = generate_combinations_from_n_lists(L_interval, branch_factor_interval)

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


def bl_minmax_l_different_choice_of_l_experiment(number_of_tests, test_results_folder, L_min_value, L_max_value,
                                                 branch_factor_min_value, branch_factor_max_value):
    validate_L(L_min_value)
    validate_branch_factor(branch_factor_min_value)

    L_interval = get_numbers_in_interval(L_min_value, L_max_value)
    branch_factor_interval = get_numbers_in_interval(branch_factor_min_value, branch_factor_max_value)
    l_interval = get_numbers_in_interval(1, max(1, L_max_value - 1))

    combinations = generate_combinations_from_n_lists(L_interval, branch_factor_interval, l_interval)

    for combination in tqdm(combinations, desc=f"Running tests..."):
        bl_minmax_l_experiment(number_of_tests, test_results_folder, BL_MINMAX_L_DIFFERENT_CHOICE_OF_L_EXPERIMENT_KEY,
                               combination[0], combination[1], combination[2])


def bl_minmax_l_optimal_l_experiment(number_of_tests, test_results_folder, L=10, branch_factor=3):
    l_interval = get_numbers_in_interval(1, max(1, L - 1))

    combinations = generate_combinations_from_n_lists(L, branch_factor, l_interval)

    for combination in tqdm(combinations, desc=f"Running tests..."):
        bl_minmax_l_experiment(number_of_tests, test_results_folder, BL_MINMAX_L_OPTIMAL_L_EXPERIMENT_KEY,
                               combination[0], combination[1], combination[2])


def bl_minmax_l_experiment(number_of_tests, test_results_folder, test_results_file_name, L, branch_factor, l):
    for _ in range(number_of_tests):
        board_game = start_random_game()

        starting_board_fen = board_game.fen

        H0 = board_game.evaluate_board()

        start_time = time.time()
        HL, best_move = bl_minmax_l(board_game, L, math.inf, math.inf, True, branch_factor, l)
        elapsed_time = time.time() - start_time

        file_path = f"{test_results_folder}{test_results_file_name}"
        write_csv_file(
            file_path,
            [
                'starting_board_fen',
                'H0',
                'L',
                'branch_factor',
                'l',
                'HL',
                'best_move',
                'elapsed_time',
            ],
            [
                starting_board_fen,
                H0,
                L,
                branch_factor,
                l,
                HL,
                best_move,
                elapsed_time,
            ]
        )


def pred_minmax_vs_ab_minmax_experiment(number_of_tests, test_results_folder,
                                        branch_factor_min_value, branch_factor_max_value):

    L = 3  # to generate the dataset on which train the regressor an L=3 value was used, so it must not be changed

    validate_branch_factor(branch_factor_min_value)

    branch_factor_interval = get_numbers_in_interval(branch_factor_min_value, branch_factor_max_value)

    combinations = generate_combinations_from_n_lists([L], branch_factor_interval)

    mlp_regressor, scaler = train_mlp_regressor("./dataset.csv")

    for combination in tqdm(combinations, desc=f"Running tests..."):
        pred_minmax_vs_ab_minmax(number_of_tests, test_results_folder, combination[0], combination[1], mlp_regressor,
                                 scaler)


def pred_minmax_vs_ab_minmax(number_of_tests, test_results_folder, L, branch_factor, mlp_regressor, scaler):
    for _ in range(number_of_tests):
        board_game = start_random_game()

        starting_board_fen = board_game.fen

        H0 = board_game.evaluate_board()

        start_time = time.time()
        pred_minmax_HL, pred_minmax_best_move = pred_minmax(board_game, L, math.inf, math.inf, True, mlp_regressor,
                                                            scaler, predict_HL)
        pred_minmax_elapsed_time = time.time() - start_time

        start_time = time.time()
        ab_minmax_HL, ab_minmax_best_move = ab_minmax(board_game, L, math.inf, math.inf, True)
        ab_minmax_elapsed_time = time.time() - start_time

        file_path = f"{test_results_folder}{PRED_MINMAX_VS_AB_MINMAX_EXPERIMENT_KEY}"
        write_csv_file(
            file_path,
            [
                'starting_board_fen',
                'H0',
                'L',
                'branch_factor',
                'pred_minmax_HL',
                'ab_minmax_HL',
                'pred_minmax_best_move',
                'ab_minmax_best_move',
                'pred_minmax_elapsed_time',
                'ab_minmax_elapsed_time'
            ],
            [
                starting_board_fen,
                H0,
                L,
                branch_factor,
                pred_minmax_HL,
                ab_minmax_HL,
                pred_minmax_best_move,
                ab_minmax_best_move,
                pred_minmax_elapsed_time,
                ab_minmax_elapsed_time
            ]
        )
