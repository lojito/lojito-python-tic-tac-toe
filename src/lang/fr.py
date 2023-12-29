FR = {
    "GAME": {
        "WELCOME": "\n  Bienvenue dans le jeu Tic-Tac-Toe!\n",
        "THANK_YOU": "\n  Merci d'avoir joué au jeu Tic-Tac-Toe. Au revoir!\n",
        "EXIT": "Quittez le jeu.",
        "HELP": "\n  Vous allez jouer contre l'ordinateur. "
        "À la fin du jeu, le joueur qui a commencé le jeu, le gagnant, "
        "l'état du plateau et la date du jour seront enregistrés dans la base de données.\n",
        "START": "\n  Le jeu commence!",
        "OVER": "  Jeu terminé! ",
        "DB_CONNECTION": "\n  Erreur de connexion à la base de données. "
        "Vous pouvez toujours jouer au jeu Tic-Tac-Toe mais les statistiques "
        "des jeux ne seront pas enregistrés dans la base de données.\n",
        "DB_ERROR_ON_CREATE": "\n  Le jeu n'a pas pu être créé avec succès "
        "en raison d'une erreur de base de données.\n",
        "DB_ERROR_ON_SAVE": "\n  Le jeu n'a pas pu être sauvegardé avec succès "
        "en raison d'une erreur de base de données.\n",
    },
    "HISTORICAL": {
        "LIST": "\n  ******** Liste des jeux précédents: ********\n\n",
        "HEADER": "  Jeu #{}(id = {}): Date: {} | L'utilisateur a joué en premier?: {}"
        " | Niveau de jeu: {} | Résultat: {}\n",
        "NOT_FOUND": "\n  Il n'y a pas encore de trace des jeux précédents. "
        "Veuillez jouer au moins une fois avant de choisir cette option.\n",
        "DB_ERROR": "\n  Impossible de récupérer les jeux historiques "
        "en raison d'une erreur de base de données.\n",
    },
    "REMOVE": {
        "PROMPT": "\n  Entrez l'identifiant du jeu que vous souhaitez supprimer: ",
        "CONFIRMATION": "\n  Êtes-vous sûr de vouloir supprimer le jeu "
        "avec l'identifiant = {}? [O/o/N/n]: ",
        "YES": "o",
        "NO": "n",
        "INVALID_ANSWER": "  Veuillez saisir 'O' ou 'o' for 'oui' ou 'N' ou 'n' for 'non'.",
        "SUCCESS": "\n  Le jeu avec l'identifiant = {} a été supprimé de la base de données.\n",
        "FAILURE": "\n  Aucun jeu n'a été supprimé! "
        "L'identifiant que vous avez saisi n'est associé à aucun jeu. "
        "Veuillez choisir l'option 2 dans le menu afin de connaître l'identifiant du jeu. "
        "vous souhaitez supprimer de la base de données.\n",
        "INVALID": "  Identifiant de jeu invalide {}. ",
        "DB_ERROR": "\n  Impossible de supprimer un jeu "
        "en raison d'une erreur de base de données.\n",
    },
    "REMOVE_ALL": {
        "CONFIRMATION": "\n  Êtes-vous sûr de vouloir supprimer tous les jeux"
        " de la base de données? [O/o/N/n]: ",
        "YES": "o",
        "NO": "n",
        "INVALID_ANSWER": "  Veuillez saisir 'O' ou 'o' for 'oui' ou 'N' ou 'n' for 'non'.",
        "SUCCESS": "\n  Tous les jeux ont été supprimés de la base de données.\n",
        "FAILURE": "\n  Aucun jeu n'a été supprimé de la base de données "
        "car une erreur interne s'est produite.",
        "DB_ERROR": "\n  Impossible de supprimer tous les jeux "
        "en raison d'une erreur de base de données.\n",
    },
    "MENU": {
        "TEXT": """  Veuillez sélectionner l'une des options de menu suivantes:
    1 - Commencer un nouveau jeu.
    2 - Voir une liste des jeux précédents.
    3 - Supprimer un jeu de la base de données.
    4 - Supprimer tous les jeux de la base de données.
    5 - Changer la langue par défaut.
    6 - Aide.
    7 - Quittez le jeu.
  Entrez une option (1 - 7): """,
        "INVALID_OPTION": "  Option invalide: '{}'\n",
    },
    "MESSAGES": {
        "INVALID_PLAYER": "Joueur invalide '{}'. ",
        "VALID_PLAYER_VALUES": "Les valeurs valides pour un joueur sont '{}' "
        "indiquant que ni l'utilisateur ni l'ordinateur n'ont joué sur une case particulière, "
        "'{}' pour l'utilisateur qui joue contre l'ordinateur et '{}' "
        "pour l'ordinateur lui-même.",
        "INVALID_PATHNAME": "\n  Impossible de sauvegarder, supprimer "
        "ou charger les jeux précédents "
        "car le chemin d'accès '{}' n'est pas valide ou "
        "vous n'avez pas suffisamment d'autorisations pour écrire dans ce fichier.",
        "INTERNAL_ERROR": "Vous ne pourrez pas continuer à jouer à ce jeu "
        "car une erreur interne s'est produite.\n",
        "BOARD_IS_FULL": "Le tableau est déjà plein.",
    },
    "PLAY_FIRST": {
        "QUESTION": "\n  Aimeriez-vous être le joueur qui joue en premier? "
        "[O/o/N/n]: ",
        "ANSWER": {
            "YES": "O",
            "NO": "N",
        },
        "TEXTS": {
            "1": "Oui",
            "2": "Non",
        },
        "INVALID_ANSWER": "  Réponse invalide: '{}'.",
        "INVALID_DB_CODE": "\n  Le code du joueur qui joue en premier '{}' "
        "n'est pas valide et ne peut donc pas être enregistré "
        "dans la base de données.\n",
    },
    "PLAYING_LEVEL": {
        "QUESTION": """  \n  S'il vous plaît, choisissez le niveau de jeu de l'ordinateur:
    1- Pour un niveau débutant saisissez 'D' or 'd'. L'ordinateur joue à chaque fois sur une position aléatoire.
    2- Pour un niveau intermédiaire saisissez 'I' or 'i'. L'ordinateur joue parfois de manière aléatoire et d'autres fois, réfléchissez avant de jouer.
    3- Pour un niveau expert saisissez 'E' or 'e'. Vous ne pourrez pas battre l'ordinateur. Soit vous perdrez, soit la partie se terminera par un match nul.
  Entrez le niveau de jeu de l'ordinateur [D/d/I/i/E/e]: """,
        "ANSWER": {
            "BEGINNER": "D",
            "INTERMEDIATE": "I",
            "EXPERT": "E",
        },
        "TEXTS": {
            "1": "Débutant",
            "2": "Intermédiaire",
            "3": "Expert",
        },
        "INVALID_ANSWER": "  Niveau de jeu invalide: '{}'.",
        "INVALID_DB_CODE": "\n  Le code de niveau de jeu de l'ordinateur '{}' "
        "n'est pas valide et ne peut donc pas être enregistré "
        "dans la base de données.\n",
    },
    "POSITION": {
        "CHOOSE_ONE": "  Veuillez choisir une position entre 1 et 9\n  1- coin supérieur gauche "
        " 2- centre supérieur  3- coin supérieur droit\n  "
        "4- milieu gauche          5- milieu centre "
        "    6- milieu droit\n  7- coin inférieur gauche  8- centre inférieur"
        "  9- coin inférieur droit: ",
        "INVALID": "\n  La position {} n'est pas valide.",
        "RANGE": " Les positions vont de 1 à {}.\n",
        "ALREADY_IN_USE": "\n  La position {} est déjà utilisée. "
        "Les positions disponibles sont : {}.\n",
        "COMPUTER_PLAYED_ON": "  L'ordinateur vient de jouer en position {}.\n",
        "COMPUTER_HAS_NOT_PLAYED_YET": "  Attendre que l'ordinateur joue avant d'imprimer  "
        "le tableau.\n",
    },
    "LANGUAGE": {
        "PROMPT": """
  Veuillez choisir la nouvelle langue par défaut: 
    1- Pour l'anglais
    2- Pour le français
    3- Pour l'espagnol
  Entrez une option (1 - 3): """,
        "OPTIONS": {
            "ENGLISH_CODE": "1",
            "FRENCH_CODE": "2",
            "SPANISH_CODE": "3",
        },
        "CHANGE_TO": "\n  La langue par défaut a été changée en français.\n",
        "INVALID_SELECTION": "  Sélection de langue invalide: '{}'.",
        "INVALID_DB_CODE": "\n  Le code de langue '{}' n'est pas valide "
        "et ne peut donc pas être enregistré dans la base de données.\n",
    },
    "RESULT": {
        "U": "Vous avez battu l'ordinateur et gagné la partie!",
        "C": "L'ordinateur vous a battu et vous avez perdu la partie!",
        "N": "Le match s'est terminé sur un match nul!",
        "INVALID_DB_CODE": "\n  Le code du résultat de jeu '{}' n'est pas valide "
        "et ne peut donc pas être enregistré dans la base de données..\n",
    },
    "PLAYER": {
        "COMPUTER_TEXT": "Computer",
        "USER_TEXT": "Utilisateur",
    },
}
