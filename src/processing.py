def filter_by_state(client_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список по указанному значение state"""
    return [i for i in client_data if i["state"] == state]


def sort_by_date(client_data: list[dict], sort_order: bool = True) -> list[dict]:
    """Функция сортирует список словарей по дате"""
    return sorted(client_data, key=lambda x: x["date"], reverse=sort_order)
