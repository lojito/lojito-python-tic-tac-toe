from abc import ABCMeta, abstractmethod

from src.lang.translation import Dictionary
from src.ui.constants import COMPUTER_MARK, NOBODY_MARK, SQUARES_NUMBER, USER_MARK


class BoardError(Exception):
    pass


class BoardSquareError(BoardError, metaclass=ABCMeta):
    def __init__(self, square):
        self._square = square

    @abstractmethod
    def __str__(self):
        pass


class BoardInvalidSquareError(BoardSquareError):
    def __str__(self):
        return Dictionary.get_text("POSITION", "INVALID").format(
            self._square + 1
        ) + Dictionary.get_text("POSITION", "RANGE").format(SQUARES_NUMBER)


class BoardAlreadyInUseSquareError(BoardSquareError):
    def __init__(self, board, square):
        super().__init__(square)
        self._availables = list((square1 + 1 for square1 in board.empty_squares()))

    def __str__(self):
        return Dictionary.get_text("POSITION", "ALREADY_IN_USE").format(
            self._square + 1, str(self._availables)
        )


class BoardInvalidPlayerError(BoardError):
    def __init__(self, player):
        self._player = player

    def __str__(self):
        return Dictionary.get_text("MESSAGES", "INVALID_PLAYER").format(
            self._player
        ) + Dictionary.get_text("MESSAGES", "VALID_PLAYER_VALUES").format(
            NOBODY_MARK, USER_MARK, COMPUTER_MARK
        )


class BoardIsFullError(BoardError):
    def __str__(self):
        return Dictionary.get_text("MESSAGES", "BOARD_IS_FULL")
