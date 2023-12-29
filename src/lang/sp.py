SP = {
    "GAME": {
        "WELCOME": "\n  Bienvenido al juego del Tic-Tac-Toe!\n",
        "THANK_YOU": "\n  Gracias por jugar al Tic-Tac-Toe! Adiós!\n",
        "EXIT": "Salir del juego.",
        "HELP": "\n  Vas a jugar contra la computadora. "
        "Al final del juego el jugador que empezó el juego, el ganador, "
        "el estado del tablero y la fecha de hoy se guardarán en la base de datos.\n",
        "START": "\n  El juego comienza!",
        "OVER": "  ¡Juego terminado! ",
        "DB_CONNECTION": "\n  Error al establecer una conexión de "
        "base de datos. Puedes aún jugar al juego del Tic-Tac-Toe pero las "
        "estadísticas de los juegos no serán guardadas en la base de datos.\n",
        "DB_ERROR_ON_CREATE": "\n  El juego no se pudo crear correctamente "
        "debido a un error en la base de datos.\n",
        "DB_ERROR_ON_SAVE": "\n  El juego no se pudo guardar correctamente "
        "debido a un error en la base de datos.\n",
    },
    "HISTORICAL": {
        "LIST": "\n  ******** Lista de juegos anteriores: ********\n\n",
        "HEADER": "  Juego #{}(id = {}): Fecha: {} | Usuario jugó primero??: {}"
        " | Nivel de juego: {} | Resultado: {}\n",
        "NOT_FOUND": "\n  Aún no hay registro de juegos anteriores. "
        "Por favor, juega al menos una vez antes de elegir esta opción.\n",
        "DB_ERROR": "\n  No se pueden recuperar con éxito los juegos "
        "históricos debido a un error en la base de datos.\n",
    },
    "REMOVE": {
        "PROMPT": "\n  Ingresa el identificador del juego que deseas eliminar: ",
        "CONFIRMATION": "\n  ¿Estás seguro de que quieres eliminar el juego "
        "con id = {}? [S/s/N/n]: ",
        "YES": "s",
        "NO": "n",
        "INVALID_ANSWER": "  Por favor, ingrese 'S' o 's' for 'sí' o 'N' o 'n' for 'no'.",
        "SUCCESS": "\n  El juego con id = {} ha sido eliminado de la base de datos.\n",
        "FAILURE": "\n  No se ha eliminado ningún juego! "
        "El id que ingresaste no está asociado con ningún juego. "
        "Por favor, elige la opción 2 del menú para conocer el identificador del juego "
        "que deseas eliminar de la base de datos.\n",
        "INVALID": "  El identificador del juego {} es inválido. ",
        "DB_ERROR": "\n  No se puede eliminar ningún juego correctamente "
        "debido a un error en la base de datos.\n",
    },
    "REMOVE_ALL": {
        "CONFIRMATION": "\n  ¿Estás seguro de que quieres eliminar todos los juegos?"
        " de la base de datos? [S/s/N/n]: ",
        "YES": "s",
        "NO": "n",
        "INVALID_ANSWER": "  Por favor, ingrese 'S' o 's' for 'sí' o 'N' o 'n' for 'no'.",
        "SUCCESS": "\n  Todos los juegos han sido eliminados de la base de datos.\n",
        "FAILURE": "\n  Ningún juego ha sido eliminado de la base de datos. "
        "ya que ha ocurrido un error interno.",
        "DB_ERROR": "\n  No se pueden eliminar todos los juegos correctamente "
        "debido a un error en la base de datos.\n",
    },
    "MENU": {
        "TEXT": """  Por favor, seleccione una de las siguientes opciones del menú:
    1 - Comenzar un nuevo juego.
    2 - Ver una lista de juegos anteriores.
    3 - Eliminar un juego de la base de datos.
    4 - Eliminar todos los juegos de la base de datos.
    5 - Cambiar el idioma predeterminado.
    6 - Ayuda.
    7 - Salir del juego.
  Introduce una opción (1 - 7): """,
        "INVALID_OPTION": "  Opción inválida: '{}'\n",
    },
    "MESSAGES": {
        "INVALID_PLAYER": "Jugador invalido '{}'. ",
        "VALID_PLAYER_VALUES": "Los valores válidos para un jugador son '{}' "
        "indicando que ni el usuario ni la computadora han jugado en una casilla concreta, "
        "'{}' para el usuario que está jugando contra la computadora y '{}' "
        "para la propia computadora.",
        "INVALID_PATHNAME": "\n  No se pueden guardar, eliminar o cargar juegos anteriores "
        "debido a que el nombre de la ruta '{}' no es valido o "
        "no tienes suficientes permisos para escribir en ese archivo.",
        "INTERNAL_ERROR": "No podrás seguir jugando a este juego "
        "as an internal error has occurred.\n",
        "BOARD_IS_FULL": "The board is already full.",
    },
    "PLAY_FIRST": {
        "QUESTION": "\n  ¿Te gustaría ser el jugador que juega primero? [S/s/N/n]: ",
        "ANSWER": {
            "YES": "S",
            "NO": "N",
        },
        "TEXTS": {
            "1": "Sí",
            "2": "No",
        },
        "INVALID_ANSWER": "  Respuesta invalida: '{}'.",
        "INVALID_DB_CODE": "\n  El código del jugador que juega primero '{}' "
        "no es válido y por eso no se puede guardar en la base de datos.\n",
    },
    "PLAYING_LEVEL": {
        "QUESTION": """  \n  Por favor, elige el nivel de juego de la computadora:
    1- Para un nivel de principiante ingrese 'P' o 'p'. La computadora siempre juega en una posición aleatoria.
    2- Para nivel intermedio ingrese 'I' o 'i'. La computadora a veces juega aleatoriamente y otras veces piensa un poco antes de jugar.
    3- Para nivel experto ingrese 'E' o 'e'. No podrás vencer a la computadora. O perderás o el juego terminará en empate.
  Ingresa el nivel de juego de la computadora [P/p/I/i/E/e]: """,
        "ANSWER": {
            "BEGINNER": "P",
            "INTERMEDIATE": "I",
            "EXPERT": "E",
        },
        "TEXTS": {
            "1": "Principiante",
            "2": "Intermedio",
            "3": "Experto",
        },
        "INVALID_ANSWER": "  Nivel de juego inválido: '{}'.",
        "INVALID_DB_CODE": "\n  El código del nivel de juego de la computadora"
        " '{}' no es válido y por eso no se puede guardar en la base de datos.\n",
    },
    "POSITION": {
        "CHOOSE_ONE": "  Por favor, elija una posición entre 1 y 9\n  "
        "1- esquina superior izquierda "
        " 2- medio superior  3- esquina superior derecha\n  "
        "4- centro izquierdo            5- centro medio "
        "   6- centro derecho\n  7- esquina inferior izquierda  "
        "8- medio inferior  9- esquina inferior derecha: ",
        "INVALID": "\n  La posición {} es invalida.",
        "RANGE": " Las posiciones van desde 1 hasta {}.\n",
        "ALREADY_IN_USE": "\n  La posición {} está en uso. Las posiciones disponibles son : {}.\n",
        "COMPUTER_PLAYED_ON": "  La computadora acaba justo de jugar en la posición {}.\n",
        "COMPUTER_HAS_NOT_PLAYED_YET": "  Esperando a que la computadora juegue antes de imprimir "
        "el tablero.\n",
    },
    "LANGUAGE": {
        "PROMPT": """
  Por favor, elige el nuevo idioma predeterminado: 
    1- Para inglés
    2- Para francés
    3- Para español
  Introduce una opción (1 - 3): """,
        "OPTIONS": {
            "ENGLISH_CODE": "1",
            "FRENCH_CODE": "2",
            "SPANISH_CODE": "3",
        },
        "CHANGE_TO": "\n  El idioma predeterminado ha sido cambiado a español.\n",
        "INVALID_SELECTION": "  Selección de idioma no válida: '{}'.",
        "INVALID_DB_CODE": "\n  El código de idioma '{}' no es válido "
        "y por eso no se puede guardar en la base de datos.\n",
    },
    "RESULT": {
        "U": "¡Venciste a la computadora y ganaste el juego!",
        "C": "¡La computadora te ganó y perdiste el juego!",
        "N": "¡El partido acabó en empate!",
        "INVALID_DB_CODE": "\n  El código del resultado del juego '{}' no es válido "
        "y por eso no se puede guardar en la base de datos.\n",
    },
    "PLAYER": {
        "COMPUTER_TEXT": "Computadora",
        "USER_TEXT": "Usuario",
    },
}
