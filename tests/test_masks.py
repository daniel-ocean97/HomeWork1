import src.masks


def test_get_mask_card_number():
    assert src.masks.get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


def test_get_mask_card_number_wrong():
    assert src.masks.get_mask_card_number('700fjghfs2289606') == 'Введён некорректный номер карты'


def test_get_mask_card_number_without_number():
    assert src.masks.get_mask_card_number('') == 'Введён некорректный номер карты'


def test_get_mask_account():
    assert src.masks.get_mask_account('73654108430135874305') == '**4305'


def test_get_mask_account_wrong():
    assert src.masks.get_mask_account('73654tars30135874305') == 'Введён некорректный номер счёта'


def test_get_mask_account_wrong_length():
    assert src.masks.get_mask_account('73654') == 'Введён некорректный номер счёта'


