from typing import Union
import src.widget

def filter_by_state(client_data: list[dict], state: str = "EXECUTED") -> Union[list[dict], str]:
    """Функция фильтрует список по указанному значение state"""
    for data in client_data:
        if 'state' not in data:
            return 'Некорректный формат ввода'
    return [i for i in client_data if i["state"] == state]


def sort_by_date(client_data: list[dict], sort_order: bool = True) -> Union[list[dict], str]:
    """Функция сортирует список словарей по дате"""
    for client in client_data:
        if src.widget.get_date(client['date']) == 'Неверный формат строки':
            return 'Некорректный формат даты'
    return sorted(client_data, key=lambda x: x["date"], reverse=sort_order)


