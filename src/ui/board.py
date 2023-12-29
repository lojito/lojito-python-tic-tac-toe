import json
from random import randint
from typing import Literal

from src.lang.translation import Dictionary
from src.ui.constants import (
    COMPUTER_MARK,
    NOBODY_MARK,
    ROWS_OF_SQUARES,
    ROWS_OF_SQUARES_DOUBLE,
    SQUARE_NOT_FOUND,
    SQUARES,
    SQUARES_NUMBER,
    USER_MARK,
)
from src.ui.exceptions import (
    BoardAlreadyInUseSquareError,
    BoardInvalidPlayerError,
    BoardInvalidSquareError,
)

Player = Literal["U", "C", " "]


class Board:
    def __init__(self):
        self._squares = [NOBODY_MARK] * SQUARES_NUMBER
        self._last_square_played_on: None | int = None
        self._moves = 0

    @property
    def last_square_played_on(self):
        return self._last_square_played_on

    @property
    def moves(self):
        return self._moves

    def reset(self):
        self._squares[:] = [NOBODY_MARK] * SQUARES_NUMBER
        self._last_square_played_on = None
        self._moves = 0

    @staticmethod
    def check_player(player: Player):
        if player not in (USER_MARK, COMPUTER_MARK, NOBODY_MARK):
            raise BoardInvalidPlayerError(player)

    def is_full(self):
        return NOBODY_MARK not in self._squares

    def is_empty(self):
        return USER_MARK not in self._squares and COMPUTER_MARK not in self._squares

    def is_square_empty(self, square: SQUARES):
        return self[square] == NOBODY_MARK

    def empty_squares(self):
        return list(
            filter(
                self.is_square_empty,
                SQUARES,
            )
        )

    def is_placed_twice_in_a_row_of_squares(self, player, squares, empty_square):
        return (
            self[squares[0]] == player
            and self[squares[1]] == player
            and self[empty_square] == NOBODY_MARK
        )

    def can_win_in_one_move(self, player: Player):
        Board.check_player(player)

        if self.is_full():
            return SQUARE_NOT_FOUND

        for square1, square2, square3 in ROWS_OF_SQUARES:
            if self.is_placed_twice_in_a_row_of_squares(
                player, [square1, square2], square3
            ):
                return square3
            if self.is_placed_twice_in_a_row_of_squares(
                player, [square1, square3], square2
            ):
                return square2
            if self.is_placed_twice_in_a_row_of_squares(
                player, [square2, square3], square1
            ):
                return square1
        return SQUARE_NOT_FOUND

    def is_placed_once_in_a_row_of_squares(self, player, square, empty_squares):
        return (
            self[square] == player
            and self[empty_squares[0]] == NOBODY_MARK
            and self[empty_squares[1]] == NOBODY_MARK
        )

    def can_win_in_two_moves_single(self, player: Player):
        Board.check_player(player)

        result = []
        for square1, square2, square3 in ROWS_OF_SQUARES:
            if self.is_placed_once_in_a_row_of_squares(
                player, square1, [square2, square3]
            ):
                result.append(square2)
                result.append(square3)
            if self.is_placed_once_in_a_row_of_squares(
                player, square2, [square1, square3]
            ):
                result.append(square1)
                result.append(square3)
            if self.is_placed_once_in_a_row_of_squares(
                player, square3, [square1, square2]
            ):
                result.append(square1)
                result.append(square2)
        return result

    def can_win_in_two_moves_double(self, player: Player):
        Board.check_player(player)

        result = []
        for squares in ROWS_OF_SQUARES_DOUBLE:
            square1, square2, square3, square4, square5 = squares
            if (
                self.is_placed_once_in_a_row_of_squares(
                    player, square3, [square1, square2]
                )
                or self.is_placed_once_in_a_row_of_squares(
                    player, square2, [square1, square3]
                )
            ) and (
                self.is_placed_once_in_a_row_of_squares(
                    player, square4, [square1, square5]
                )
                or self.is_placed_once_in_a_row_of_squares(
                    player, square5, [square1, square4]
                )
            ):
                result.append(square1)
        return result

    def won(self, player: Player):
        Board.check_player(player)

        for square1, square2, square3 in ROWS_OF_SQUARES:
            if (
                self[square1] == player
                and self[square2] == player
                and self[square3] == player
            ):
                return True
        return False

    def place(self, player: Player, square):
        self[square] = player
        self._last_square_played_on = square
        if player != NOBODY_MARK:
            self._moves += 1
        else:
            self._moves -= 1

    def place_on_random_empty_square(self, player: Player):
        if self.is_full():
            return SQUARE_NOT_FOUND

        empty_squares = self.empty_squares()
        square = empty_squares[randint(0, len(empty_squares) - 1)]
        self.place(player, square)
        return square

    def __str__(self):
        msg = f"""
    {self[SQUARES.TOP_LEFT]} | {self[SQUARES.TOP_CENTER]} | {self[SQUARES.TOP_RIGHT]}
   -----------
    {self[SQUARES.MIDDLE_LEFT]} | {self[SQUARES.MIDDLE_CENTER]} | {self[SQUARES.MIDDLE_RIGHT]}
   -----------
    {self[SQUARES.BOTTOM_LEFT]} | {self[SQUARES.BOTTOM_CENTER]} | {self[SQUARES.BOTTOM_RIGHT]}
        
   {COMPUTER_MARK} : {Dictionary.get_text("PLAYER", "COMPUTER_TEXT")}
   {USER_MARK} : {Dictionary.get_text("PLAYER", "USER_TEXT")}

"""
        return msg

    def __getitem__(self, square: SQUARES):
        try:
            return self._squares[square]
        except IndexError as exc:
            raise BoardInvalidSquareError(square) from exc

    def __setitem__(self, square, player: Player):
        Board.check_player(player)

        if not self.is_square_empty(square):
            raise BoardAlreadyInUseSquareError(self, square)

        try:
            self._squares[square] = player
        except IndexError as exc:
            raise BoardInvalidSquareError(square) from exc

    def to_json(self):
        return json.dumps(self._squares)

    @classmethod
    def from_json(cls, json_board: str):
        board_from_json = cls()
        board_from_json._squares = json.loads(json_board)
        return board_from_json
