from src.filter_data import categories_counter, filter_by_description


def test_filter_by_description(trans_data):
    """Функция для тестирования функции filter_by_description"""
    assert filter_by_description(trans_data, "Перевод с карты на карту") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


def test_categories_counter(trans_data):
    """Функция для тестирования функции categories_counter"""
    assert categories_counter(
        trans_data, ["Перевод с карты на карту", "Перевод организации", "Перевод со счета на счет"]
    ) == {"Перевод с карты на карту": 1, "Перевод организации": 2, "Перевод со счета на счет": 2}
