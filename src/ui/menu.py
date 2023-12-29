from enum import Enum

from src.back.controllers import (
    get_games,
    new_game,
    remove_all_games,
    remove_game,
    save_game,
)
from src.back.validators import (
    DB_COMPUTER_PLAYING_LEVEL_BEGINNER,
    DB_COMPUTER_PLAYING_LEVEL_EXPERT,
    DB_COMPUTER_PLAYING_LEVEL_INTERMEDIATE,
    DB_USER_PLAY_FIRST_NO,
    DB_USER_PLAY_FIRST_YES,
)
from src.lang.translation import Dictionary
from src.ui.board import Board
from src.ui.prompt import (
    prompt_game_setting,
    prompt_integer_value,
    prompt_remove_game_confirmation,
)
from src.ui.tictactoe import TicTacToe


class MENUOPTIONS(Enum):
    NEW_GAME = "1"
    LIST_PREVIOUS_GAMES = "2"
    REMOVE_GAME = "3"
    REMOVE_ALL_GAMES = "4"
    CHANGE_LANGUAGE = "5"
    HELP = "6"
    EXIT_GAME = "7"


def prompt_menu_option():
    while (user_option := input(Dictionary.get_text("MENU", "TEXT"))) not in [
        opt.value for opt in MENUOPTIONS
    ]:
        print(Dictionary.get_text("MENU", "INVALID_OPTION").format(user_option))
    return user_option


def menu_new_game():
    user_plays_first = prompt_game_setting("PLAY_FIRST")
    user_plays_first_db_code = (
        DB_USER_PLAY_FIRST_YES
        if user_plays_first == Dictionary.get_text("PLAY_FIRST", "ANSWER", "YES")
        else DB_USER_PLAY_FIRST_NO
    )
    playing_level = prompt_game_setting("PLAYING_LEVEL")
    if playing_level == Dictionary.get_text("PLAYING_LEVEL", "ANSWER", "BEGINNER"):
        playing_level_db_code = DB_COMPUTER_PLAYING_LEVEL_BEGINNER
    elif playing_level == Dictionary.get_text(
        "PLAYING_LEVEL", "ANSWER", "INTERMEDIATE"
    ):
        playing_level_db_code = DB_COMPUTER_PLAYING_LEVEL_INTERMEDIATE
    else:
        playing_level_db_code = DB_COMPUTER_PLAYING_LEVEL_EXPERT

    game_id, err = new_game(
        user_plays_first_db_code, playing_level_db_code, Dictionary.user_language
    )
    if err:
        print(Dictionary.get_text("GAME", "DB_ERROR_ON_CREATE"))
    return (game_id, user_plays_first, playing_level)


def menu_save_game(game_id, winner: str):
    if save_game(game_id, TicTacToe.board.to_json(), winner):
        print(Dictionary.get_text("GAME", "DB_ERROR_ON_SAVE"))


def menu_get_games():
    games, err = get_games()
    if err:
        print(Dictionary.get_text("HISTORICAL", "DB_ERROR"))
        return
    if games is not None and len(games) > 0:
        historical_games_text = Dictionary.get_text("HISTORICAL", "LIST")
        default_language = Dictionary.default_language
        for i, game in enumerate(games, 1):
            historical_games_text += Dictionary.get_text("HISTORICAL", "HEADER").format(
                i,
                game.id,
                game.created_date.strip() if game.created_date is not None else None,
                Dictionary.get_text(
                    "PLAY_FIRST",
                    "TEXTS",
                    game.user_plays_first,
                    language=default_language,
                ),
                Dictionary.get_text(
                    "PLAYING_LEVEL",
                    "TEXTS",
                    game.playing_level,
                    language=default_language,
                ),
                Dictionary.get_text("RESULT", game.winner),
            )
            game_board = Board.from_json(game.board)
            historical_games_text += str(game_board)
            del game_board
        print(historical_games_text)
    else:
        print(Dictionary.get_text("HISTORICAL", "NOT_FOUND"))


def menu_remove_game():
    game_id = prompt_integer_value("REMOVE", "PROMPT")
    if prompt_remove_game_confirmation(game_id) == Dictionary.get_text("REMOVE", "YES"):
        (number_of_games_removed, err) = remove_game(game_id)
        if err is True:
            print(Dictionary.get_text("REMOVE", "DB_ERROR"))
        elif number_of_games_removed == 0:
            print(Dictionary.get_text("REMOVE", "FAILURE"))
        else:
            print(Dictionary.get_text("REMOVE", "SUCCESS").format(game_id))
    else:
        print("\n")


def menu_remove_all_games():
    if prompt_remove_game_confirmation() == Dictionary.get_text("REMOVE_ALL", "YES"):
        (number_of_games_removed, err) = remove_all_games()
        if err is True:
            print(Dictionary.get_text("REMOVE_ALL", "DB_ERROR"))
        elif number_of_games_removed == 0:
            print(Dictionary.get_text("REMOVE_ALL", "FAILURE"))
        else:
            print(Dictionary.get_text("REMOVE_ALL", "SUCCESS"))
    else:
        print("\n")
