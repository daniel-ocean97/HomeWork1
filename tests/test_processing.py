import pytest

import src.processing


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("NOTEXIST", []),
    ],
)
def test_filter_by_state(client_data_fix: list[dict], state, expected: str) -> None:
    """Функция для тестирования filter_by_state в базовых случаях"""
    assert src.processing.filter_by_state(client_data_fix, state) == expected


def test_sort_by_date_descending_order(client_data_fix: list[dict]) -> None:
    """Функция для тестирования filter_by_state при указании сортировки по убыванию"""
    assert src.processing.sort_by_date(client_data_fix) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_ascending_order(client_data_fix: list[dict]) -> None:
    """Функция для тестирования filter_by_state при указании сортировки по возрастанию"""
    assert src.processing.sort_by_date(client_data_fix, sort_order=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_same_date() -> None:
    """Функция для тестирования sort_by_date при указании одинаковой даты"""
    assert src.processing.sort_by_date(
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    ) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_wrong_date() -> None:
    """Функция для тестирования sort_by_date при указании неверной даты"""
    assert (
        src.processing.sort_by_date(
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-sdfsdf8:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "20183214145 18:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30"},
            ]
        )
        == "Некорректный формат даты"
    )
