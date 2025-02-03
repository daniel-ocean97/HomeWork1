import re
from collections import Counter


def filter_by_description(transactions, search_string):
    pattern = re.compile(fr'\b{search_string}\b')
    result = []
    for transaction in transactions:
        if re.search(pattern, transaction["description"]):
            result.append(transaction)
    return result


def state_counter(transactions, categories):
    all_categories = []
    for category in categories:
        for transaction in transactions:
            if re.search(fr"\b{category}\b", transaction["description"], flags=re.IGNORECASE):
                all_categories.append(category)

    result = Counter(all_categories)
    return dict(result)


