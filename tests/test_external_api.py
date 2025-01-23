from src.external_api import show_amount_in_rub
from src.utils import data_for_tests
from unittest.mock import patch, Mock

def test_show_amount_in_rub():
    """ Тест функции show_amount_in_rub в базовом случае когда обращение к API не требуется"""
    assert show_amount_in_rub(data_for_tests[0]) == 31957.58


@patch("requests.request")
def test_show_amount_in_rub(mock_request):
    """ Тест функции show_amount_in_rub в случае когда требуется обращение к API"""
    mock_response = Mock()
    mock_response.json.return_value = {'result': 10.023}
    mock_request.return_value = mock_response
    assert show_amount_in_rub(data_for_tests[1]) == 10.02
