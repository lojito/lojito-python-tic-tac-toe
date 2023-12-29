from abc import ABCMeta, abstractmethod

from src.lang.translation import Dictionary


class GameDBError(Exception):
    pass


class GameDBValuesError(GameDBError, metaclass=ABCMeta):
    def __init__(self, value) -> None:
        self._value = value

    @abstractmethod
    def __str__(self):
        pass


class GameLanguageError(GameDBValuesError):
    def __str__(self):
        return Dictionary.get_text("LANGUAGE", "INVALID_DB_CODE").format(self._value)


class GameUserPlaysFirstError(GameDBValuesError):
    def __str__(self):
        return Dictionary.get_text("PLAY_FIRST", "INVALID_DB_CODE").format(self._value)


class GamePlayingLevelError(GameDBValuesError):
    def __str__(self):
        return Dictionary.get_text("PLAYING_LEVEL", "INVALID_DB_CODE").format(
            self._value
        )


class GameWinnerError(GameDBValuesError):
    def __str__(self):
        return Dictionary.get_text("RESULT", "INVALID_DB_CODE").format(self._value)
