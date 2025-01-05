import random

def filter_by_currency(client_data: list[dict], currency: str) -> dict:
    for client in client_data:
        if client["operationAmount"]["currency"]["name"] == currency:
            yield client



def transaction_descriptions(client_data: list[dict]) -> str:
    for client in client_data:
        yield client['description']



def card_number_generator(start, end):
    result = ''
    for i in range(4):
        result += ' '
        for j in range(4):
            result += str(random.randint(start, end))
    return result.strip()





