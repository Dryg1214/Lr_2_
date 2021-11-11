import re
from tqdm import tqdm
from ReadingFile import ReadingFile


class Validator_elem:
    """Валидатор для элемента списка (словаря)"""
    dict: dict()
    email: str
    weight: int
    snils: str
    passport_number: int
    university: str
    age: int
    academic_degree: str
    worldview: str
    address: str

    def __init__(self, dict) -> None:
        """Конструктор класса"""
        self.email = dict["email"]
        self.weight = dict["weight"]
        self.snils = dict["snils"]
        self.passport_number = dict["passport_number"]
        self.university = dict["university"]
        self.age = dict["age"]
        self.academic_degree = dict["academic_degree"]
        self.worldview = dict["worldview"]
        self.address = dict["address"]

    def check_email(self) -> bool:
        """Проверка почты"""
        pattern = "^[^\\s@]+@([^\\s@.,]+\\.)+[^\\s@.,]{2,}$"
        if re.match(pattern, self.email):
            return True
        return False

    def check_weight(self) -> bool:
        """Проверка веса"""
        if isinstance(self.weight, int):
            if 30 <= self.weight < 200:
                return True
        return False

    def check_snils(self) -> bool:
        """Проверка снилса"""
        if isinstance(self.snils, str):
            if re.match('[0-9]*$', self.snils):
                if 9999999999 < int(
                        self.snils) < 100000000000:  # почему несмотря на то что в классе мы объявили
                    # поле снилса интом, оно выкидывает здесь и требует явного
                    return True
        return False                                    # приведения типов?

    def check_passport_number(self) -> bool:
        """Проверка паспорта"""
        # if re.match('[0-9]*$', str(self.passport_number)):
        if isinstance(self.passport_number, int):
            if 100000 <= self.passport_number < 1000000:
                return True
        return False

    def check_university(self) -> bool:
        """Проверка названия университета"""
        pattern = "^([а-яА-Я]|-| ){3,}$"
        if re.match(pattern, self.university):
            return True
        return False

    def check_age(self) -> bool:
        """Проверка возраста человека на валидность"""
        if isinstance(self.age, int):
            if 0 < self.age < 100:
                return True
        return False

    def check_academic_degree(self) -> bool:
        """Проверка академической степени"""
        pattern = "Магистр|Специалист|Бакалавр|Кандидат наук|Доктор наук|"
        if re.match(pattern, self.academic_degree):
            return True
        return False

    def check_worldview(self) -> bool:
        """Проверка вероисповедания"""
        pattern = "^.+(?:изм|анство)$"
        if re.match(pattern, self.worldview):
            return True
        return False

    def check_address(self) -> bool:
        """Проверка адреса"""
        pattern = "(?:ул\\.|Аллея) (?:им[\\.\\s]|)[^\\s]+ [^\\s]*(?:\\s|)\\d+"
        if re.match(pattern, self.address):
            return True
        return False


class Validator_collection:
    """Валидатор с коллекцией экземпляров класса записей"""
    data: list

    def __init__(self, collection_ins) -> None:
        """Инициализация списком с экземпляров класса записей"""
        self.data = collection_ins

    def check_dictionary(self, index) -> dict():
        check = False
        if Validator_elem(self.data[index]).check_email() and Validator_elem(self.data[index]).check_weight() \
                and Validator_elem(self.data[index]).check_snils() and Validator_elem(self.data[index]).check_passport_number()\
                and Validator_elem(self.data[index]).check_university() and Validator_elem(self.data[index]).check_age()\
                and Validator_elem(self.data[index]).check_academic_degree() and Validator_elem(self.data[index]).check_worldview()\
                and Validator_elem(self.data[index]).check_address():
            check = True
        return check

    def count_valid(self) -> int:
        """Число валидных записей"""
        count_correct = 0
        for i in tqdm(range(len(self.data)),
                      desc="Подсчёт количества валидных записей",
                      ncols=150, colour='green'):
            if self.check_dictionary(i):
                count_correct += 1
        return count_correct

    def count_invalid(self) -> int:
        """Число невалидных записей"""
        count_incorrect = 0
        for i in tqdm(range(len(self.data)),
                      desc="Подсчёт количества невалидных записей",
                      ncols=150, colour='green'):
            if not self.check_dictionary(i):
                count_incorrect += 1
        return count_incorrect

    def count_invalid_general(self) -> dict:
        """Количество некорректных записей отдельно"""
        count_email = 0
        count_weight = 0
        count_snils = 0
        count_passport_number = 0
        count_university = 0
        count_age = 0
        count_academic_degree = 0
        count_worldview = 0
        count_address = 0
        for index in tqdm(range(len(self.data)),
                          desc="Подсчёт некорректных записей  данных",
                          ncols=150, colour='green'):
            if not Validator_elem(self.data[index]).check_email():
                count_email += 1
            if not Validator_elem(self.data[index]).check_weight():
                count_weight += 1
            if not Validator_elem(self.data[index]).check_snils():
                count_snils += 1
            if not Validator_elem(self.data[index]).check_passport_number():
                count_passport_number += 1
            if not Validator_elem(self.data[index]).check_university():
                count_university += 1
            if not Validator_elem(self.data[index]).check_age():
                count_age += 1
            if not Validator_elem(self.data[index]).check_academic_degree():
                count_academic_degree += 1
            if not Validator_elem(self.data[index]).check_worldview():
                count_worldview += 1
            if not Validator_elem(self.data[index]).check_address():
                count_address += 1

        rezult = {"invalid_email": count_email,
                  "invalid_weight": count_weight,
                  "invalid_snils": count_snils,
                  "invalid_passport_number": count_passport_number,
                  "invalid_university": count_university,
                  "invalid_age": count_age,
                  "invalid_academic_degree": count_academic_degree,
                  "invalid_worldview": count_worldview,
                  "invalid_address": count_address}
        return rezult


"""
read_path = ReadingFile()
data = read_path.get_data()
lst_valid = Validator_collection(data)
print(lst_valid.count_invalid())

#print(Validator_elem(lst_valid.data[0]).check_snils())
#print (lst_valid.check_dictionary(6))
print (lst_valid.count_valid())
print (lst_valid.count_invalid_general())
"""
