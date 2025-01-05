import pytest
import src.generators
from tests.conftest import trans_data


def test_filter_by_currency_usd(trans_data):
    assert next(src.generators.filter_by_currency(trans_data, "USD")) ==  {
                 "id": 939719570,
                "state": "EXECUTED",
                 "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации",
                 "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702",
             }


def test_filter_by_currancy_rub(trans_data):
    assert next(src.generators.filter_by_currency(trans_data, "руб.")) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }


def test_filter_by_currancy_none(trans_data):
    result = src.generators.filter_by_currency([], 'USD')
    assert not list(result)


def test_filter_by_no_currancy(trans_data):
    result = src.generators.filter_by_currency(trans_data, 'USB')
    assert not list(result)


def test_transaction_descriptions(trans_data):
    docs = src.generators.transaction_descriptions(trans_data)
    assert next(docs) == "Перевод организации"
    assert next(docs) == "Перевод со счета на счет"
    assert next(docs) == "Перевод со счета на счет"
    assert next(docs) == "Перевод с карты на карту"
    assert next(docs) == "Перевод организации"


def test_transaction_descriptions_emptylist():
    docs = src.generators.transaction_descriptions([])
    assert not list(docs)


def test_card_number_generator():
    result = src.generators.card_number_generator(3, 7)
    for i in result:
        if i != ' ':
            assert int(i) >= 3 and int(i) <= 7
    #Проверка правильности формата
    result_list = result.split()
    for number_group in result_list:
        assert len(number_group) == 4



def test_card_number_generator_wrong():
    result = src.generators.card_number_generator(0, 10)
    assert result == "Введены некорректные рамки"