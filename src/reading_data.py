import csv
import os

import pandas as pd

data_directory = os.path.join("..", "data")
csv_file_path = os.path.join(data_directory, "transactions.csv")


def reading_from_csv(path_to_file):
    """Функция для чтения данных из csv файла"""
    result = []
    with open(path_to_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            temp_res = {}
            for key, value in row.items():
                keys = key.split(";")
                values = value.split(";")
                for i in range(len(keys)):
                    temp_res[keys[i]] = values[i]
            result.append(temp_res)

    return result


# print(reading_from_csv(csv_file_path))

exel_file_path = os.path.join(data_directory, "transactions_excel.xlsx")


def reading_from_exсel(path_to_file):
    """Функция для чтения данных из excel файла"""
    excel_data = pd.read_excel(path_to_file)
    dict_data = excel_data.to_dict()
    file_len = len(excel_data)
    result = []
    for i in range(file_len):
        result.append({})
    for key in dict_data:
        for i in range(file_len):
            result[i][key] = dict_data[key][i]
    return result


CONST = reading_from_csv(csv_file_path)
