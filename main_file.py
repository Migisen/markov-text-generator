from magic_dict import MagicDict
from text_generator import TextGenerator

with open("windows1251.txt", "r", encoding="windows-1251") as file:
    text = file.read()

base_text = MagicDict(text)
base_model = base_text.generate()
generated_text = TextGenerator(base_model, length=100000).create_text()
print(generated_text)