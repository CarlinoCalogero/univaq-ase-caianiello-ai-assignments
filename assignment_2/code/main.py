import chess_game
from game_setter import start_random_game
from ab_minmax import ab_minmax
from bl_minmax import bl_minmax
from bl_minmax_l import bl_minmax_l
import math
from scorekeeper import Scorekeeper
from tqdm import tqdm
from data_analyst import generate_dataset
from reader import read_csv_file_as_dictionary
from printer import write_json_file
from trainer import train_mlp_regressor
from pred_minmax import pred_minmax


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


def generate_dataset_for_HL():
    generate_dataset(300000, "./")


def convert_dataset_for_HL_to_json_dictionary():
    data = read_csv_file_as_dictionary("./dataset.csv")
    write_json_file("./prova", data)


if __name__ == '__main__':
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
                eval, move = pred_minmax(board_game, 2, -math.inf, math.inf, True, mlp_regressor, scaler)

            board_game.make_move(move)

            # print(f"{move_counter}. {move}")
            scorekeeper.record_move(move)

            move_counter = move_counter + 1

        # print(board_game.board.outcome())
        scorekeeper.record_outcome()

        scorekeeper.record_game("./games/")
        scorekeeper.clear_records()
