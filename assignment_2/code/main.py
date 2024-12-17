from chess_game import ChessGame
import chess_game
from ab_minmax import ab_minmax
from bl_minmax import bl_minmax
from bl_minmax_l import bl_minmax_l
import random
import math
import json
import datetime
from tqdm import tqdm

if __name__ == '__main__':
    for _ in tqdm(range(1000), desc="Playing matches..."):
        match = {
            "FEN": None,
            "moves": None,
            "analysis_string": None,
            "outcome": None
        }

        board_game = ChessGame()

        for _ in range(3, 8):
            move = random.choice(list(board_game.board.legal_moves))
            board_game.make_move(move)

        #print(f"[FEN \"{board_game.fen}\"]")
        match["FEN"] = board_game.fen

        move_counter = 1

        while True:
            if board_game.is_game_over():
                break

            if board_game.turn == chess_game.WHITE:
                eval, move = ab_minmax(board_game, 3, math.inf, math.inf, True)
            else:
                eval, move = bl_minmax(board_game, 3, math.inf, math.inf, True, 5)

            board_game.make_move(move)

            #print(f"{move_counter}. {move}")
            if match["moves"] is None:
                match["moves"] = f"{move_counter}. {move}"
            else:
                match["moves"] = f"{match["moves"]} {move_counter}. {move}"

            move_counter = move_counter + 1

        match["analysis_string"] = f"{match["FEN"]} {match["moves"]}"

        #print(board_game.board.outcome())
        match["outcome"] = board_game.board.outcome().termination.__str__()

        current_time = datetime.datetime.now()
        file_name = f"{current_time.year}{current_time.month}{current_time.day}{current_time.hour}{current_time.minute}{current_time.second}{current_time.microsecond}"

        # Write dictionary to file using json.dump()
        file_path = f"./games/{file_name}.json"
        with open(file_path, "w") as f:
            json.dump(match, f)

