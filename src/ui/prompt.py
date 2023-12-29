from src.lang.translation import Dictionary


def prompt_integer_value(key1, key2):
    while True:
        try:
            value = int(input(Dictionary.get_text(key1, key2)))
        except ValueError as e:
            print(
                Dictionary.get_text(key1, "INVALID").format(
                    str(e).split(":")[1].strip()
                ),
                "\n",
            )
        else:
            return value


def prompt_game_setting(option):
    user_answer = input(Dictionary.get_text(option, "QUESTION"))
    while (user_answer.upper()) not in list(
        Dictionary.get_text(option, "ANSWER").values()
    ):
        print(Dictionary.get_text(option, "INVALID_ANSWER").format(user_answer))
        user_answer = input(Dictionary.get_text(option, "QUESTION"))
    return user_answer.upper()


def prompt_remove_game_confirmation(game_id=None):
    if game_id is None:
        remove = "REMOVE_ALL"
        confirmation = Dictionary.get_text(remove, "CONFIRMATION")
    else:
        remove = "REMOVE"
        confirmation = Dictionary.get_text(remove, "CONFIRMATION").format(game_id)

    while (user_answer := input(confirmation).lower()) not in (
        ([Dictionary.get_text(remove, "YES"), Dictionary.get_text(remove, "NO")])
    ):
        print(Dictionary.get_text(remove, "INVALID_ANSWER"))
    return user_answer


def prompt_change_language():
    user_answer = input(Dictionary.get_text("LANGUAGE", "PROMPT"))
    while (user_answer.upper()) not in list(
        Dictionary.get_text("LANGUAGE", "OPTIONS").values()
    ):
        print(Dictionary.get_text("LANGUAGE", "INVALID_SELECTION").format(user_answer))
        user_answer = input(Dictionary.get_text("LANGUAGE", "PROMPT"))
    return user_answer.upper()
