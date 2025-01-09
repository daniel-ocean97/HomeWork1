import src.masks


def test_get_mask_card_number() -> None:
    """Функция для тестирования get_mask_card_number в базовом случае"""
    assert src.masks.get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_wrong() -> None:
    """Функция для тестирования get_mask_card_number если введен некорректный номер карты"""
    assert src.masks.get_mask_card_number("700fjghfs2289606") == "Введён некорректный номер карты"


def test_get_mask_card_number_without_number() -> None:
    """Функция для тестирования get_mask_card_number если введена пустая строка"""
    assert src.masks.get_mask_card_number("") == "Введён некорректный номер карты"


def test_get_mask_account() -> None:
    """Функция для тестирования get_mask_account в базовом случае"""
    assert src.masks.get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_wrong() -> None:
    """Функция для тестирования get_mask_account если введен некорректный номер счета"""
    assert src.masks.get_mask_account("73654tars30135874305") == "Введён некорректный номер счёта"


def test_get_mask_account_wrong_length() -> None:
    """Функция для тестирования get_mask_account если введен некорректный номер счета"""
    assert src.masks.get_mask_account("73654") == "Введён некорректный номер счёта"
