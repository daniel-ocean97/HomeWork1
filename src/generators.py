import random


def filter_by_currency(client_data: list[dict], currency: str) -> dict:
    """Функция-генератор, которая фильтрует переданный список по указанной валюте"""
    if client_data == [] or currency not in ["USD", "руб."]:
        return iter([])
    for client in client_data:
        if client["operationAmount"]["currency"]["name"] == currency:
            yield client


def transaction_descriptions(client_data: list[dict]) -> str:
    """Функция-генератор которая поочередно выводит описание каждой операции, переданной ей в списке"""
    for client in client_data:
        yield client["description"]


def card_number_generator(start, end):
    """Функция генерирует номер карты в нужном формате и заданном диапазоне"""
    result = ""
    if start < 0 or end > 9:
        return "Введены некорректные рамки"
    for i in range(4):
        result += " "
        for j in range(4):
            result += str(random.randint(start, end))
    return result.strip()
