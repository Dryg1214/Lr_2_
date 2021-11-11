import json
from tqdm import tqdm
from Validator import Validator_collection
from ReadingFile import ReadingFile


class WritingFile:
    """Класс для записи валидных записей в Файл"""

    def __init__(self, path_write) -> None:
        """Инициализация объектов класса"""
        self.path = path_write

    def write_file(self, lst) -> None:
        """Запись в файл списка словарей"""
        rezult_lst = []
        for i in tqdm(range(len(lst.data)),
                      desc="Запись результата валидации в файл",
                      ncols=150, colour='green'):
            if lst.check_dictionary(i):
                rezult_lst.append(lst.data[i])
        json.dump(rezult_lst, open(self.path, "w", encoding="windows-1251"),
                  ensure_ascii=False, indent=4)
