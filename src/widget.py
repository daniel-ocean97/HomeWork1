import src.masks


def mask_account_card(account_card: str) -> str:
    """Функция для маскировки номера карты/счета"""
    account_card_list = account_card.split()
    if account_card_list[0].lower() == "счет":
        mask = src.masks.get_mask_account(str(account_card_list[-1]))
        if mask == "Введён некорректный номер счёта":
            return "Введена некорректная карта аккаунта"
        return account_card_list[0] + " " + mask
    else:
        mask = src.masks.get_mask_card_number(str(account_card_list[-1]))
        if mask == "Введён некорректный номер карты":
            return "Введена некорректная карта аккаунта"
        return " ".join(account_card_list[0:-1]) + " " + mask


def get_date(date_need_to_format: str) -> str:
    """Функция для форматирования строки с датой"""
    formated_date = []
    date_need_to_format_list = date_need_to_format.split("-")
    if len(date_need_to_format_list) != 3:
        return "Неверный формат строки"
    formated_date.append(date_need_to_format_list[2][:2])
    formated_date.append(date_need_to_format_list[1])
    formated_date.append(date_need_to_format_list[0])
    return ".".join(formated_date)
