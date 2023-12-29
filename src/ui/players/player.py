from abc import ABCMeta, abstractmethod
from typing import Literal, cast

from src.ui.board import Board


class Player(metaclass=ABCMeta):
    def __init__(self, board: Board):
        self._board = board

    @abstractmethod
    def play(self, square: int):
        return

    @abstractmethod
    def print_board_info(self):
        return

    def won(self):
        return self._board.won(cast(Literal["U", "C"], str(self)))
