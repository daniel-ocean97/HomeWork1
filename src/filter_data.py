import re
from collections import Counter


def filter_by_description(transactions, search_string):
    """Функция для фильтрации транзакций по строке в описании"""
    result = []
    for transaction in transactions:
        if re.search(rf"\b{search_string}\b", transaction["description"], flags=re.IGNORECASE):
            result.append(transaction)
    return result


def categories_counter(transactions, categories):
    """Функция для подсчёта операций в указанных категориях"""
    all_categories = []
    for category in categories:
        for transaction in transactions:
            if re.search(rf"\b{category}\b", transaction["description"], flags=re.IGNORECASE):
                all_categories.append(category)

    result = Counter(all_categories)
    return dict(result)
