from WritingFile import WritingFile
from ReadingFile import ReadingFile
from Validator import Validator_collection
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=str, help='Input path for file')
parser.add_argument("rezult_name", type=str, help='Input path for rezult file')
args = parser.parse_args()

read_path = (ReadingFile(args.file_path))  # r"C:\Users\andre\Downloads\9.txt")  # ReadingFile(args.file_path)
data = read_path.get_data()
lst_valid = Validator_collection(data)
write_path = WritingFile(args.rezult_name)  # WritingFile(r"C:\Users\andre\Downloads\ll.txt")
write_path.write_file(lst_valid)

print("Число валидных записей")
print(lst_valid.count_valid())
print("Число невалидных записей")
print(lst_valid.count_invalid())
print("Число невалидных записей по типам ошибок.")
dct = lst_valid.count_invalid_general()
for key, value in dct.items():
    print(key, ':', value)

print("Число валидных и невалидных записей в результирующем файле")
read_path = ReadingFile(args.rezult_name)
data = read_path.get_data()
lst_valid = Validator_collection(data)
print("Валидных записей:")
print(lst_valid.count_valid())
print("Число невалидных записей:")
print(lst_valid.count_invalid())
