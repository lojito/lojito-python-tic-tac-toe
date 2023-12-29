from src.lang.en import EN
from src.lang.fr import FR
from src.lang.sp import SP

ENGLISH_CODE = "EN"
FRENCH_CODE = "FR"
SPANISH_CODE = "SP"


class Dictionary:
    texts = {
        ENGLISH_CODE: EN,
        SPANISH_CODE: SP,
        FRENCH_CODE: FR,
    }

    default_language = ENGLISH_CODE
    user_language = "1"

    @classmethod
    def get_text(cls, key1, key2, key3=None, language=None):
        lang = cls.default_language if language is None else language
        if key3 is None:
            return cls.texts[lang][key1][key2]
        return cls.texts[lang][key1][key2][key3]

    @classmethod
    def change_default_language(cls):
        from src.ui.prompt import prompt_change_language

        lang = prompt_change_language()
        if lang == "1":
            cls.default_language = ENGLISH_CODE
            cls.user_language = "1"
        elif lang == "2":
            cls.default_language = FRENCH_CODE
            cls.user_language = "2"
        else:
            cls.default_language = SPANISH_CODE
            cls.user_language = "3"
