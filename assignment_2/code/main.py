import chess_game
from game_setter import start_random_game
from ab_minmax import ab_minmax
from bl_minmax import bl_minmax
from bl_minmax_l import bl_minmax_l
import math
from scorekeeper import Scorekeeper
from tqdm import tqdm
from data_analyst import generate_dataset, generate_extended_dataset
from reader import read_csv_file_as_dictionary
from printer import write_json_file
from trainer import train_mlp_regressor, train_mlp_regressor_with_extended_dataset
from pred_minmax import pred_minmax
from pred_bl_minmax_l import pred_bl_minmax_l
from oracle import predict_HL, predict_HL_extended
from statistician import ab_minmax_vs_bl_minmax_experiment, plot_ab_minmax_vs_bl_minmax_experiment_results_data, bl_minmax_l_optimal_l_experiment


def dummy_function():
    for _ in tqdm(range(1000), desc="Playing matches..."):

        board_game = start_random_game()

        # print(f"[FEN \"{board_game.fen}\"]")
        scorekeeper = Scorekeeper()
        scorekeeper.set_game_board_to_be_tracked(board_game)
        scorekeeper.record_fen()

        move_counter = 1

        while True:
            if board_game.is_game_over():
                break

            if board_game.turn == chess_game.WHITE:
                eval, move = ab_minmax(board_game, 3, math.inf, math.inf, True)
            else:
                eval, move = bl_minmax(board_game, 3, math.inf, math.inf, True, 5)

            board_game.make_move(move)

            # print(f"{move_counter}. {move}")
            scorekeeper.record_move(move)

            move_counter = move_counter + 1

        # print(board_game.board.outcome())
        scorekeeper.record_outcome()

        scorekeeper.record_game("./games/")
        scorekeeper.clear_records()


def dummy_regressor_function():
    mlp_regressor, scaler = train_mlp_regressor("./dataset.csv")

    for _ in tqdm(range(10), desc="Playing matches..."):

        board_game = start_random_game()

        # print(f"[FEN \"{board_game.fen}\"]")
        scorekeeper = Scorekeeper()
        scorekeeper.set_game_board_to_be_tracked(board_game)
        scorekeeper.record_fen()

        move_counter = 1

        while True:
            if board_game.is_game_over():
                break

            if board_game.turn == chess_game.WHITE:
                eval, move = ab_minmax(board_game, 3, math.inf, math.inf, True)
            else:
                eval, move = pred_minmax(board_game, 2, -math.inf, math.inf, True, mlp_regressor, scaler, predict_HL)
                # eval, move = pred_bl_minmax_l(board_game, 2, -math.inf, math.inf, True, 5, 1, mlp_regressor, scaler, predict_HL)

            board_game.make_move(move)

            # print(f"{move_counter}. {move}")
            scorekeeper.record_move(move)

            move_counter = move_counter + 1

        # print(board_game.board.outcome())
        scorekeeper.record_outcome()

        scorekeeper.record_game("./games/")
        scorekeeper.clear_records()


def dummy_extended_regressor_function():
    mlp_regressor, scaler = train_mlp_regressor_with_extended_dataset("./extended_dataset.csv")

    for _ in tqdm(range(10), desc="Playing matches..."):

        board_game = start_random_game()

        # print(f"[FEN \"{board_game.fen}\"]")
        scorekeeper = Scorekeeper()
        scorekeeper.set_game_board_to_be_tracked(board_game)
        scorekeeper.record_fen()

        move_counter = 1

        while True:
            if board_game.is_game_over():
                break

            if board_game.turn == chess_game.WHITE:
                eval, move = ab_minmax(board_game, 3, math.inf, math.inf, True)
            else:
                eval, move = pred_minmax(board_game, 2, -math.inf, math.inf, True, mlp_regressor, scaler,
                                         predict_HL_extended)
                # eval, move = pred_bl_minmax_l(board_game, 2, -math.inf, math.inf, True, 5, 1, mlp_regressor, scaler, predict_HL)

            board_game.make_move(move)

            # print(f"{move_counter}. {move}")
            scorekeeper.record_move(move)

            move_counter = move_counter + 1

        # print(board_game.board.outcome())
        scorekeeper.record_outcome()

        scorekeeper.record_game("./games/")
        scorekeeper.clear_records()


def generate_dataset_for_HL():
    generate_dataset(300000, "./")


def convert_dataset_for_HL_to_json_dictionary():
    data = read_csv_file_as_dictionary("./dataset.csv")
    write_json_file("./prova", data)


def generate_extended_dataset_for_HL():
    generate_extended_dataset(300000, "./")


def convert_extended_dataset_for_HL_to_json_dictionary():
    data = read_csv_file_as_dictionary("./dataset.csv")
    write_json_file("./prova", data)


def run_ab_minmax_vs_bl_minmax_experiment():
    ab_minmax_vs_bl_minmax_experiment(500, "./stats/", 1, 5, 1, 5)


def plot_ab_minmax_vs_bl_minmax_experiment():
    plot_ab_minmax_vs_bl_minmax_experiment_results_data("./stats/")


if __name__ == '__main__':
    bl_minmax_l_optimal_l_experiment(10, "./stats/", 5, 5, 3, 3)
