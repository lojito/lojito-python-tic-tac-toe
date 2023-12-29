EN = {
    "GAME": {
        "WELCOME": "\n  Welcome to the Tic-Tac-Toe game!\n",
        "THANK_YOU": "\n  Thank you for playing the Tic-Tac-Toe game. Bye!\n",
        "EXIT": "Exit the game.",
        "HELP": "\n  You are going to play against the computer. "
        "At the end of the game the player who started the game, the winner, "
        "the state of the board and the today's date will be saved to the database.\n",
        "START": "\n  The game starts!",
        "OVER": "  Game over! ",
        "BOARD": "  Board:",
        "DB_CONNECTION": "\n  Error establishing a database connection. "
        "You can still play the Tic-Tac-Toe game "
        "but the games statistics will not be saved in the database.\n",
        "DB_ERROR_ON_CREATE": "\n  The game couldn't be successfully created "
        "due to a database error.\n",
        "DB_ERROR_ON_SAVE": "\n  The game couldn't be successfully saved "
        "due to a database error.\n",
    },
    "HISTORICAL": {
        "LIST": "\n  ******** List of previous games: ********\n\n",
        "HEADER": "  Game #{}(id = {}): Date: {} | User played first?: {}"
        " | Playing level: {} | Result: {}\n",
        "NOT_FOUND": "\n  There is no record of previous games yet. "
        "Please, play at least one time before choosing this option.\n",
        "DB_ERROR": "\n  Cannot successfully retrieve the historical games "
        "due to a database error.\n",
    },
    "REMOVE": {
        "PROMPT": "\n  Enter the id of the game you want to remove: ",
        "CONFIRMATION": "\n  Are you sure you want to remove the game with id = {}? [Y/y/N/n]: ",
        "YES": "y",
        "NO": "n",
        "INVALID_ANSWER": "  Please, enter 'Y' or 'y' for 'yes' or 'N' or 'n' for 'no'.",
        "SUCCESS": "\n  The game with id = {} has been removed from the database.\n",
        "FAILURE": "\n  No game has been removed! "
        "The id you entered is not associated with any game. "
        "Please, choose option 2 from the menu in order to find out the id of the game "
        "you would like to remove from the database.\n",
        "INVALID": "  Invalid game id {}. ",
        "DB_ERROR": "\n  Cannot successfully remove any game due to a database error.\n",
    },
    "REMOVE_ALL": {
        "CONFIRMATION": "\n  Are you sure you want to remove all the games"
        " from the database? [Y/y/N/n]: ",
        "YES": "y",
        "NO": "n",
        "INVALID_ANSWER": "  Please, enter 'Y' or 'y' for 'yes' or 'N' or 'n' for 'no'.",
        "SUCCESS": "\n  All the games have been removed from the database.\n",
        "FAILURE": "\n  No game has been removed from the database "
        "as an internal error has occurred.",
        "DB_ERROR": "\n  Cannot successfully remove all the games due to a database error.\n",
    },
    "MENU": {
        "TEXT": """  Please, select one of the following menu options:
    1 - Start a new game.
    2 - See a list of previous games.
    3 - Remove a game from the database.
    4 - Remove all games from the database.
    5 - Change the default language.
    6 - Help.
    7 - Exit the game.
  Enter an option (1 - 7): """,
        "INVALID_OPTION": "  Invalid option: '{}'\n",
    },
    "MESSAGES": {
        "INVALID_PLAYER": "Invalid player '{}'. ",
        "VALID_PLAYER_VALUES": "Valid values for a player are '{}' "
        "indicating nor the user nor the computer has played on a particular square, "
        "'{}' for the user who is playing against the computer and '{}' "
        "for the computer itself.",
        "INVALID_PATHNAME": "\n  Can not save, remove or load previous games "
        "due to the pathname '{}' is not valid or "
        "you don't have enough permissions to write to that file.",
        "INTERNAL_ERROR": "You will not be able to continue playing this game "
        "as an internal error has occurred.\n",
        "BOARD_IS_FULL": "The board is already full.",
    },
    "PLAY_FIRST": {
        "QUESTION": "\n  Would you like to be the player who plays first? [Y/y/N/n]: ",
        "ANSWER": {
            "YES": "Y",
            "NO": "N",
        },
        "TEXTS": {
            "1": "Yes",
            "2": "No",
        },
        "INVALID_ANSWER": "  Invalid answer: '{}'.",
        "INVALID_DB_CODE": "\n  The user play first code '{}' is invalid "
        "and because of that cannot be saved in the database.\n",
    },
    "PLAYING_LEVEL": {
        "QUESTION": """  \n  Please, choose the computer playing level:
    1- For a beginner level enter 'B' or 'b'. The computer plays each time on a random position.
    2- For intermediate level enter 'I' or 'i'. The computer plays sometimes randomly and other times do some thinking before playing.
    3- For expert level enter 'E' or 'e'. You will not be able to beat the computer. Either you will lose or the game will endup in a draw.
  Enter the computer playing level [B/b/I/i/E/e]: """,
        "ANSWER": {
            "BEGINNER": "B",
            "INTERMEDIATE": "I",
            "EXPERT": "E",
        },
        "TEXTS": {
            "1": "Beginner",
            "2": "Intermediate",
            "3": "Expert",
        },
        "INVALID_ANSWER": "  Invalid playing level: '{}'.",
        "INVALID_DB_CODE": "\n  The computer playing level code '{}' "
        "is invalid and because of that cannot be saved in the database.\n",
    },
    "POSITION": {
        "CHOOSE_ONE": "  Please, choose a position between 1 and 9\n  1- top left corner "
        "     2- top center     3- top right corner\n  4- middle left          5- middle center "
        " 6- middle right\n  7- bottom, left corner  8- bottom center  9- bottom right corner: ",
        "INVALID": "\n  The position {} is invalid.",
        "RANGE": " Positions range from 1 to {}.\n",
        "ALREADY_IN_USE": "\n  The position {} is already in use. "
        "The positions available are : {}.\n",
        "COMPUTER_PLAYED_ON": "  The computer just played on position {}.\n",
        "COMPUTER_HAS_NOT_PLAYED_YET": "  Waiting for the computer to play before printing out "
        "the board.\n",
    },
    "LANGUAGE": {
        "PROMPT": """
  Please, choose the new default language: 
    1- For English
    2- For French
    3- For Spanish 
  Enter an option (1 - 3): """,
        "OPTIONS": {
            "ENGLISH_CODE": "1",
            "FRENCH_CODE": "2",
            "SPANISH_CODE": "3",
        },
        "CHANGE_TO": "\n  The default language has been changed to English.\n",
        "INVALID_SELECTION": "  Invalid language selection: '{}'.",
        "INVALID_DB_CODE": "\n  The language code '{}' is invalid "
        "and because of that cannot be saved in the database.\n",
    },
    "RESULT": {
        "U": "You beat the computer and won the game!",
        "C": "The computer beat you and you lost the game!",
        "N": "The game ended in a tie!",
        "INVALID_DB_CODE": "\n  The code of the result of the game '{}' is "
        "invalid and because of that cannot be saved in the database.\n",
    },
    "PLAYER": {
        "COMPUTER_TEXT": "Computer",
        "USER_TEXT": "User",
    },
}
