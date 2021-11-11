import json


class ReadingFile:
    def __init__(self, path_read) -> None:
        """Инициализация пути"""
        self.path = path_read

    def get_data(self) -> list:
        # data это список словарей
        data = json.load(open(self.path, encoding='windows-1251'))
        return data
