from src.lang.translation import Dictionary
from src.ui.board import Board
from src.ui.constants import COMPUTER_MARK, NOBODY_MARK, USER_MARK
from src.ui.exceptions import BoardSquareError
from src.ui.players.computer import Computer
from src.ui.players.user import User
from src.ui.prompt import prompt_integer_value


class TicTacToe:
    board = Board()
    user = User(board)
    computer = Computer(board)

    def __init__(
        self,
        user_plays_first,
        playing_level,
    ):
        self._user_won = False
        self._computer_won = False
        self._over = False
        self._user_plays_first = user_plays_first
        self._playing_level = playing_level
        TicTacToe.computer.user_plays_first = user_plays_first
        TicTacToe.computer.playing_level = playing_level
        TicTacToe.board.reset()

    def user_turn_to_play(self):
        while True:
            try:
                TicTacToe.user.play(prompt_integer_value("POSITION", "CHOOSE_ONE"))
            except BoardSquareError as e:
                print(str(e))
            else:
                self._user_won = TicTacToe.user.won()
                break

    def computer_turn_to_play(self):
        TicTacToe.computer.play()
        TicTacToe.computer.print_board_info()
        self._computer_won = TicTacToe.computer.won()

    def get_current_player(self, current_player=None):
        if current_player is None:
            return (
                TicTacToe.user
                if self._user_plays_first
                == Dictionary.get_text("PLAY_FIRST", "ANSWER", "YES")
                else TicTacToe.computer
            )
        return (
            TicTacToe.user
            if current_player == TicTacToe.computer
            else TicTacToe.computer
        )

    def play(self):
        current_player = self.get_current_player()

        if current_player == TicTacToe.user:
            TicTacToe.user.print_board_info()

        while not self._over:
            if current_player == TicTacToe.user:
                self.user_turn_to_play()
            else:
                self.computer_turn_to_play()
            if self._user_won or self._computer_won or TicTacToe.board.is_full():
                self._over = True
            else:
                current_player = self.get_current_player(current_player)

        if current_player == TicTacToe.user:
            TicTacToe.user.print_board_info()

    @property
    def winner(self):
        return (
            USER_MARK
            if self._user_won
            else COMPUTER_MARK
            if self._computer_won
            else NOBODY_MARK
        )
