import os

from src.filter_data import filter_by_description
from src.processing import filter_by_state, sort_by_date
from src.reading_data import reading_from_csv, reading_from_exсel
from src.utils import read_from_json
from src.widget import get_date, mask_account_card

DATA_DIRECTORY = os.path.join("..", "data")


def main():
    """Функция, которая отвечает за основную логику проекта
     с пользователем и связывает функциональности между собой."""
    print(
        """Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями."""
    )
    type_of_file = input(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
    )
    if type_of_file == "1":
        print("Для обработки выбран JSON-файл.")
        path_to_file = os.path.join(DATA_DIRECTORY, "operations.json")
        data = read_from_json(path_to_file)
        state = ask_user()
    elif type_of_file == "2":
        print("Для обработки выбран CSV-файл.")
        path_to_file = os.path.join(DATA_DIRECTORY, "transactions.csv")
        data = reading_from_csv(path_to_file)
        state = ask_user()
    else:
        print("Для обработки выбран XLSX-файл.")
        path_to_file = os.path.join(DATA_DIRECTORY, "transactions_excel.xlsx")
        data = reading_from_exсel(path_to_file)
        state = ask_user()
    filtered_data = filter_by_state(data, state)
    print(f"Операции отфильтрованы по статусу {state}")
    sort_request = input("Отсортировать операции по дате? Да/Нет\n")
    if sort_request.lower() == "да":
        ascending_order = input("Отсортировать по возрастанию или по убыванию?\n")
        if ascending_order.lower() == "по возрастанию":
            filtered_data = sort_by_date(filtered_data, sort_order=False)
        else:
            filtered_data = sort_by_date(filtered_data, sort_order=True)
    rub_request = input("Выводить только рублевые транзакции? Да/Нет\n")
    if rub_request.lower() == "да":
        if type_of_file == "1":
            result = [i for i in filtered_data if i["operationAmount"]["currency"]["code"] == "RUB"]
        else:
            result = [i for i in filtered_data if i["currency_code"] == "RUB"]
    else:
        result = filtered_data
    description_filter_order = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if description_filter_order.lower() == "да":
        searchig_string = input("По какому слову будем искать?\n")
        result = filter_by_description(result, searchig_string)
    print("Распечатываю итоговый список транзакций:")
    print(f"Всего банковских операций в выборке: {len(result)}")
    for transaction in result:
        print(f"{get_date(transaction["date"])} {transaction["description"]}")
        if transaction["description"].lower() == "открытие вклада":
            print(mask_account_card(transaction["to"]))
        else:
            print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
        if type_of_file == "1":
            print(f"Сумма: {transaction["operationAmount"]["amount"]}\n")
        else:
            print(f"Сумма: {transaction["amount"]}\n")


def ask_user():
    available_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
                            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )
        if state.upper() in available_states:
            break
    return state


if __name__ == "__main__":
    main()
