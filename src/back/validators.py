DB_LANGUAGE_ENGLISH = "1"
DB_LANGUAGE_FRENCH = "2"
DB_LANGUAGE_SPANISH = "3"

DB_USER_MARK = "U"
DB_COMPUTER_MARK = "C"
DB_NOBODY_MARK = "N"


DB_USER_PLAY_FIRST_YES = "1"
DB_USER_PLAY_FIRST_NO = "2"

DB_COMPUTER_PLAYING_LEVEL_BEGINNER = "1"
DB_COMPUTER_PLAYING_LEVEL_INTERMEDIATE = "2"
DB_COMPUTER_PLAYING_LEVEL_EXPERT = "3"


def validate_language(language: str):
    return language in (DB_LANGUAGE_ENGLISH, DB_LANGUAGE_FRENCH, DB_LANGUAGE_SPANISH)


def validate_user_play_first(user_plays_first: str):
    return user_plays_first in (DB_USER_PLAY_FIRST_YES, DB_USER_PLAY_FIRST_NO)


def validate_playing_level(playing_level: str):
    return playing_level in (
        DB_COMPUTER_PLAYING_LEVEL_BEGINNER,
        DB_COMPUTER_PLAYING_LEVEL_INTERMEDIATE,
        DB_COMPUTER_PLAYING_LEVEL_EXPERT,
    )


def validate_winner(winner: str):
    return winner in (DB_USER_MARK, DB_COMPUTER_MARK, DB_NOBODY_MARK)
