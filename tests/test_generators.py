import pytest

import src.generators


def test_filter_by_currency_usd(trans_data):
    """Функция для тестирования filter_by_currency_usd с указанием валюты USD"""
    assert next(src.generators.filter_by_currency(trans_data, "USD")) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currancy_rub(trans_data):
    """Функция для тестирования filter_by_currency_usd с указанием валюты руб."""
    assert next(src.generators.filter_by_currency(trans_data, "руб.")) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_by_currancy_none(trans_data):
    """Функция для тестирования filter_by_currency_usd с указанием пустого списка"""
    result = src.generators.filter_by_currency([], "USD")
    assert not list(result)


def test_filter_by_no_currancy(trans_data):
    """Функция для тестирования filter_by_currency_usd с указанием неверной валюты"""
    result = src.generators.filter_by_currency(trans_data, "USB")
    assert not list(result)


def test_transaction_descriptions(trans_data):
    """Функция для тестирования transaction_descriptions в базовых случаях"""
    docs = src.generators.transaction_descriptions(trans_data)
    assert next(docs) == "Перевод организации"
    assert next(docs) == "Перевод со счета на счет"
    assert next(docs) == "Перевод со счета на счет"
    assert next(docs) == "Перевод с карты на карту"
    assert next(docs) == "Перевод организации"


def test_transaction_descriptions_emptylist():
    """Функция для тестирования transaction_descriptions если указан пустой список"""
    docs = src.generators.transaction_descriptions([])
    assert not list(docs)


def test_card_number_generator():
    """Функция для тестирования card_number_generator в базовом случае"""
    result = src.generators.card_number_generator(3, 7)
    for i in result:
        if i != " ":
            assert int(i) >= 3 and int(i) <= 7
    # Проверка правильности формата
    result_list = result.split()
    for number_group in result_list:
        assert len(number_group) == 4


def test_card_number_generator_wrong():
    """Функция для тестирования card_number_generator если переданы неверные рамки"""
    result = src.generators.card_number_generator(0, 10)
    assert result == "Введены некорректные рамки"


@pytest.mark.parametrize(
    "data",
    "expected",
    [
        (
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
            "Перевод со счета на счет",
        ),
        (
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
            "Перевод с карты на карту",
        ),
    ],
)
def transaction_descriptions_one(data, expected):
    actual_descriptions = list(src.generators.transaction_descriptions(data))
    assert actual_descriptions == expected
