import random

from src.lang.translation import Dictionary
from src.ui.board import Board
from src.ui.constants import (
    COMPUTER_MARK,
    NOBODY_MARK,
    SQUARE_NOT_FOUND,
    SQUARES,
    USER_MARK,
)
from src.ui.exceptions import BoardIsFullError
from src.ui.players.player import Player


class Computer(Player):
    def __init__(self, board: Board):
        super().__init__(board)
        self.user_plays_first = Dictionary.get_text("PLAY_FIRST", "ANSWER", "YES")
        self.playing_level = Dictionary.get_text("PLAYING_LEVEL", "ANSWER", "BEGINNER")

    def print_board_info(self):
        print("\n")
        if self._board.last_square_played_on is not None:
            print(str(self._board))
            print(
                Dictionary.get_text("POSITION", "COMPUTER_PLAYED_ON").format(
                    self._board.last_square_played_on + 1
                )
            )
        else:
            print(Dictionary.get_text("POSITION", "COMPUTER_HAS_NOT_PLAYED_YET"))

    def get_random_corner_square(self):
        return random.choice(
            [
                SQUARES.TOP_LEFT,
                SQUARES.TOP_RIGHT,
                SQUARES.BOTTOM_LEFT,
                SQUARES.BOTTOM_RIGHT,
            ]
        )

    def get_random_corner_middle_square(self):
        return random.choice(
            [
                SQUARES.TOP_LEFT,
                SQUARES.TOP_RIGHT,
                SQUARES.BOTTOM_LEFT,
                SQUARES.BOTTOM_RIGHT,
                SQUARES.MIDDLE_CENTER,
            ]
        )

    def play_first_time(self):
        if self._board.is_empty():
            self._board.place(COMPUTER_MARK, self.get_random_corner_middle_square())
        else:
            self._board.place(
                COMPUTER_MARK,
                self.get_random_corner_square()
                if self._board[SQUARES.MIDDLE_CENTER] == USER_MARK
                else SQUARES.MIDDLE_CENTER,
            )

    def play_second_time(self):
        if self._board[SQUARES.MIDDLE_CENTER] == COMPUTER_MARK:
            square = self.get_random_corner_square()

            while self._board[square] != NOBODY_MARK:
                square = self.get_random_corner_square()

            self._board.place(COMPUTER_MARK, square)
        elif self._board[SQUARES.MIDDLE_CENTER] == USER_MARK:
            self.play_on_any_empty_square()
        else:
            self._board.place(COMPUTER_MARK, SQUARES.MIDDLE_CENTER)

    def can_win_in_one_move(self, player):
        square = self._board.can_win_in_one_move(player)
        if square != SQUARE_NOT_FOUND:
            self._board.place(COMPUTER_MARK, square)
            return True
        return False

    def play_one_more_time(self):
        if self.can_win_in_one_move(COMPUTER_MARK):
            return
        if self.can_win_in_one_move(USER_MARK):
            return
        squares = self._board.can_win_in_two_moves_double(COMPUTER_MARK)
        if len(squares) > 0:
            self._board.place(COMPUTER_MARK, random.choice(squares))
            return

        squares = self._board.can_win_in_two_moves_single(COMPUTER_MARK)
        for square in squares:
            self._board.place(COMPUTER_MARK, square)
            square_computer = self._board.can_win_in_one_move(COMPUTER_MARK)
            squares_user = self._board.can_win_in_two_moves_double(USER_MARK)
            if len(squares_user) > 0 and square_computer in squares_user:
                self._board.place(NOBODY_MARK, square)
            else:
                return

        self.play_on_any_empty_square()

    def play_expert_level(self):
        moves = self._board.moves
        if self.user_plays_first == Dictionary.get_text("PLAY_FIRST", "ANSWER", "YES"):
            if moves == 1:
                self.play_first_time()
            else:
                self.play_one_more_time()
        elif self._board.is_empty():
            self.play_first_time()
        elif moves == 2:
            self.play_second_time()
        else:
            self.play_one_more_time()

    def play_intermediate_level(self):
        if self.can_win_in_one_move(COMPUTER_MARK):
            return
        if self.can_win_in_one_move(USER_MARK):
            return
        square = self._board.place_on_random_empty_square(COMPUTER_MARK)
        if square == SQUARE_NOT_FOUND:
            raise BoardIsFullError()

    def play_on_any_empty_square(self):
        square = self._board.place_on_random_empty_square(COMPUTER_MARK)
        if square == SQUARE_NOT_FOUND:
            raise BoardIsFullError()

    def play(self, square=0):
        if self.playing_level == Dictionary.get_text(
            "PLAYING_LEVEL", "ANSWER", "BEGINNER"
        ):
            self.play_on_any_empty_square()
        elif self.playing_level == Dictionary.get_text(
            "PLAYING_LEVEL", "ANSWER", "INTERMEDIATE"
        ):
            self.play_intermediate_level()
        else:
            self.play_expert_level()

    def __str__(self):
        return COMPUTER_MARK
