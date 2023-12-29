from src.back.exceptions import (
    GameLanguageError,
    GamePlayingLevelError,
    GameUserPlaysFirstError,
    GameWinnerError,
)
from src.back.models import Game
from src.back.validators import (
    validate_language,
    validate_playing_level,
    validate_user_play_first,
    validate_winner,
)


def new_game(user_plays_first_db_code: str, playing_level: str, language: str):
    if not validate_language(language):
        raise GameLanguageError(language)

    if not validate_user_play_first(user_plays_first_db_code):
        raise GameUserPlaysFirstError(user_plays_first_db_code)

    if not validate_playing_level(playing_level):
        raise GamePlayingLevelError(playing_level)

    (game_id, err) = Game.create(user_plays_first_db_code, playing_level, language)
    return (game_id, err)


def save_game(game_id: str, board: str, winner: str):
    if not validate_winner(winner):
        raise GameWinnerError(winner)
    return Game.save(game_id, board, winner)


def get_games():
    return Game.all()


def remove_game(game_id: int):
    return Game.remove(game_id)


def remove_all_games():
    return Game.remove_all()
