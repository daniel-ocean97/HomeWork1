from unittest.mock import mock_open, patch

import pandas as pd

from src.reading_data import reading_from_csv, reading_from_exсel


def test_reading_from_exсel():
    """Функция для тестирования reading_from_exel"""
    mock_data = pd.DataFrame({"id": [3107343, 2130098, 4653427], "state": ["EXECUTED", "CANCELED", "EXECUTED"]})

    with patch("pandas.read_excel", return_value=mock_data):
        result = reading_from_exсel("any_path.xlsx")

    expected_result = [
        {"id": 3107343, "state": "EXECUTED"},
        {"id": 2130098, "state": "CANCELED"},
        {"id": 4653427, "state": "EXECUTED"},
    ]

    assert result == expected_result


def test_reading_from_csv():
    """Функция для тестирования reading_from_csv"""
    mock_csv_content = "id;state\n650703;EXECUTED\n3598919;EXECUTED\n"

    m = mock_open(read_data=mock_csv_content)

    with patch("builtins.open", m):
        result = reading_from_csv("mock_file.csv")

    expected_result = [{"id": "650703", "state": "EXECUTED"}, {"id": "3598919", "state": "EXECUTED"}]

    assert result == expected_result
