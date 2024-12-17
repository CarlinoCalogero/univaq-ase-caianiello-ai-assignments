from tqdm import tqdm
from game_setter import start_random_game
from ab_minmax import ab_minmax
import math
from printer import write_csv_file


def generate_dataset(number_of_rows_to_be_generated, dataset_folder):
    for _ in tqdm(range(number_of_rows_to_be_generated), desc="Creating dataset..."):
        board_game = start_random_game()
        H0 = board_game.evaluate_board()
        HL, move = ab_minmax(board_game, 3, math.inf, math.inf, True)

        file_path = f"{dataset_folder}dataset"
        write_csv_file(file_path, ['H0', 'HL'], [H0, HL])

