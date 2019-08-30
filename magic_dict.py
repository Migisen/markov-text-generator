import itertools
import re
import pickle


class MagicDict(object):

    """
    Создание объекта для последующей генерации текста.

    prepared_text: Разбитый на отдельные слова текст
    state_counts: Количество уникальных слов в словаре
    model: Финальный словарь

    """

    def __init__(self, raw_text, prepared_text=""):
        self.text = raw_text
        self.state_counts = int()
        self.model = {}
        self.prepared_text = self.prepare_text()

    """
    Метод создает словарь, где ключи - это список встреченных в тексте слов, а
    их значения - это список со следующими после них словами и частотой их употребления.
    
    state:      Текущее слово
    next_state: Следующее после state слово 

    """

    def generate(self):
        for state, next_state in itertools.zip_longest(self.prepared_text, self.prepared_text[1:]):
            if state in self.model:
                for word_dict in self.model[state]:
                    if next_state in word_dict.keys():
                        word_dict[next_state] += 1
                    else:
                        self.state_counts += 1
                        word_dict[next_state] = 1
            else:
                if next_state is None:
                    self.model[state] = [{self.prepared_text[0]: 1}]
                else:
                    self.model[state] = [{next_state: 1}]
        return self.model

    """
    Метод приводит заданный текст в необходимую форму.
    
    regex: Строка позволяющай выбрать свой собственный шаблон для regex.
    
    """

    def prepare_text(self, regex=""):
        regex_split = re.compile(r"\w+|[^\w\s]")
        if regex != "":
            regex = re.compile(r"{}".format(regex))
        else:
            regex = re.compile(r"[\d(/|{\]\[};—\-\"#*')«»„“]")
        self.prepared_text = regex.sub("", self.text).lower()
        self.prepared_text = regex_split.findall(self.prepared_text)
        return self.prepared_text
