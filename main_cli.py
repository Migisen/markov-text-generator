import argparse
import pickle

from magic_dict import MagicDict
from text_generator import TextGenerator

# CLI
parser = argparse.ArgumentParser(description="Генератор текста на основе цепей Маркова")
parser.add_argument("dir", type=str, help="Путь к файлу с текстом или модели, если установлен параметр load-model")
parser.add_argument("--save-dir", type=str, help="Путь для сохранения модели")
parser.add_argument("--save-model", type=bool, help="Сохранять ли модель", default=False)
parser.add_argument("--load-model", type=bool, help="Если True, загружает заданную модель")
parser.add_argument("--length", type=int, help="Длинна генерируемого текста", default=20)
parser.add_argument("--encoding", type=str, help="Кодировка файла", default="utf-8")

args = parser.parse_args()

if args.load_model:
    # Загрузка модели
    with open(args.dir, "rb") as file:
        base_model = pickle.load(file)
else:
    # Открытие файла с текстом и создание модели
    with open(args.dir, "r", encoding=args.encoding) as file:
        text = file.read()
    base_text = MagicDict(text)
    base_model = base_text.generate()


# Создание модели и генерация текста
if args.save_model:  # Сохранение модели в файл(pickle)
    with open(args.save_dir, "wb") as file:
        pickle.dump(base_model, file, fix_imports=False)
generated_text = TextGenerator(base_model, args.length).create_text()
print(generated_text)
