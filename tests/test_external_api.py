from src.external_api import show_amount_in_rub
from unittest.mock import patch, Mock


def test_show_amount_in_rub():
    """Тест функции show_amount_in_rub в базовом случае когда обращение к API не требуется"""
    assert (
        show_amount_in_rub(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )


@patch("requests.request")
def test_show_amount_in_rub_with_api(mock_request):
    """Тест функции show_amount_in_rub в случае когда требуется обращение к API"""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 10.023}
    mock_request.return_value = mock_response
    assert (
        show_amount_in_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 10.02
    )
