from printer import write_json_file, write_text_file
import datetime


class Scorekeeper:

    def __init__(self):
        self.__tracked_board_game = None
        self.__tracked_board_game_fen = None
        self.__tracked_board_game_moves = []
        self.__tracked_board_game_outcome = None

    def clear_records(self):
        self.__tracked_board_game = None
        self.__tracked_board_game_fen = None
        self.__tracked_board_game_moves = []
        self.__tracked_board_game_outcome = None

    def set_game_board_to_be_tracked(self, board_game):
        self.clear_records()  # clear everything before setting new tracked board
        self.__tracked_board_game = board_game

    def check_tracked_game_board(self):
        if self.__tracked_board_game is None:
            raise Exception("Error! The scorekeeper is not tracking any board!")

    def record_fen(self):
        self.check_tracked_game_board()
        self.__tracked_board_game_fen = self.__tracked_board_game.fen

    def check_tracked_game_board_fen(self):
        if self.__tracked_board_game_fen is None:
            raise Exception("Error! The scorekeeper has not yet recorded the game board's FEN!")

    def record_move(self, move):
        self.__tracked_board_game_moves.append(move)

    def record_outcome(self):
        self.check_tracked_game_board()
        self.__tracked_board_game_outcome = self.__tracked_board_game.board.outcome().termination.__str__()
    
    def check_tracked_game_board_outcome(self):
        if self.__tracked_board_game_outcome is None:
            raise Exception("Error! The scorekeeper has not yet recorded the game board's outcome!")

    def get_moves_string(self):
        return "".join(f'{index + 1}. {move} ' for index, move in enumerate(self.__tracked_board_game_moves))

    def get_formatted_fen(self):
        return f"[FEN \"{self.__tracked_board_game_fen}\"]"

    def get_analysis_string(self):
        return f"{self.get_formatted_fen()} {self.get_moves_string()}"

    def get_game_report(self):
        self.check_tracked_game_board_fen()
        self.check_tracked_game_board_outcome()
        return {
            "FEN": self.__tracked_board_game_fen,
            "moves": {index+1: f"{move}" for index, move in enumerate(self.__tracked_board_game_moves)},
            "outcome": self.__tracked_board_game_outcome
        }

    def record_game(self, game_folder):
        game = self.get_game_report()

        current_time = datetime.datetime.now()
        file_name = f"{current_time.year}{current_time.month}{current_time.day}{current_time.hour}{current_time.minute}{current_time.second}{current_time.microsecond}"
        file_path = f"{game_folder}{file_name}"

        write_json_file(file_path, game)
        write_text_file(file_path, self.get_analysis_string())
