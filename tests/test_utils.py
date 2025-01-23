from src.utils import read_from_json


def test_read_from_json():
    """ Проверяет работу функции read_from_json в базовом случае """
    assert read_from_json('../data/test.json') == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]

def test_read_from_json_empty():
    """ Проверяет работу функции read_from_json если файл пустой """
    assert read_from_json('../data/test1.json') == []

def test_read_from_json_incorrect_path():
    """ Проверяет работу функции read_from_json если файла не существует """
    assert read_from_json('../data/test12.json') == []