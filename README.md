# Виджет банковских операций клиента
## Описание
Виджет банковских операций клиента это учебный проект целью которого
является обучение работы с такими инструментами как Poetry и Git
### Установка
Клонируйте Git репозиторий
```
git clone https://github.com/daniel-ocean97/HomeWork1
```
### Использование разработанных функций 

1. Функция get_mask_card_number
    принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате 
    XXXX XX** **** XXXX, где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные
    символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
      7000792289606361     # входной аргумент
      7000 79** **** 6361  # выход функции

2. Функция get_mask_account
    принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
    Пример работы функции:
      73654108430135874305  # входной аргумент
      **4305  # выход функции
3. Функция mask_account_card 
    умеет обрабатывать информация как о картах, так и о счетах.
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером. Для карт и счетов используются разные типы маскировки (а именно функции
    которые описаны выше)
    
    Пример для карты
    Visa Platinum 7000792289606361  # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции

    Пример для счета
    Счет 73654108430135874305  # входной аргумент
    Счет **4305  # выход функции
4. Функция get_date принимает на вход строку с датой в формате 
   "2024-03-11T02:26:18.671407"
   и возвращает строку с датой в формате 
   "ДД.ММ.ГГГГ"("11.03.2024").
5. Функция filter_by_state  принимает список словарей и опционально значение для ключа 
   state(по умолчанию'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
   state соответствует указанному значению.
6. Функция sort_by_date принимает список словарей и необязательный параметр, задающий порядок сортировки
   (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date).
   Примеры работы функции
   Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CA