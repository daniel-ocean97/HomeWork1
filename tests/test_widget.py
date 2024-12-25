import pytest

import src.widget
import src.masks


@pytest.mark.parametrize('account_card, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                    ('Счет 73654108430135874305', 'Счет **4305'),
                                                    ('MasterCard 726758', 'Введена некорректная карта аккаунта'),
                                                    ('Счет 353вава33474447895560', 'Введена некорректная карта аккаунта'),
                                                    ('Счет ', 'Введена некорректная карта аккаунта'),
                                                    ('Visa Platinum ', 'Введена некорректная карта аккаунта')])
def test_mask_account_card(account_card, expected):
    assert src.widget.mask_account_card(account_card) == expected


@pytest.mark.parametrize('date_need_to_format, expected', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                                           ('20240311T02:26:18.671407', 'Неверный формат строки'),
                                                           ('2024-03-11', 'Неверный формат строки'),
                                                           ('20245-03-11T02:26:18.671407', 'Неверный формат строки')])
def test_get_date(date_need_to_format, expected):
    assert src.widget.get_date(date_need_to_format) == expected