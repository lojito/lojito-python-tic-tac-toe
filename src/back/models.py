from src.back.database import DB
from src.back.queries import (
    DELETE_ALL_GAMES_QUERY,
    DELETE_GAME_QUERY,
    GET_GAMES_QUERY,
    INSERT_GAME_QUERY,
    UPDATE_GAME_QUERY,
)


class Game:
    def __init__(
        self,
        user_plays_first: str,
        playing_level: str,
        board: str,
        winner: str,
        language: str,
        _id: int,
        created_date: str,
    ):
        self.user_plays_first = user_plays_first
        self.playing_level = playing_level
        self.board = board
        self.winner = winner
        self.language = language
        self.id = _id
        self.created_date = created_date

    @classmethod
    def create(cls, user_plays_first, playing_level, language):
        record, err = DB.get_result_one(
            INSERT_GAME_QUERY, (user_plays_first, playing_level, language)
        )
        if record is not None and record != 0:
            return record["id"], err
        return None, err

    @staticmethod
    def save(game_id: str, board: str, winner: str):
        _, err = DB.execute(UPDATE_GAME_QUERY, (board, winner, game_id))
        return err

    @classmethod
    def all(cls):
        (games, err) = DB.get_result_all(GET_GAMES_QUERY)
        if err:
            return [], err
        if games is not None:
            return (
                [
                    cls(
                        game["user_plays_first"],
                        game["playing_level"],
                        game["board"],
                        game["winner"],
                        game["language"],
                        game["id"],
                        game["created_date"],
                    )
                    for game in games
                ],
                err,
            )
        return None, err

    @staticmethod
    def remove(game_id: int):
        return DB.execute(DELETE_GAME_QUERY, (game_id,))

    @staticmethod
    def remove_all():
        return DB.execute(DELETE_ALL_GAMES_QUERY)
