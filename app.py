import os

from dotenv import load_dotenv

from src.back.database import DB, DBConnectionError
from src.back.exceptions import GameDBError
from src.back.queries import CREATE_GAMES_TABLE_QUERY
from src.lang.translation import Dictionary
from src.ui.exceptions import BoardError
from src.ui.menu import (
    MENUOPTIONS,
    menu_get_games,
    menu_new_game,
    menu_remove_all_games,
    menu_remove_game,
    menu_save_game,
    prompt_menu_option,
)
from src.ui.tictactoe import TicTacToe


def start_game(user_plays_first, playing_level):
    tictactoe = TicTacToe(user_plays_first, playing_level)
    print(Dictionary.get_text("GAME", "START"))
    tictactoe.play()
    winner = tictactoe.winner
    print(
        Dictionary.get_text("GAME", "OVER")
        + Dictionary.get_text("RESULT", winner)
        + "\n"
    )
    return winner


def main():
    try:
        load_dotenv()
        DB.connect(
            f'host={os.environ["HOST"]} dbname={os.environ["DATABASE"]} \
            user={os.environ["USER"]} password={os.environ["PASSWORD"]} \
            port={os.environ["PORT"]}'
        )
        _, err = DB.execute(CREATE_GAMES_TABLE_QUERY)
        if err:
            print("Error creating the games table.")
    except DBConnectionError:
        print(Dictionary.get_text("GAME", "DB_CONNECTION"))

    print(Dictionary.get_text("GAME", "WELCOME"))
    while True:
        try:
            option = MENUOPTIONS(prompt_menu_option())
            match option:
                case MENUOPTIONS.NEW_GAME:
                    game_id, user_plays_first, playing_level = menu_new_game()
                    winner = start_game(user_plays_first, playing_level)
                    if game_id is not None:
                        menu_save_game(game_id, winner)
                case MENUOPTIONS.LIST_PREVIOUS_GAMES:
                    menu_get_games()
                case MENUOPTIONS.REMOVE_GAME:
                    menu_remove_game()
                case MENUOPTIONS.REMOVE_ALL_GAMES:
                    menu_remove_all_games()
                case MENUOPTIONS.CHANGE_LANGUAGE:
                    Dictionary.change_default_language()
                    print(Dictionary.get_text("LANGUAGE", "CHANGE_TO"))
                case MENUOPTIONS.HELP:
                    print(Dictionary.get_text("GAME", "HELP"))
                case MENUOPTIONS.EXIT_GAME:
                    print(Dictionary.get_text("GAME", "THANK_YOU"))
                    break
        except BoardError as e:
            print("\n")
            print(Dictionary.get_text("MESSAGES", "INTERNAL_ERROR") + str(e))
        except GameDBError as e:
            print(str(e))
        except DBConnectionError:
            print(Dictionary.get_text("GAME", "DB_CONNECTION"))


if __name__ == "__main__":
    main()
