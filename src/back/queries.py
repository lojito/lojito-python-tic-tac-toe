CREATE_GAMES_TABLE_QUERY = (
    "CREATE TABLE IF NOT EXISTS games ("
    '"id"	SERIAL PRIMARY KEY,'
    '"user_plays_first" CHAR(1) NOT NULL,'
    '"playing_level" CHAR(1) NOT NULL,'
    '"board" CHAR(50) DEFAULT \'[" ", " ", " ", " ", " ", " ", " ", " ", " "]\'  NOT NULL,'
    "\"winner\" CHAR(1) DEFAULT ' ' NOT NULL,"
    '"language" CHAR(1) NOT NULL,'
    '"game_over" BOOLEAN DEFAULT false NOT NULL,'
    '"created_date" DATE NOT NULL DEFAULT CURRENT_DATE);'
)
INSERT_GAME_QUERY = (
    "INSERT INTO games(user_plays_first, playing_level, language)"
    "VALUES (%s, %s, %s) RETURNING id;"
)
UPDATE_GAME_QUERY = (
    "UPDATE games SET board = %s, winner = %s, game_over = true WHERE id = %s"
)
GET_GAMES_QUERY = (
    "SELECT id, user_plays_first, playing_level, board, "
    "winner, language, TO_CHAR(created_date, 'DD-Mon-YYYY') AS created_date FROM games "
    "WHERE game_over = true"
)
DELETE_GAME_QUERY = "DELETE FROM games WHERE id = %s;"
DELETE_ALL_GAMES_QUERY = "TRUNCATE TABLE games;"
