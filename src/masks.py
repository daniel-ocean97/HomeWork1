def get_mask_card_number(card_number: str) -> str:
    """Функция, которая создает маску номера карты.
    Передаваемое значение должно быть приведено к строковому типу в момент вызова"""
    for i in range(4, len(card_number), 5):
        card_number = card_number[:i] + " " + card_number[i:]
    card_number_list = card_number.split()
    card_number_list[1] = card_number_list[1][:2] + "**"
    card_number_list[2] = "****"
    return " ".join(card_number_list)


def get_mask_account(account: str) -> str:
    """Функция, которая создает маску номер счета
    Передаваемое значение должно быть приведено к строковому типу в момент вызова"""
    return "**" + account[-4:]
