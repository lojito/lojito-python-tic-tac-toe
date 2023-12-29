from typing import Literal

from src.ui.constants import USER_MARK
from src.ui.players.player import Player


class User(Player):
    def play(self, square):
        self._board.place(USER_MARK, square - 1)

    def print_board_info(self):
        print(str(self._board))

    def __str__(self) -> Literal["U"]:
        return USER_MARK
