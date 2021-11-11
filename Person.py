
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=str, help='Input path for file')
parser.add_argument("rezult_name", type=str, help='Input name for rezult file')
args = parser.parse_args()
"""
"""
print(args.file_path)
print(args.rezult_name)
"""


class Person:
    email: str
    weight: int
    snils: int
    passport_number: int
    university: str
    age: int
    academic_degree: str
    worldview: str
    address: str

    def __init__(self, em, we, sn, pa, un, ag, ac, wo, ad) -> None:
        self.email = em
        self.weight = we
        self.snils = sn
        self.passport_number = pa
        self.university = un
        self.age = ag
        self.academic_degree = ac
        self.worldview = wo
        self.address = ad


def collection_instances(path) -> list:
    """Cозданиe коллекции экземпляров класса записи (только вопрос зачем)"""
    read_path = ReadingFile(path)
    data = read_path.get_data()
    # ***
    need_lst = list()
    for pd in data:
        need_lst.append(
            Person(
                pd["email"],
                pd["weight"],
                pd["snils"],
                pd["passport_number"],
                pd["university"],
                pd["age"],
                pd["academic_degree"],
                pd["worldview"],
                pd["address"]))
    # ***
    return need_lst
