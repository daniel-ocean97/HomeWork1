import json


def read_from_json(path_to_json: str):
    """
    Функция считывает данные из json файла и возвращает Python объект.
    Если файл не найден, пуст или не является списком - возвращается пустой список
    """
    data = []
    try:
        with open(path_to_json, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return data
    return data


data_for_tests = read_from_json("../data/operations.json")
