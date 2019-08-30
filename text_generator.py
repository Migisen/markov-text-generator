import random
import re


class TextGenerator:
    """
    Генерация текста на основе цепей Маркова

    length:      Длинна необходимого текста
    begin:       Стартовое слово
    random_type: Способ выбора следующего слова

    """

    def __init__(self, model, length=100, begin=None):
        self.model = model
        self.model_keys = list(model.keys())
        self.length = length
        self.begin = begin
        self.result = ""

    @staticmethod
    def weighted_random(state):
        word = random.choices(list(state.keys()), weights=list(state.values()))
        return word[0]

    """
    Основной метод генерации

    """

    def create_text(self):
        if self.begin is None:
            self.begin = random.choice(list(self.model.keys()))
        self.result = self.begin.capitalize()
        for i in range(self.length - 1):
            next_word = self.weighted_random(self.model[self.begin][0])
            if next_word is None:
                next_word = random.choice(list(self.model.keys()))
            self.check_sentence(next_word)
            self.begin = next_word
        return self.result

    """
    Метод проверяет, нужно ли добоалять заглавную букву

    """

    def check_sentence(self, next_word):
        pattern = re.compile(r"[.;!?]")
        if pattern.match(self.begin) and not pattern.match(next_word):
            self.result += f"\n{next_word.capitalize()}"
        else:
            self.result += f" {next_word}"
