import chess
import chess.engine
import math

WHITE = chess.WHITE


class ChessGame:

    def __init__(self):
        self.__board = chess.Board()

    @property
    def board(self):
        return self.__board

    @property
    def legal_moves(self):
        return self.__board.legal_moves

    @property
    def fen(self):
        return self.__board.fen()

    @property
    def turn(self):
        return self.__board.turn

    def is_game_over(self):
        return self.__board.is_game_over()

    def make_move(self, move):
        self.__board.push(move)

    def take_back_last_move(self):
        self.__board.pop()

    def get_piece_material_value(self, piece):
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0  # King is invaluable
        }
        if piece.color == chess.WHITE:
            return piece_values[piece.piece_type]
        return -piece_values[piece.piece_type]

    def get_piece_piece_square_table_value(self, piece, square):
        # Positive values favor White;
        # Negative values favor Black.
        # For Black's perspective, the tables are flipped vertically (row symmetry).
        # Pawns are encouraged to advance but are cautious in the early ranks.
        PAWN_TABLE = [
            0, 0, 0, 0, 0, 0, 0, 0,
            50, 50, 50, 50, 50, 50, 50, 50,
            10, 10, 20, 30, 30, 20, 10, 10,
            5, 5, 10, 25, 25, 10, 5, 5,
            0, 0, 0, 20, 20, 0, 0, 0,
            -5, -10, -10, 0, 0, -10, -10, -5,
            -10, -10, -10, -20, -20, -10, -10, -10,
            0, 0, 0, 0, 0, 0, 0, 0
        ]
        # Knights are stronger in the center and weaker on the edges.
        KNIGHT_TABLE = [
            -50, -40, -30, -30, -30, -30, -40, -50,
            -40, -20, 0, 0, 0, 0, -20, -40,
            -30, 0, 10, 15, 15, 10, 0, -30,
            -30, 5, 15, 20, 20, 15, 5, -30,
            -30, 0, 15, 20, 20, 15, 0, -30,
            -30, 5, 10, 15, 15, 10, 5, -30,
            -40, -20, 0, 5, 5, 0, -20, -40,
            -50, -40, -30, -30, -30, -30, -40, -50
        ]
        # Bishops are strong in open diagonals and near the center.
        BISHOP_TABLE = [
            -20, -10, -10, -10, -10, -10, -10, -20,
            -10, 5, 0, 0, 0, 0, 5, -10,
            -10, 10, 10, 10, 10, 10, 10, -10,
            -10, 0, 10, 10, 10, 10, 0, -10,
            -10, 5, 15, 10, 10, 15, 5, -10,
            -10, 10, 15, 15, 15, 15, 10, -10,
            -10, 5, 0, 0, 0, 0, 5, -10,
            -20, -10, -10, -10, -10, -10, -10, -20
        ]
        # Rooks are strong on open files and the 7th rank.
        ROOK_TABLE = [
            0, 0, 0, 5, 5, 0, 0, 0,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            5, 10, 10, 10, 10, 10, 10, 5,
            0, 0, 0, 5, 5, 0, 0, 0
        ]
        # Queens are strongest in the center and active positions.
        QUEEN_TABLE = [
            -20, -10, -10, -5, -5, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 0, 5, 5, 5, 5, 0, -10,
            -5, 0, 5, 5, 5, 5, 0, -5,
            0, 0, 5, 5, 5, 5, 0, -5,
            -10, 5, 5, 5, 5, 5, 0, -10,
            -10, 0, 5, 0, 0, 0, 0, -10,
            -20, -10, -10, -5, -5, -10, -10, -20
        ]
        # Encourages king safety during the middle game.
        KING_MIDGAME_TABLE = [
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -20, -30, -30, -40, -40, -30, -30, -20,
            -10, -20, -20, -20, -20, -20, -20, -10,
            20, 20, 0, 0, 0, 0, 20, 20,
            20, 30, 10, 0, 0, 10, 30, 20
        ]
        # Encourages king activity in the endgame
        KING_ENDGAME_TABLE = [
            -50, -40, -30, -20, -20, -30, -40, -50,
            -30, -20, -10, 0, 0, -10, -20, -30,
            -30, -10, 20, 30, 30, 20, -10, -30,
            -30, -10, 30, 40, 40, 30, -10, -30,
            -30, -10, 30, 40, 40, 30, -10, -30,
            -30, -10, 20, 30, 30, 20, -10, -30,
            -30, -30, 0, 0, 0, 0, -30, -30,
            -50, -30, -30, -30, -30, -30, -30, -50
        ]

        table = None

        match piece.piece_type:
            case chess.PAWN:
                table = PAWN_TABLE
            case chess.KNIGHT:
                table = KNIGHT_TABLE
            case chess.BISHOP:
                table = BISHOP_TABLE
            case chess.ROOK:
                table = ROOK_TABLE
            case chess.QUEEN:
                table = QUEEN_TABLE
            case chess.KING:
                if self.is_midgame():
                    table = KING_MIDGAME_TABLE
                else:
                    table = KING_ENDGAME_TABLE

        if piece.color == chess.WHITE:
            return table[square]
        return -table[63 - square]  # Flip table for Black

    def evaluate_king_safety(self, color):
        """
        Evaluate king safety for the given color.
        This considers pawn shields, castling, open files, and threats near the king.
        """
        king_square = self.__board.king(color)  # Get the king's position
        safety_score = 0

        # Get king's file and rank
        king_file = king_square % 8
        king_rank = king_square // 8

        # 1. Pawn Shield (only valid for kingside and queenside positions)
        pawn_shield = self.evaluate_pawn_shield(king_square, color)
        safety_score += pawn_shield  # Add pawn shield score

        # 2. Castling Bonus
        if self.is_castled(color):
            safety_score += 50  # Reward castling

        # 3. Penalty for being on or near open files
        if self.is_open_file(king_file):
            safety_score -= 30  # Penalize open file
        if king_file > 0 and self.is_open_file(king_file - 1):
            safety_score -= 15  # Penalize adjacent open file
        if king_file < 7 and self.is_open_file(king_file + 1):
            safety_score -= 15  # Penalize adjacent open file

        # 4. Count threats near the king
        adjacent_squares = self.get_adjacent_squares(king_square)
        for square in adjacent_squares:
            piece = self.__board.piece_at(square)
            if piece and piece.color != color:  # Enemy piece
                safety_score -= self.evaluate_threat(piece)

        # 5. Midgame exposure penalty (king too central)
        if self.is_midgame():
            center_distance = abs(king_file - 4) + abs(king_rank - 4)  # Manhattan distance to center
            safety_score -= center_distance * 10  # Penalize central king

        return safety_score

    def is_castled(self, color):
        """
        Check if the given color has castled.
        :param board: chess.Board instance
        :param color: chess.WHITE or chess.BLACK
        :return: True if the king has castled, False otherwise
        """
        king_square = self.__board.king(color)
        if color == chess.WHITE:
            # Castling moves place the king on g1 (kingside) or c1 (queenside)
            return king_square == chess.G1 or king_square == chess.C1
        else:  # chess.BLACK
            # Castling moves place the king on g8 (kingside) or c8 (queenside)
            return king_square == chess.G8 or king_square == chess.C8

    def evaluate_pawn_shield(self, king_square, color):
        """
        Evaluates the pawn shield around a castled king.
        Penalizes missing pawns in front of a castled king.
        :param board: chess.Board instance
        :param king_square: The square of the king (int)
        :param color: The color of the king (chess.WHITE or chess.BLACK)
        :return: A numerical evaluation of the pawn shield around the king
        """
        shield_score = 0
        penalty = -20  # Penalty for missing pawns in front of the castled king

        # For White (king castled on g1 or c1)
        if color == chess.WHITE:
            if king_square == chess.G1:
                # White king is castled on kingside (g1)
                # Check if pawns are present on f2 and g2
                if not self.__board.piece_at(chess.F2):
                    shield_score += penalty  # Missing pawn on f2
                if not self.__board.piece_at(chess.G2):
                    shield_score += penalty  # Missing pawn on g2
            elif king_square == chess.C1:
                # White king is castled on queenside (c1)
                # Check if pawns are present on b2 and d2
                if not self.__board.piece_at(chess.B2):
                    shield_score += penalty  # Missing pawn on b2
                if not self.__board.piece_at(chess.D2):
                    shield_score += penalty  # Missing pawn on d2

        # For Black (king castled on g8 or c8)
        elif color == chess.BLACK:
            if king_square == chess.G8:
                # Black king is castled on kingside (g8)
                # Check if pawns are present on f7 and g7
                if not self.__board.piece_at(chess.F7):
                    shield_score += penalty  # Missing pawn on f7
                if not self.__board.piece_at(chess.G7):
                    shield_score += penalty  # Missing pawn on g7
            elif king_square == chess.C8:
                # Black king is castled on queenside (c8)
                # Check if pawns are present on b7 and d7
                if not self.__board.piece_at(chess.B7):
                    shield_score += penalty  # Missing pawn on b7
                if not self.__board.piece_at(chess.D7):
                    shield_score += penalty  # Missing pawn on d7

        return shield_score

    def is_open_file(self, file_index):
        """
        Check if a given file is open (no pawns on the file).
        """
        for rank in range(8):
            square = file_index + rank * 8
            piece = self.__board.piece_at(square)
            if piece and piece.piece_type == chess.PAWN:
                return False  # Pawn exists on this file
        return True

    def get_adjacent_squares(self, square):
        """
        Get all squares adjacent to the given square (within one square radius).
        """
        adjacent = []
        file = square % 8
        rank = square // 8

        for df in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                if df == 0 and dr == 0:
                    continue  # Skip the square itself
                new_file = file + df
                new_rank = rank + dr
                if 0 <= new_file < 8 and 0 <= new_rank < 8:
                    adjacent.append(new_rank * 8 + new_file)

        return adjacent

    def evaluate_threat(self, piece):
        """
        Evaluate the threat posed by an enemy piece near the king.
        """
        threat_values = {
            chess.PAWN: 10,
            chess.KNIGHT: 30,
            chess.BISHOP: 30,
            chess.ROOK: 50,
            chess.QUEEN: 90,
            chess.KING: 0  # King itself isn't considered a direct threat
        }
        return threat_values.get(piece.piece_type, 0)

    # Static evaluation function for chess board
    def evaluate_board(self):
        """
        Static evaluation function for chess board.
        :return:
        """

        #print(f"turn: {"WHITE" if self.__board.turn else "BLACK"}, move: {self.__board.peek()}")

        # Checkmate
        if self.__board.is_game_over() and self.__board.outcome().termination and chess.Termination.CHECKMATE:
            return -math.inf if self.__board.turn else math.inf

        # Fivefold
        if self.__board.is_game_over() and self.__board.outcome().termination == chess.Termination.FIVEFOLD_REPETITION:
            return math.inf if self.__board.turn else -math.inf

        # SeventyFive
        if self.__board.is_game_over() and self.__board.outcome().termination == chess.Termination.SEVENTYFIVE_MOVES:
            return math.inf if self.__board.turn else -math.inf

        score = 0

        # List of all squares on a chessboard
        squares = list(chess.SQUARES)

        for square in squares:
            piece = self.__board.piece_at(square)
            if piece:
                # Material balance
                score += self.get_piece_material_value(piece)
                # Piece-square table
                score += self.get_piece_piece_square_table_value(piece, square)

        # King Safety
        score += self.evaluate_king_safety(chess.WHITE)
        score -= self.evaluate_king_safety(chess.BLACK)

        # Center Control (reward control of central squares e4, d4, e5, d5)
        CENTER_SQUARES = [27, 28, 35, 36]  # e4, d4, e5, d5
        for square in CENTER_SQUARES:
            controlling_piece = self.__board.piece_at(square)
            if controlling_piece:
                if controlling_piece.color == chess.WHITE:
                    score += 10
                else:
                    score -= 10

        # Pawn Structure
        score += self.evaluate_pawn_structure(chess.WHITE)
        score -= self.evaluate_pawn_structure(chess.BLACK)

        # Piece Activity (number of legal moves)
        score += 0.1 * len(self.get_color_legal_moves(chess.WHITE))
        score -= 0.1 * len(self.get_color_legal_moves(chess.BLACK))

        # Checks
        if self.__board.is_check():
            score += 100 if self.__board.turn else -100

        #print(score)
        return score

    def get_color_legal_moves(self, color):
        # Get all legal moves
        legal_moves = [move for move in self.__board.legal_moves if self.__board.piece_at(move.from_square).color == color]

        # Convert moves to UCI format (like e2e4, g1f3) for display
        legal_moves_uci = [move.uci() for move in legal_moves]

        return legal_moves_uci

    def is_midgame(self):
        """
        Determine if the game is in the midgame phase based on remaining material.
        Assumes the `board` object is from a library like python-chess.

        Midgame heuristic:
        - Enough heavy and minor pieces are present (queens, rooks, knights, bishops).
        - Pawns are still distributed, and the position hasn't transitioned to the king activity stage.
        """
        # Get counts of pieces
        white_material = self.count_material(chess.WHITE)
        black_material = self.count_material(chess.BLACK)
        total_material = white_material + black_material

        # Heuristic thresholds for midgame
        return 14 <= total_material <= 24

    def count_material(self, color):
        """
        Count material for a given color based on weighted values of pieces.
        Assign 0 points to pawns to focus only on heavy and minor pieces for midgame.
        """
        material = 0
        for piece_type in [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT]:
            material += len(self.__board.pieces(piece_type, color))
        return material

    def evaluate_pawn_structure(self, color):
        """
        Evaluate the pawn structure for the given color.
        Considers doubled, isolated, backward, passed, and connected pawns.

        :param board: chess.Board instance
        :param color: chess.WHITE or chess.BLACK
        :return: Integer score for pawn structure
        """
        score = 0
        pawns = self.__board.pieces(chess.PAWN, color)

        for pawn in pawns:
            file = chess.square_file(pawn)
            rank = chess.square_rank(pawn)

            # 1. Doubled Pawns
            if self.is_doubled_pawn(pawn, color):
                score -= 15  # Penalty for doubled pawn

            # 2. Isolated Pawns
            if self.is_isolated_pawn(pawn, color):
                score -= 20  # Penalty for isolated pawn

            # 3. Backward Pawns
            if self.is_backward_pawn(pawn, color):
                score -= 10  # Penalty for backward pawn

            # 4. Passed Pawns
            if self.is_passed_pawn(pawn, color):
                score += 30 + (7 - rank if color == chess.WHITE else rank) * 5  # Reward for passed pawn

            # 5. Connected Pawns
            if self.is_connected_pawn(pawn, color):
                score += 10  # Reward for connected pawn

            # 6. Pawn Chains
            if self.is_in_pawn_chain(pawn, color):
                score += 5  # Reward for being part of a pawn chain

        return score

    def is_doubled_pawn(self, pawn, color):
        """
        Check if the pawn is doubled (other friendly pawns on the same file).
        """
        file = chess.square_file(pawn)
        return sum(1 for sq in self.__board.pieces(chess.PAWN, color) if chess.square_file(sq) == file) > 1

    def is_isolated_pawn(self, pawn, color):
        """
        Check if the pawn is isolated (no friendly pawns on adjacent files).
        """
        file = chess.square_file(pawn)
        adjacent_files = [file - 1, file + 1]
        for adj_file in adjacent_files:
            if 0 <= adj_file <= 7:
                for rank in range(8):
                    square = chess.square(adj_file, rank)
                    if square in self.__board.pieces(chess.PAWN, color):
                        return False
        return True

    def is_backward_pawn(self, pawn, color):
        """
        Check if the pawn is backward (cannot advance without being captured or unsupported).
        """
        file = chess.square_file(pawn)
        rank = chess.square_rank(pawn)
        if color == chess.WHITE:
            for r in range(rank + 1, 8):
                square = chess.square(file, r)
                if square in self.__board.pieces(chess.PAWN, color):
                    return False  # Friendly pawn supports the advance
            return not self.is_protected(chess.square(file, rank + 1), color)
        else:
            for r in range(rank - 1, -1, -1):
                square = chess.square(file, r)
                if square in self.__board.pieces(chess.PAWN, color):
                    return False  # Friendly pawn supports the advance
            return not self.is_protected(chess.square(file, rank - 1), color)

    def is_passed_pawn(self, pawn, color):
        """
        Check if the pawn is passed (no enemy pawns block or can capture it).
        """
        file = chess.square_file(pawn)
        rank = chess.square_rank(pawn)
        if color == chess.WHITE:
            for r in range(rank + 1, 8):
                for adj_file in [file - 1, file, file + 1]:
                    if 0 <= adj_file < 8:
                        square = chess.square(adj_file, r)
                        if square in self.__board.pieces(chess.PAWN, chess.BLACK):
                            return False
        else:
            for r in range(rank - 1, -1, -1):
                for adj_file in [file - 1, file, file + 1]:
                    if 0 <= adj_file < 8:
                        square = chess.square(adj_file, r)
                        if square in self.__board.pieces(chess.PAWN, chess.WHITE):
                            return False
        return True

    def is_connected_pawn(self, pawn, color):
        """
        Check if the pawn is connected (adjacent friendly pawns on the same or nearby ranks).
        """
        file = chess.square_file(pawn)
        rank = chess.square_rank(pawn)
        for adj_file in [file - 1, file + 1]:
            if 0 <= adj_file < 8:
                for adj_rank in [rank - 1, rank, rank + 1]:
                    if 0 <= adj_rank < 8:
                        square = chess.square(adj_file, adj_rank)
                        if square in self.__board.pieces(chess.PAWN, color):
                            return True
        return False

    def is_in_pawn_chain(self, pawn, color):
        """
        Check if the given pawn is part of a pawn chain.
        :param board: chess.Board instance
        :param pawn: The square of the pawn being checked
        :param color: The color of the pawn (chess.WHITE or chess.BLACK)
        :return: True if the pawn is part of a pawn chain, False otherwise
        """
        file = chess.square_file(pawn)
        rank = chess.square_rank(pawn)

        if color == chess.WHITE:
            # Check if the pawn has supporting pawns below it
            supporting_pawns = [
                chess.square(file - 1, rank - 1),
                chess.square(file + 1, rank - 1)
            ]
            # Check if the pawn is supporting pawns above it
            supported_pawns = [
                chess.square(file - 1, rank + 1),
                chess.square(file + 1, rank + 1)
            ]
        else:  # For Black pawns
            # Check if the pawn has supporting pawns above it
            supporting_pawns = [
                chess.square(file - 1, rank + 1),
                chess.square(file + 1, rank + 1)
            ]
            # Check if the pawn is supporting pawns below it
            supported_pawns = [
                chess.square(file - 1, rank - 1),
                chess.square(file + 1, rank - 1)
            ]

        # Verify if any supporting or supported pawn exists
        for square in supporting_pawns + supported_pawns:
            if chess.SQUARES[0] <= square <= chess.SQUARES[63]:  # Check if square is valid
                if square in self.__board.pieces(chess.PAWN, color):
                    return True

        return False

    def is_protected(self, square, color):
        """
        Check if a square is protected by a friendly piece.
        """
        attackers = self.__board.attackers(color, square)
        return len(attackers) > 0

    def evaluate_move(self, move):
        """
        Evaluate a move by applying it and using the static board evaluation.
        :param move:
        :return:
        """
        self.make_move(move)
        score = self.evaluate_board()
        self.take_back_last_move()
        return score
