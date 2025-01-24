import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("API_KEY")


def show_amount_in_rub(data):
    """Функция, которая выводит сумму переданной транзакции в рублях"""
    currency = data["operationAmount"]["currency"]["code"]
    amount = data["operationAmount"]["amount"]
    if currency == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        payload = {}
        headers = {
            "apikey": f"{token}"
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()
        return round(result["result"], 2)
